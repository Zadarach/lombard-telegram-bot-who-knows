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