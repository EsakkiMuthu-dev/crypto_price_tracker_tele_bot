# Crypto coin Price Tracker Telegram Bot
**Hii friends👬.. this Telegram bot tracks the prices of crypto currencies 


## Deploying Python Selenium based project live into Heroku.

**Article based on YouTube video:**

**English : https://youtu.be/kHByjOJh7O0**

**Malayalam : https://youtu.be/7glbuNJN_6A**

**Usage ** 

**Initial Configuration in the script**

**- chrome_options = webdriver.ChromeOptions()**

**- chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")**

**-chrome_options.add_argument("--headless")**

**-chrome_options.add_argument("--disable-dev-shm-usage")**

**-chrome_options.add_argument("--no-sandbox")**

**-driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)**

**-Heroku Configuration**

**-Heroku buildpacks**

**Python (Select it from the officially supported buildpacks)**

**Headless Google Chrome**

**Chromedrive**r

**Heroku config variables
CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver
requirements.txt
Procfile
web: python main.py**
