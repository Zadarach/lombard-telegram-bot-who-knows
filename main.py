import asyncio
import logging
from telegram.ext import Application, CommandHandler
from bot_handlers import BotHandlers
from scraper import LombardScraper
from database import Database
from config import Config
from datetime import datetime

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