# requirements.txt
"""
python-telegram-bot==20.7
requests==2.31.0
beautifulsoup4==4.12.2
lxml==4.9.3
python-dotenv==1.0.0
schedule==1.2.0
aiohttp==3.9.1
"""

# .env (utwórz ten plik)
"""
TELEGRAM_TOKEN=7694975534:AAHISLJqI94XrekJ6FpP252Z9hhZCG_RJsA
"""

# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '7694975534:AAHISLJqI94XrekJ6FpP252Z9hhZCG_RJsA')
    
    # URLs do skanowania (3 strony)
    BASE_URL = "https://www.loombard.pl/categories/smartfony-i-telefony-komorkowe-WDK5Fy"
    BASE_PARAMS = "price%5Bfrom%5D=1500&price%5Bto%5D=3150&region=&location=&localization=&parameters%5B4386%5D%5Btype%5D=dictionary_checkbox&parameters%5B248862%5D%5Btype%5D=dictionary_checkbox&parameters%5B202849%5D%5Bvalue%5D=&parameters%5B202849%5D%5Btype%5D=number&parameters%5B202841%5D%5Btype%5D=dictionary_checkbox&parameters%5B225693%5D%5Bvalue%5D=&parameters%5B225693%5D%5Btype%5D=string&parameters%5B202873%5D%5Btype%5D=dictionary_checkbox&parameters%5B202833%5D%5Btype%5D=dictionary_checkbox&parameters%5B202733%5D%5Btype%5D=dictionary_checkbox&parameters%5B202829%5D%5Btype%5D=dictionary_checkbox&parameters%5B202753%5D%5Bvalue%5D=&parameters%5B202753%5D%5Btype%5D=number&parameters%5B245581%5D%5Bvalue%5D=&parameters%5B245581%5D%5Btype%5D=number&parameters%5B218669%5D%5Btype%5D=dictionary_checkbox&parameters%5B247945%5D%5Btype%5D=dictionary_checkbox&parameters%5B248255%5D%5Bvalue%5D=&parameters%5B248255%5D%5Btype%5D=number&parameters%5B224017%5D%5Bvalue%5D=&parameters%5B224017%5D%5Btype%5D=string&parameters%5B249512%5D%5Btype%5D=dictionary_checkbox&parameters%5B219%5D%5Btype%5D=dictionary_checkbox&parameters%5B202877%5D%5Bvalue%5D=&parameters%5B202877%5D%5Btype%5D=number&parameters%5B202857%5D%5Btype%5D=dictionary_checkbox&parameters%5B219773%5D%5Bvalue%5D=&parameters%5B219773%5D%5Btype%5D=string&parameters%5B246705%5D%5Btype%5D=dictionary_checkbox&parameters%5B202741%5D%5Btype%5D=dictionary_checkbox&parameters%5B246737%5D%5Btype%5D=dictionary_checkbox&parameters%5B202845%5D%5Btype%5D=dictionary_checkbox&parameters%5B250791%5D%5Btype%5D=dictionary_checkbox&parameters%5B202821%5D%5Btype%5D=dictionary_checkbox&parameters%5B202865%5D%5Btype%5D=dictionary_checkbox&parameters%5B202717%5D%5Bvalue%5D=&parameters%5B202717%5D%5Btype%5D=number&parameters%5B249565%5D%5Btype%5D=dictionary_checkbox&parameters%5B202749%5D%5Bvalue%5D=&parameters%5B202749%5D%5Btype%5D=number&parameters%5B202745%5D%5Btype%5D=dictionary_checkbox&parameters%5B202729%5D%5Bvalue%5D=&parameters%5B202729%5D%5Btype%5D=number&parameters%5B202725%5D%5Bvalue%5D=&parameters%5B202725%5D%5Btype%5D=number&parameters%5B202757%5D%5Btype%5D=dictionary_checkbox&parameters%5B202737%5D%5Btype%5D=dictionary_checkbox&parameters%5B202861%5D%5Btype%5D=dictionary_checkbox&parameters%5B11323%5D%5Btype%5D=dictionary_checkbox&parameters%5B229205%5D%5Btype%5D=dictionary_checkbox&parameters%5B4388%5D%5Btype%5D=dictionary_checkbox&parameters%5B227381%5D%5Bvalue%5D=&parameters%5B227381%5D%5Btype%5D=number&parameters%5B249446%5D%5Btype%5D=dictionary_checkbox&parameters%5B217%5D%5Btype%5D=dictionary_checkbox&parameters%5B202685%5D%5Btype%5D=dictionary_checkbox&parameters%5B202713%5D%5Btype%5D=dictionary_checkbox&parameters%5B219765%5D%5Bvalue%5D=&parameters%5B219765%5D%5Btype%5D=string&parameters%5B202705%5D%5Bvalue%5D=&parameters%5B202705%5D%5Btype%5D=number&parameters%5B17448%5D%5Bvalue%5D=&parameters%5B17448%5D%5Btype%5D=number&parameters%5B202869%5D%5Btype%5D=dictionary_checkbox&parameters%5B202853%5D%5Btype%5D=dictionary_checkbox&parameters%5B227357%5D%5Bvalue%5D=&parameters%5B227357%5D%5Btype%5D=number&parameters%5B250685%5D%5Btype%5D=dictionary_checkbox&parameters%5B202837%5D%5Btype%5D=dictionary_checkbox&parameters%5B249445%5D%5Btype%5D=dictionary_checkbox&searchQuery=&per_page=192"
    
    URLS = [
        f"{BASE_URL}?{BASE_PARAMS}&page=1",
        f"{BASE_URL}?{BASE_PARAMS}&page=2", 
        f"{BASE_URL}?{BASE_PARAMS}&page=3"
    ]
    
    # Filtery - frazy do odrzucenia
    BAD_KEYWORDS = [
        'zablokowany', 'z a b l o k o w a n y', 'operator', 'operatora', 
        'na części', 'nie działa', 'uszkodzony', 'simlock', 'bez ładowarki', 
        'tylko obudowa', 'nie uruchamia', 'rozbity', 'pęknięty', 'zalany',
        'nie ładuje', 'czarny ekran', 'dead boot'
    ]
    
    # Baza danych
    DB_FILE = 'lombard.db'
    
    # Automatyczne skanowanie co X minut
    SCAN_INTERVAL = 30

