from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,LocationMessage,LocationSendMessage
from app import app
from app.action import search_shop,globals
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config['line_bot']['channel_access_token'])
handler = WebhookHandler(config['line_bot']['channel_secret'])

@app.route("/callback", methods=['POST'])
def callback():
    
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入你想尋找的店'))
    globals.initialize()
    globals.search_place = event.message.text
    print( globals.search_place)
    return  globals.search_place
    

@handler.add(MessageEvent, message=LocationMessage)
def handle_message(event):
    if  globals.search_place!='':
    # data = search_cafe.search_cafe(event.message.latitude,event.message.longitude,'咖啡廳')
        print(event.message.latitude,event.message.longitude)
        store_inf = search_shop.search_place(event.message.latitude,event.message.longitude, globals.search_place)
        if store_inf == []:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='查無此店家'))
        else:
            print(store_inf)
            # location_message = LocationSendMessage(type=data['types'][0],title=data['name'],address=data['formatted_address'],latitude = data['geometry']['location']['lat'],longitude=data['geometry']['location']['lng'])
            location_message = LocationSendMessage(type=globals.search_place,title=store_inf['shop_name'],address=store_inf['shop_address'],latitude = store_inf['latitude'],longitude=store_inf['longitude'])
            line_bot_api.reply_message(event.reply_token, location_message)
            globals.initialize()
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請先輸入你想找的店家'))