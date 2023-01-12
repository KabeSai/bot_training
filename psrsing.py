#!/usr/bin/env python3
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.users import GetFullUserRequest
import configparser
import os, sys
import csv
import traceback
import time
import random
import json
import asyncio

cpass = configparser.RawConfigParser()
cpass.read('config.data')
#
with open(f'{cpass["cred"][f"phone"]}.json') as f:
    templates = json.load(f)
try:
    session_file = templates['session_file']
    phone = templates['phone']
    register_time = templates['register_time']
    app_id = templates['app_id']
    app_hash = templates['app_hash']
    sdk = templates['sdk']
    app_version = templates['app_version']
    device = templates['device']
    last_check_time = templates['last_check_time']
    first_name = templates['first_name']
    last_name = templates['last_name']
    system_lang_pack = templates['system_lang_pack']
    lang_code = templates['lang_code']
    proxy = templates['proxy']
    ipv6 = templates['ipv6']
    username = templates['username']
    avatar = templates['avatar']
    print(templates['phone'])
    print(templates['app_id'])
    print(templates['session_file'])
    client = TelegramClient(phone, app_id, app_hash)
except KeyError:
    os.system('clear')
    print("[!] run python3 setup.py first !!")
    sys.exit(1)
#
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    try:
        client.sign_in(phone, input('[+] Enter the code: '))
    except:
        client.sign_in(password='Endmolninos2005')

os.system('clear')
#
# chats = []
# last_date = None
# chunk_size = 200
# groups=[]
# #

# result = client(GetDialogsRequest(
#                 offset_date=last_date,
#                 offset_id=0,
#                 offset_peer=InputPeerEmpty(),
#                 limit=chunk_size,
#                 hash = 0
#             ))
# chats.extend(result.chats)
# #
# for chat in chats:
#     try:
#         groups.append(chat)
#     except:
#         continue
# #
# i=0
# for group in groups:
#     print(f"[{str(i)}] - ", group.title)
#     i+=1
# #
# print('[+] Choose a group to add members')
# g_index = input("[+] Enter a Number : ")
# target_group=groups[int(g_index)]
# #
# target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
#
full = await client(GetFullUserRequest('username'))
bio = full.full_user.about