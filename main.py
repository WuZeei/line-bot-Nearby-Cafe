# from app import app
# from flask import Flask
# from app.action import search_cafe
# from flask import request, abort,Flask
# from linebot import  LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import MessageEvent, TextMessage, TextSendMessage,LocationMessage,LocationSendMessage
# import json
# import configparser
# config = configparser.ConfigParser()
# config.read('config.ini')
# app = Flask(__name__)
# line_bot_api = LineBotApi(config['line_bot']['channel_access_token'])
# handler = WebhookHandler(config['line_bot']['channel_secret'])


# @app.route("/callback", methods=['POST'])
# def callback():
    
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         print(body,signature)
#         abort(400)
#     return 'OK'

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
#     print(event)

# @handler.add(MessageEvent, message=LocationMessage)
# def handle_message(event):
#     data = search_cafe.search_cafe(event.message.latitude,event.message.longitude,'咖啡廳')
#     if len(data) == 1:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='附近沒有咖啡廳'))
#     else:
#         location_message = LocationSendMessage(type=data['types'][0],title=data['name'],address=data['formatted_address'],latitude = data['geometry']['location']['lat'],longitude=data['geometry']['location']['lng'])
#         line_bot_api.reply_message(event.reply_token, location_message)
from app import app

if __name__ == '__main__':
    app.run(debug=True,port=8787)
