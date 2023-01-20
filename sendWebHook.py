# Send telegram messages using the webhook
# sendWebHook.py 

def sendTelegram (alertType, telegramChatID= '-00000000'):
   import requests, datetime, pytz

   # I am using pytz to use the function in another server maybe out of Spain
   datedate = datetime.datetime.now(pytz.timezone('Europe/Madrid')).strftime("%Y-%m-%d, %H:%M:%S")

   # Webhook link
   url = 'http://XXXX.org/webhook/XXXXXX'
   #Parameter to send with the GET call: alert type, time and Chat ID of the Telegram
   parame01 = '?Alert=' + alertType + ' - FREE - ' + '&Time=' + datedate + '&TelegramIdChat='+ telegramChatID
  
   # In case you need a proxy
   proxy_servers = {
      'http': 'http://proxyeurope.XXXXX.com:8080',
   }

   try:
      s = requests.Session()
      
      # Comment this line if you don't need the proxy 
      s.proxies = proxy_servers
      
      response = s.get(url + parame01)

   except Exception as error:
      print(f'ERROR: {error} -> Telegram message not sent.')
   else:
      print(response.text)
   #print(response.json())


#sendTelegram ('Not file found in the system')
