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
