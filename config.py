import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env', override=True)

class Config(object):
    ##API_KEY get it from dev, dont edit if added
    API_KEY = os.environ.get("API_KEY", "6607cc1ef9e03346e48c886d")
    #telegram user session str for 4gb limit
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQGlVqIAaQCW7onbtdCbesyxExwOHWBZeA-bYLODgc95BpZSiHbwqGA0CC8_9EDtVxhSjDnAlLRGO3wM-oFp4CGEWCIn1Q996Xz4jCAlXPbc4eHRI06yRuuE3K_rd1uuBoL2IrdDaOA3447-dwVkdWRhH2yYrisu0NhFPEX4tXORVGhAw6NJSv5wjZ1-wzsRZZFHpTsCPSr8RybxCOWYiBZUpjNc1JPkNBPgr1KU4XOQbvjU2wen751Sbl-_8-Mcr1HRx-p37sYOqpbikMyhOb4hYEdZHmx09j7BIqyYp5tcqJGhffFnl0P2evPUlxgNh-wuwUIZbGQ8b7rHWdaRbQ-Bb1q0AQAAAAGKB0kwAA")
    #tg bot token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6789408604:AAFRp8uDWavFhBFhpjb8lXbS805FUtVKIBQ")
    #api id and hash get it from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 27612834))
    API_HASH = os.environ.get("API_HASH", "28d176c899b65da009467232171d60f9")
    #Proxy url leave blank if dont have, eg "http://13.42.34.52:52380"
    PROXY = os.environ.get("PROXY", "")
    #mongodb url get it from mongodb.com
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://animebash32:animebash3222@cluster0.tcey822.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    #owner id
    OWNER_ID = [int(i) for i in  os.environ.get("OWNER_ID", "5574593875").split(" ")]
    #log channel, where to send logs
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002200330916"))
    #gdrive folder id for upload
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "1-geGQG9k7_idJ0876uDYqTe")
    #use service accounts or not, used to bypass daily upload limit
    USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS","False")
    #is team drive
    IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", "True")
    #index url of gdrive folder
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://widewine.example.workers.dev/0:/BOT")
    ###JIO_CINEMA_TOKEN###
    #JIO_CINEMA_TOKEN = os.environ.get("JIO_CINEMA_TOKEN", "")
    #JIO_CINEMA_DEVICE_ID = os.environ.get("JIO_CINEMA_DEVICE_ID", "")
    #JIO_CINEMA_REFRESH_TOKEN = os.environ.get("JIO_CINEMA_REFRESH_TOKEN", "")
    ###HotsStar token###
    HOTSTAR_USER_TOKEN = os.environ.get("HOTSTAR_USER_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTcxODk4NTk3OCwiaWF0IjoxNzE4ODk5NTc4LCJpc3MiOiJUUyIsImp0aSI6ImM3ZDM4Mzk4MmY1ZjRkNmI5YTJmZTVkNWNkMzY0MGMxIiwic3ViIjoie1wiaElkXCI6XCJlMjFmODlmMzNkOTY0NzVhODYyZmQ3YmNiM2IyZTIxOVwiLFwicElkXCI6XCIwNDQxMDNmNjcxNWM0YjkxYjM5N2MzMmQ2MTE2MmRmNFwiLFwibmFtZVwiOlwiS2lkc1wiLFwicGhvbmVcIjpcIjgyMTgzMDg3NjJcIixcImlwXCI6XCIyNDA1OjIwMTo2ODFiOjIwN2U6MThkZTplNmQ1OjY1OGU6NDJmN1wiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJwaG9uZVwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjp0cnVlLFwiZGV2aWNlSWRcIjpcIjNmNWZjNy00ZDczYS0xOWFmNDAtNTJmNmNjXCIsXCJwcm9maWxlXCI6XCJLSURTXCIsXCJ2ZXJzaW9uXCI6XCJ2MlwiLFwic3Vic2NyaXB0aW9uc1wiOntcImluXCI6e1wiSG90c3RhckJ1bmRsZVwiOntcInN0YXR1c1wiOlwiU1wiLFwiZXhwaXJ5XCI6XCIyMDI0LTA2LTIyVDEwOjI5OjU5LjAwMFpcIixcInNob3dBZHNcIjpcIjFcIixcImNudFwiOlwiMVwifX19LFwiZW50XCI6XCJDc2tCQ2dVS0F3b0JCUksvQVJJSFlXNWtjbTlwWkJJRGFXOXpFZ2xoYm1SeWIybGtkSFlTQm1acGNtVjBkaElIWV")
    #Metadata and Name at end of file
    END_NAME = os.environ.get("END_NAME", "@SharkToonsIndia")
    METADATA_NAME = os.environ.get("METADATA_NAME", "@SharkToonsIndia")
    #ur choice
    TEMP_DIR = os.environ.get("TEMP_DIR", "output")
    TG_SPLIT_SIZE = int(os.environ.get("TG_SPLIT_SIZE","2000000000"))
    ##############Dont touch##############
    if SESSION_STRING == "" or SESSION_STRING is None:
        TG_SPLIT_SIZE = TG_SPLIT_SIZE
    USE_SERVICE_ACCOUNTS = USE_SERVICE_ACCOUNTS.lower() == "true"
    IS_TEAM_DRIVE = IS_TEAM_DRIVE.lower() == "true"
    HOTSTAR_REFRESH = 0.0
