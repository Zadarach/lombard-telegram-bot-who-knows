import aiohttp
from bs4 import BeautifulSoup
import re
from typing import List, Dict
from config import Config
from database import Database
import asyncio

class LombardScraper:
    def __init__(self):
        self.db = Database()
        self.session = None
    
    async def get_session(self):
        """Uzyskaj sesję aiohttp"""
        if not self.session:
            self.session = aiohttp.ClientSession(
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                },
                timeout=aiohttp.ClientTimeout(total=30)
            )
        return self.session
    
    async def scan_all_pages(self) -> Dict:
        """Skanuj wszystkie 3 strony"""
        all_offers = []
        session = await self.get_session()
        
        for i, url in enumerate(Config.URLS, 1):
            print(f"🔍 Skanuję stronę {i}/3...")
            offers = await self.scan_page(url, session)
            all_offers.extend(offers)
            await asyncio.sleep(1)  # Opóźnienie między stronami
        
        # Filtruj i zapisz do bazy
        filtered_offers = self.filter_offers(all_offers)
        new_offers = self.db.save_offers(filtered_offers)
        
        return {
            'total_found': len(all_offers),
            'after_filtering': len(filtered_offers),
            'new_offers': new_offers
        }
    
    async def scan_page(self, url: str, session: aiohttp.ClientSession) -> List[Dict]:
        """Skanuj pojedynczą stronę"""
        try:
            async with session.get(url) as response:
                if response.status != 200:
                    print(f"❌ Błąd HTTP {response.status} dla {url}")
                    return []
                
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                offers = []
                
                # Znajdź wszystkie karty produktów - używam różnych selektorów na wszelki wypadek
                product_cards = soup.find_all('div', {'data-v-6f316315': True}) or \
                               soup.find_all('div', class_=re.compile('product')) or \
                               soup.select('[data-v-6f316315]')
                
                print(f"📦 Znaleziono {len(product_cards)} kart produktów")
                
                for card in product_cards:
                    offer = self.parse_offer(card)
                    if offer:
                        offers.append(offer)
                
                return offers
                
        except Exception as e:
            print(f"❌ Błąd skanowania {url}: {e}")
            return []
    
    def parse_offer(self, card) -> Dict:
        """Parsuj pojedynczą ofertę"""
        try:
            # Tytuł
            title_element = card.find('h2', class_='product-title')
            if not title_element:
                return None
            
            title_link = title_element.find('a')
            if not title_link:
                return None
            
            title = title_link.get_text(strip=True)
            link = title_link.get('href', '')
            
            # Cena
            price_element = card.find('p', class_='product-value')
            if not price_element:
                return None
            
            price_text = price_element.get_text(strip=True)
            price_num = int(re.sub(r'[^\d]', '', price_text))
            
            # Stan i lokalizacja
            desc_elements = card.find_all('p', class_='product-desc')
            location = "Nieznana"
            condition_status = "Nieznany"
            
            for desc in desc_elements:
                text = desc.get_text(strip=True)
                if 'Lokalizacja:' in text:
                    location = text.replace('Lokalizacja:', '').strip()
                elif 'Stan:' in text:
                    condition_status = text.replace('Stan:', '').strip()
            
            # Pełny link
            full_link = f"https://www.loombard.pl{link}" if not link.startswith('http') else link
            
            return {
                'title': title,
                'price': price_num,
                'location': location,
                'condition_status': condition_status,
                'link': full_link
            }
            
        except Exception as e:
            print(f"❌ Błąd parsowania oferty: {e}")
            return None
    
    def filter_offers(self, offers: List[Dict]) -> List[Dict]:
        """Filtruj oferty - usuń te z 'złymi' słowami kluczowymi"""
        filtered = []
        
        for offer in offers:
            title_lower = offer['title'].lower()
            location_lower = offer['location'].lower()
            
            # Sprawdź czy zawiera złe słowa kluczowe
            has_bad_keyword = any(
                keyword in title_lower or keyword in location_lower
                for keyword in Config.BAD_KEYWORDS
            )
            
            if not has_bad_keyword:
                filtered.append(offer)
            else:
                print(f"🚫 Odfiltrowano: {offer['title'][:50]}...")
        
        return sorted(filtered, key=lambda x: x['price'])  # Sortuj po cenie
    
    async def close(self):
        """Zamknij sesję"""
        if self.session:
            await self.session.close()