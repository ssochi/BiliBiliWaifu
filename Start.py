# -*- coding: utf-8 -*-
import asyncio
from multiprocessing.reduction import duplicate
from os import dup
import random

import blivedm
import socket
import threading
import time
import sys
import _thread
import json
from AI import AIClient
# 直播间ID的取值看直播间URL
# TEST_ROOM_IDS = [
#     '3253817','23918197','1023','5050','5050','23956617'
# ]
TEST_ROOM_IDS = [
    # '3253817','24900566','25757456'
    '25757456'
]

TEXT = '''
你现在是一个喝醉酒的醉汉,只会说胡话
'''

global conn
global msgList
msgList = []


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')
 
    while 1:
        global conn
        connection, addr = s.accept()
        conn = connection


async def main():

    await run_single_client()
    await run_multi_client()
    
def gpt():
    aiClient = AIClient()
    aiClient.InputMessage(TEXT)    

    while 1:
        global msgList
        if len(msgList) > 0:
            aiClient.InputMessage(msgList[0])    
            del msgList[0]
        if len(msgList) > 30:
            del msgList[:15]

async def run_single_client():
    """
    演示监听一个直播间
    """
    room_id = random.choice(TEST_ROOM_IDS)
    # 如果SSL验证失败就把ssl设为False，B站真的有过忘续证书的情况
    client = blivedm.BLiveClient(room_id, ssl=True)
    handler = MyHandler()
    client.add_handler(handler)

    

    # try:
    #     # 演示5秒后停止
    #     await asyncio.sleep(5)
    #     client.stop()

    #     await client.join()
    # finally:
    #     await client.stop_and_close()


async def run_multi_client():
    """
    演示同时监听多个直播间
    """
    clients = [blivedm.BLiveClient(room_id) for room_id in TEST_ROOM_IDS]
    handler = MyHandler()
    for client in clients:
        client.add_handler(handler)
        client.start()

    try:
        await asyncio.gather(*(
            client.join() for client in clients
        ))
    finally:
        await asyncio.gather(*(
            client.stop_and_close() for client in clients
        ))
class MyHandler(blivedm.BaseHandler):
    # # 演示如何添加自定义回调
    # _CMD_CALLBACK_DICT = blivedm.BaseHandler._CMD_CALLBACK_DICT.copy()
    #
    # # 入场消息回调
    # async def __interact_word_callback(self, client: blivedm.BLiveClient, command: dict):
    #     print(f"[{client.room_id}] INTERACT_WORD: self_type={type(self).__name__}, room_id={client.room_id},"
    #           f" uname={command['data']['uname']}")
    # _CMD_CALLBACK_DICT['INTERACT_WORD'] = __interact_word_callback  # noqa

    global duplicater
    duplicater = {}

    

    async def _on_heartbeat(self, client: blivedm.BLiveClient, message: blivedm.HeartbeatMessage):
        print(f'[{client.room_id}] 当前人气值：{message.popularity}')
        pass
        

    async def _on_danmaku(self, client: blivedm.BLiveClient, message: blivedm.DanmakuMessage):

        data = {
            "type":"message",
            "username":message.uname,
            "value":message.msg,
            "timestamp":str(message.timestamp),
        }
        data = json.dumps(data)

        global duplicater
        if data in duplicater:
            return
        duplicater[data] = ""
        # global conn
        # conn.send(data.encode('utf8'))
        if len(message.msg) <= 2 or message.msg.endswith('b') or message.msg.isdigit() or '红包' in message.msg:
            return
        global msgList
        msgList.append(f'{message.uname}说：{message.msg}')
        print(f'[{client.room_id}] {message.uname}：{message.msg}')


    async def _on_gift(self, client: blivedm.BLiveClient, message: blivedm.GiftMessage):
        data = {
            "type":"gift",
            "username":message.uname,
            "value":message.gift_name,
            "timestamp":str(message.timestamp)
        }
        data = json.dumps(data)

        global duplicater
        if data in duplicater:
            return
        duplicater[data] = ""
        # global conn
        # conn.send(data.encode('utf8'))
        if message.total_coin > 10000:
            msgList.append(f'{message.uname}赠送了{message.num}个{message.gift_name},好好感谢他吧')
        print(f'[{client.room_id}] {message.uname} 赠送{message.gift_name}x{message.num}'
              f' （{message.coin_type}瓜子x{message.total_coin}）')
     

    async def _on_buy_guard(self, client: blivedm.BLiveClient, message: blivedm.GuardBuyMessage):
        print(f'[{client.room_id}] {message.username} 购买{message.gift_name}')

    async def _on_super_chat(self, client: blivedm.BLiveClient, message: blivedm.SuperChatMessage):
        print(f'[{client.room_id}] 醒目留言 ¥{message.price} {message.uname}：{message.message}')


    async def  _on_super_red_packet_callback(self, client: blivedm.BLiveClient, message: blivedm.redPacketMessage):
        data = {
            "type":"packet",
            "username":message.username,
            "value":message.price,
            "timestamp":str(message.timestamp)
        }
        data = json.dumps(data)

        global duplicater
        if data in duplicater:
            return
        duplicater[data] = ""

        msgList.append(f'{message.username}送了一个红包,感谢他,并让直播间的观众们一起抢红包')
        print(f'[{client.room_id}] 红包,价格: ¥{message.price} 用户名:{message.username}') 
    
    async def  _on_click_like_callback(self, client: blivedm.BLiveClient, message: blivedm.likeClickMessage):
        data = {
            "type":"click",
            "username":message.username,
        }
        data = json.dumps(data)
        global msgList
        msgList.append(f'{message.username}给主播点了一个赞,感谢他,鼓励大家多多点赞哦')
        print(f'[{client.room_id}] {message.username} 给主播点赞了!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')  



if __name__ == '__main__':
    _thread.start_new_thread(socket_service,())
    _thread.start_new_thread(gpt,())
    asyncio.get_event_loop().run_until_complete(main())