# database.py
import sqlite3
from typing import List, Dict
from config import Config
from datetime import datetime

class Database:
    def __init__(self):
        self.init_db()
    
    def init_db(self):
        """Inicjalizuj bazę danych"""
        conn = sqlite3.connect(Config.DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS offers (
                id INTEGER PRIMARY KEY,
                title TEXT,
                price INTEGER,
                location TEXT,
                condition_status TEXT,
                link TEXT UNIQUE,
                found_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                watch_enabled BOOLEAN DEFAULT 0,
                last_notified TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_offers(self, offers: List[Dict]):
        """Zapisz oferty do bazy"""
        conn = sqlite3.connect(Config.DB_FILE)
        cursor = conn.cursor()
        
        new_offers = 0
        for offer in offers:
            try:
                cursor.execute('''
                    INSERT OR REPLACE INTO offers 
                    (title, price, location, condition_status, link)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    offer['title'], offer['price'], offer['location'],
                    offer['condition_status'], offer['link']
                ))
                new_offers += 1
            except Exception as e:
                print(f"Błąd zapisywania oferty: {e}")
        
        conn.commit()
        conn.close()
        return new_offers
    
    def get_best_offers(self, limit: int = 5) -> List[Dict]:
        """Pobierz najlepsze oferty"""
        conn = sqlite3.connect(Config.DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT title, price, location, condition_status, link, found_at
            FROM offers 
            WHERE is_active = 1
            ORDER BY price ASC 
            LIMIT ?
        ''', (limit,))
        
        offers = cursor.fetchall()
        conn.close()
        
        return [
            {
                'title': row[0],
                'price': row[1], 
                'location': row[2],
                'condition_status': row[3],
                'link': row[4],
                'found_at': row[5]
            }
            for row in offers
        ]
    
    def get_stats(self) -> Dict:
        """Pobierz statystyki"""
        conn = sqlite3.connect(Config.DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM offers WHERE is_active = 1')
        total_offers = cursor.fetchone()[0]
        
        cursor.execute('SELECT MIN(price), MAX(price), AVG(price) FROM offers WHERE is_active = 1')
        price_stats = cursor.fetchone()
        
        conn.close()
        
        return {
            'total_offers': total_offers,
            'min_price': price_stats[0] if price_stats[0] else 0,
            'max_price': price_stats[1] if price_stats[1] else 0,
            'avg_price': round(price_stats[2], 2) if price_stats[2] else 0
        }

# scraper.py
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

# bot_handlers.py
from telegram import Update
from telegram.ext import ContextTypes
from database import Database
from scraper import LombardScraper
import asyncio
from datetime import datetime

class BotHandlers:
    def __init__(self, db: Database, scraper: LombardScraper):
        self.db = db
        self.scraper = scraper
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Komenda /start"""
        stats = self.db.get_stats()
        await update.message.reply_text(
            f"🤖 *Lombard Bot* - Najlepsze oferty telefonów!\n\n"
            f"📱 Monitoruję smartfony w przedziale 1500-3150 zł\n"
            f"📊 W bazie: {stats['total_offers']} ofert\n\n"
            f"🚀 *Komendy:*\n"
            f"/scan - Skanuj 3 strony teraz\n"
            f"/best - Pokaż TOP 5 ofert\n"
            f"/stats - Statystyki bazy\n"
            f"/help - Pomoc\n\n"
            f"⚡ Bot automatycznie skanuje co {Config.SCAN_INTERVAL} minut",
            parse_mode='Markdown'
        )
    
    async def scan_now(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Komenda /scan - skanuj teraz"""
        msg = await update.message.reply_text("🔄 Skanuję 3 strony...")
        
        try:
            start_time = datetime.now()
            results = await self.scraper.scan_all_pages()
            scan_time = (datetime.now() - start_time).seconds
            
            await msg.edit_text(
                f"✅ *Skanowanie zakończone!* ({scan_time}s)\n\n"
                f"🔍 Znaleziono: {results['total_found']} ofert\n"
                f"✅ Po filtrach: {results['after_filtering']} ofert\n"
                f"🆕 Nowych: {results['new_offers']} ofert\n\n"
                f"Użyj /best aby zobaczyć najlepsze oferty!",
                parse_mode='Markdown'
            )
        except Exception as e:
            await msg.edit_text(f"❌ Błąd skanowania: {str(e)}")
    
    async def show_best(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Komenda /best - pokaż najlepsze oferty"""
        offers = self.db.get_best_offers(5)
        
        if not offers:
            await update.message.reply_text(
                "😔 Brak ofert w bazie.\n\nUżyj /scan aby zeskanować strony!"
            )
            return
        
        message = "🏆 *TOP 5 NAJLEPSZYCH OFERT:*\n\n"
        
        for i, offer in enumerate(offers, 1):
            # Skróć tytuł jeśli za długi
            title = offer['title'][:60] + "..." if len(offer['title']) > 60 else offer['title']
            
            message += (
                f"*{i}. {title}*\n"
                f"💰 Cena: *{offer['price']:,} zł*\n"
                f"📍 {offer['location']}\n"
                f"🏷️ Stan: {offer['condition_status']}\n"
                f"🔗 [Zobacz ofertę]({offer['link']})\n\n"
            )
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def show_stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Pokaż statystyki"""
        stats = self.db.get_stats()
        
        await update.message.reply_text(
            f"📊 *STATYSTYKI BAZY:*\n\n"
            f"📱 Ofert w bazie: *{stats['total_offers']:,}*\n"
            f"💰 Najtańsza: *{stats['min_price']:,} zł*\n"
            f"💎 Najdroższa: *{stats['max_price']:,} zł*\n"
            f"📈 Średnia cena: *{stats['avg_price']:,} zł*\n\n"
            f"🔄 Ostatnie skanowanie: właśnie teraz\n"
            f"⚡ Następne za: {Config.SCAN_INTERVAL} minut",
            parse_mode='Markdown'
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Komenda /help"""
        await update.message.reply_text(
            f"📚 *POMOC - Lombard Bot*\n\n"
            f"🤖 Bot automatycznie skanuje 3 strony Lombard.pl\n"
            f"💰 Przedział cenowy: 1500-3150 zł\n"
            f"🚫 Automatyczne filtrowanie uszkodzonych/zablokowanych\n\n"
            f"*📋 KOMENDY:*\n"
            f"🔍 /scan - Skanuj strony teraz\n" 
            f"🏆 /best - TOP 5 najlepszych ofert\n"
            f"📊 /stats - Statystyki bazy danych\n"
            f"❓ /help - Ta pomoc\n\n"
            f"*🚫 FILTROWANE FRAZY:*\n"
            f"• zablokowany / operator\n"
            f"• na części / nie działa\n"
            f"• uszkodzony / rozbity\n"
            f"• simlock / bez ładowarki\n\n"
            f"💡 Bot działa 24/7 i automatycznie skanuje co {Config.SCAN_INTERVAL} min!",
            parse_mode='Markdown'
        )

# main.py
import asyncio
import logging
from telegram.ext import Application, CommandHandler
from bot_handlers import BotHandlers
from scraper import LombardScraper
from database import Database
from config import Config
from datetime import datetime

# Konfiguracja logowania
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class LombardBot:
    def __init__(self):
        self.db = Database()
        self.scraper = LombardScraper()
        self.handlers = BotHandlers(self.db, self.scraper)
        self.auto_scan_task = None
        
    async def start_bot(self):
        """Uruchom bota Telegram"""
        print("🚀 Uruchamianie Lombard Bot...")
        
        app = Application.builder().token(Config.TELEGRAM_TOKEN).build()
        
        # Dodaj handlery
        app.add_handler(CommandHandler("start", self.handlers.start))
        app.add_handler(CommandHandler("scan", self.handlers.scan_now))
        app.add_handler(CommandHandler("best", self.handlers.show_best))
        app.add_handler(CommandHandler("stats", self.handlers.show_stats))
        app.add_handler(CommandHandler("help", self.handlers.help_command))
        
        # Uruchom automatyczne skanowanie w tle
        self.auto_scan_task = asyncio.create_task(self.auto_scan_loop())
        
        print("✅ Bot gotowy!")
        print(f"🔍 Automatyczne skanowanie co {Config.SCAN_INTERVAL} minut")
        
        # Uruchom bota
        await app.run_polling(drop_pending_updates=True)
    
    async def auto_scan_loop(self):
        """Automatyczne skanowanie co X minut"""
        await asyncio.sleep(10)  # Poczekaj 10 sekund po starcie
        
        while True:
            try:
                print(f"🔄 Auto scan rozpoczęty - {datetime.now()}")
                results = await self.scraper.scan_all_pages()
                print(f"✅ Auto scan zakończony - znaleziono {results['after_filtering']} ofert")
                
            except Exception as e:
                print(f"❌ Auto scan error: {e}")
            
            # Czekaj następne skanowanie
            await asyncio.sleep(Config.SCAN_INTERVAL * 60)
    
    async def shutdown(self):
        """Zamknij bota"""
        if self.auto_scan_task:
            self.auto_scan_task.cancel()
        await self.scraper.close()

# Główna funkcja
async def main():
    bot = LombardBot()
    try:
        await bot.start_bot()
    except KeyboardInterrupt:
        print("🛑 Zamykanie bota...")
        await bot.shutdown()

if __name__ == "__main__":
    asyncio.run(main())

# Dockerfile (dla Railway/Render)
"""
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
"""

# railway.json (dla Railway)
"""
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python main.py",
    "healthcheckPath": "/",
    "healthcheckTimeout": 300,
    "sleepApplication": false
  }
}
"""