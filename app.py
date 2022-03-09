from logging.handlers import RotatingFileHandler
from twilio.rest import Client
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import datetime, requests, os, logging, time

load_dotenv()

closed = False
contacts = []

url = 'https://nationalhighways.co.uk/travel-updates/the-severn-bridges/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

status = soup.findAll('div', {'class':'severn-crossing-status'})

old_bridge = status[0].text.strip()
new_bridge = status[1].text.strip()

def log(msg):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(os.getenv('LOG_PATH'), maxBytes=100000000, backupCount=5)
    logger.addHandler(handler)
    
    logger.info("[{}] {}".format(str(datetime.datetime.now()), msg))
    time.sleep(1)
    logger.info("[{}] Message Sent.".format(str(datetime.datetime.now())))

def notify(msg):
    body = '''
    [ALERT]

    Severn Bridge Status: "{}"
    '''.format(msg)

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    for number in contacts:
        message = client.messages.create(body=body, from_=os.getenv('TWILIO_PHONE'), to=number)
        log(msg)
        print(message.sid)

if 'closed' in old_bridge.lower():
    if closed == True: # if was already closed do not message again
        pass
    else:
        notify(old_bridge) # if was open now closed send message
else:
    if closed == True:
        notify(old_bridge) # if was closed now open send message
    else:
        pass # if was never closed always open do not send message