
# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '4707251'))
    API_HASH = str(getenv('API_HASH', '800f04bcf6c37b78b52be670789ea81a'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6585910708:AAFc8sjxkyrb7bOiC-3f67ziFmi_8ackv8A'))
    name = str(getenv('name', 'tentukotta'))
    PIC = str(getenv('PIC', 'https://i.ibb.co/r5zsPW1/logo.jpg'))
    TUTORIAL_VIDEO = str(getenv('TUTORIAL_VIDEO', 'https://telegra.ph/file/35bfe15a705d870a47f85.mp4'))
    SHORTENER_API = str(getenv('SHORTENER_API', 'f13ca81474b71eb9453255d75ed304ca21b3bf63'))
    SHORTENER_URL = str(getenv('SHORTENER_URL', 'https://tnshort.net/api'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    BOT_USERNAME = str(getenv('BOT_USERNAME', 'filetolinkmbm_bot')) #without @ symbol
    BOT_NAME = str(getenv('BOT_NAME', 'Tentukotta Streaming Bot'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001587191598'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1001721054").split())
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://tentukottamovie:148644@cluster0.lc31g6b.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))  
