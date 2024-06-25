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
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7369126743:AAEaysZ7E0k-CB2DeWuOePmWamDytWQc09Y")
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
    HOTSTAR_USER_TOKEN = os.environ.get("HOTSTAR_USER_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTcxOTA2NDgwMywiaWF0IjoxNzE4OTc4NDAzLCJpc3MiOiJUUyIsImp0aSI6IjU5NDg3MjY0NjhhYTRlNjM5YjJiNDgzMmQwNzkzMzk1Iiwic3ViIjoie1wiaElkXCI6XCJlMjFmODlmMzNkOTY0NzVhODYyZmQ3YmNiM2IyZTIxOVwiLFwicElkXCI6XCIwNDQxMDNmNjcxNWM0YjkxYjM5N2MzMmQ2MTE2MmRmNFwiLFwibmFtZVwiOlwiS2lkc1wiLFwicGhvbmVcIjpcIjgyMTgzMDg3NjJcIixcImlwXCI6XCIyNDA1OjIwMTo2ODFiOjIwN2U6MzhmMzpiZjcxOmI0ZmM6ZGY5OVwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJwaG9uZVwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjp0cnVlLFwiZGV2aWNlSWRcIjpcIjM4MWY0NC0xMWQzMjAtMmI5OTk0LTQ2MzZjOVwiLFwicHJvZmlsZVwiOlwiS0lEU1wiLFwidmVyc2lvblwiOlwidjJcIixcInN1YnNjcmlwdGlvbnNcIjp7XCJpblwiOntcIkhvdHN0YXJCdW5kbGVcIjp7XCJzdGF0dXNcIjpcIlNcIixcImV4cGlyeVwiOlwiMjAyNC0wNy0yMlQxMDoyOTo1OS4wMDBaXCIsXCJzaG93QWRzXCI6XCIxXCIsXCJjbnRcIjpcIjFcIn19fSxcImVudFwiOlwiQ3NrQkNnVUtBd29CQlJLL0FSSUhZVzVrY205cFpCSURhVzl6RWdsaGJtUnliMmxrZEhZU0JtWnBjbVYwZGhJSFlYQndiR1YwZGhJRWNtOXJkUklEZDJWaUVnUnRkMlZpRWdkMGFYcGxiblIyRWdWM1pXSnZjeElHYW1sdmMzUmlFZ3BqYUhKdmJXVmpZWE4wRWdSMGRtOXpFZ1J3WTNSMkVnTnFhVzhTQjJwcGJ5MXNlV1lhQW5Oa0dnSm9aQm9EWm1oa0lnTnpaSElpQldoa2NqRXdJZ3RrYjJ4aWVYWnBjMmx2YmlvR2MzUmxjbVZ2S2doa2IyeGllVFV1TVNvS1pHOXNZbmxCZEcxdmMxZ0JDZzBTQ3doa09BWkFBVkM0Q0ZnQkNpSUtHZ29PRWdVMU5UZ3pOaElGTmpRd05Ea0tDQ0lHWm1seVpYUjJFZ1E0WkZnQkN0d0JDZ1VLQXdvQkFCTFNBUklIWVc1a2NtOXBaQklEYVc5ekVnbGhibVJ5YjJsa2RIWVNCbVpwY21WMGRoSUhZWEJ3YkdWMGRoSUVjbTlyZFJJRGQyVmlFZ1J0ZDJWaUVnZDBhWHBsYm5SMkVnVjNaV0p2Y3hJR2FtbHZjM1JpRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0IycHBieTFzZVdZU0JIaGliM2dTQzNCc1lYbHpkR0YwYVc5dUdnSnpaQm9DYUdRYUEyWm9aQ0lEYzJSeUlnVm9aSEl4TUNJTFpHOXNZbmwyYVhOcGIyNHFCbk4wWlhKbGJ5b0laRzlzWW5rMUxqRXFDbVJ2YkdKNVFYUnRiM05ZQVJKUkNBRVEyTmoyejQweUdrUUtHa3BwYnk1SlRpNUNkVzVrYkdVdVRXOXVkR2hzZVM1R1ZGUklFZzFJYjNSemRHRnlRblZ1Wkd4bEdnTktTVThna0pUVXo5c3dLTmpZOXMrTk1qQUdPQUZBQXpBQlwiLFwiaXNzdWVkQXRcIjoxNzE4OTc4NDAzNzE0LFwibWF0dXJpdHlMZXZlbFwiOlwiVS9BIDcrXCIsXCJpbWdcIjpcIjE5XCIsXCJkcGlkXCI6XCI1ZmI0Yjc0OWNmOTA0ODc4YmU5MmZhYWM2ZTJiNjliN1wiLFwic3RcIjoxLFwiZGF0YVwiOlwiQ2dRSUFCSUFDZ1FJQURJQUNoSUlBQ0lPZ0FFWGlBRUJrQUhJcDcrazJ6QUtCQWdBT2dBS0xnZ0FRaW9LS0VJM1pqQTBOV000TlRJMk0ySTBZV00yT1RkaU1EYzJZMkl3TWpRMU1qWmtNM00yYVhoSFkxSUtrQUVJQUNxTEFRb3pDZ0FTTHdvRGFHbHVHaElTQ2pFeU5qQXdNakV3TURRWXBwemxxUVlhRkFnQ0VncGthWE51Wlhsd2JIVnpHS2FjNWFrR0NoRUtBZ2dDRWdVS0EyaHBiaGkzbnRLekJnb2JDZ2NJQVJVQUFBQkFFZ29LQTJocGJpVUFBSUEvR0xlZTByTUdDaEVLQWdnREVnVUtBMmhwYmhpM250S3pCZ29SQ2dJSUJCSUZDZ05vYVc0WXQ1N1Nzd1k9XCJ9IiwidmVyc2lvbiI6IjFfMCJ9.P9TgPapWIP4UJm6r4hTW43HIAisiT8rlVcnFQI2rcgk")
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
