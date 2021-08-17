

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.chrome.webdriver.WebDriver(executable_path='/usr/local/bin/chromedriver')
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


import time
url = 'https://coinswitch.co/' 
driver.get(url)
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

# start function
def start(update, context):
    """Send a message when the command /start is issued."""
    
    while True:
        # fecthing crypto names
        labels = driver.find_elements_by_css_selector(".ticker .ticker__asset-name") 
        ls =[]
        for label in labels:
            b = label.text
            ls.append(b)
        crypto =ls[0:2]

        #fetching their prices
        labels1 = driver.find_elements_by_css_selector(".ticker .ticker__price") 
        lf =[]
        for label in labels1:
            a = label.text
            a = a[1:]
            lf.append(a)
                
        price = lf[0:2]

        scrap = dict(zip(crypto,price))
            
            
        for i,j in scrap.items():
            update.message.reply_text('cryptocurrency name is :'+i +'\nprice of the currency :₹'+ j +'\n')
            
        bitcoin = float(lf[0])
        deal_price = 3500000.00 # you can change the deal price

        if bitcoin <= deal_price:
            for i in range(20):
                update.message.reply_text('inga enna pakkuura 🧐 buy pannu da pakki..oduuuu🏃..💰price of bitcoin : ₹'+''+str(bitcoin))
                
        else:
            update.message.reply_text('ippo buy panna venam🙅🏻‍♂.. innum price kammi aagala😤... 💰price of bitcoin:₹'+''+str(bitcoin))
        
        break   
    update.message.reply_text('do you wanna get crypto prices for every 10 mins . smash the /subscribe button')

# it starts the loop when you subscribes
def subscribe(update,context):
    update.message.reply_text('Hi!.thankyou for choosing us!!..')
    while True:
            # fecthing crypto names
        labels = driver.find_elements_by_css_selector(".ticker .ticker__asset-name") 
        ls =[]
        for label in labels:
            b = label.text
            ls.append(b)
        crypto =ls[0:2]

        #fetching their prices
        labels1 = driver.find_elements_by_css_selector(".ticker .ticker__price") 
        lf =[]
        for label in labels1:
            a = label.text
            a = a[1:]
            lf.append(a)
                
        price = lf[0:2]

        scrap = dict(zip(crypto,price))
            
            
        bitcoin = float(lf[0])
        deal_price = 3500000.00 # you can change the deal price

        if bitcoin <= deal_price:
            for i in range(20):
                update.message.reply_text('inga enna pakkuura 🧐 buy pannu da pakki..oduuuu🏃..💰price of bitcoin : ₹'+''+str(bitcoin))
                
        else:
            update.message.reply_text('ippo buy panna venam🙅🏻‍♂.. innum price kammi aagala😤... 💰price of bitcoin:₹'+''+str(bitcoin))
        time.sleep(900)
        driver.refresh()

 

   
     
  
        
 


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/start - starts our bot'+'\n'+'/help - for help contact us+'+'\n'+'/subscribe - subscribe to our bot for instant updates')



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1926440903:AAF2zAbHknV3qculO4RgSQjmgjDLajn3LWI", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("subscribe", subscribe))


  

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()