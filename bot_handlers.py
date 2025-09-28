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