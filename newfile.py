SleepTime = 0.1
FileName = "a.json"


import os


try:
	import multiprocessing
except ModuleNotFoundError:
	os.system("pip install multiprocessing")

try:
	import hashlib
except ModuleNotFoundError:
	os.system("pip install hashlib")

try:
	import json
except ModuleNotFoundError:
	os.system("pip install json")

try:
	import aminofix
except ModuleNotFoundError:
	os.system("pip install Amino.fix")

try:
	import colorama
except ModuleNotFoundError:
	os.system("pip install colorama")

try:
	import hmac
except ModuleNotFoundError:
	os.system("pip install hmac")

try:
	import pyfiglet
except ModuleNotFoundError:
	os.system("pip install pyfiglet")


import requests
import time


from colorama import *
from pyfiglet import *


from multiprocessing import Process
from os import path
from hashlib import sha1


os.system("clear")


print(Fore.GREEN)
print("𝔴𝔞𝔡𝔢 𝔟𝔶 𝔪𝔥𝔞𝔱")
print("𝔞 𝔰𝔠𝔯𝔦𝔭𝔱 𝔣𝔬𝔯 𝔰𝔭𝔞𝔪𝔴𝔞𝔱𝔠𝔥𝔦𝔫𝔤 𝔩𝔦𝔳𝔢𝔳𝔦𝔡𝔢𝔬𝔰")
print("")
print(Fore.RED + Style.BRIGHT)
print(pyfiglet.figlet_format("Spam", font="sblood"))
print(Fore.GREEN + Style.BRIGHT)
print("")
print("𝔧𝔬𝔦𝔫 𝔪𝔶 𝔱𝔢𝔩𝔢𝔤𝔯𝔞𝔪 𝔣𝔬𝔯 𝔪𝔬𝔯𝔢 𝔰𝔠𝔯𝔦𝔭𝔱𝔰")
print("[ https://t.me/mhat0 ]")
print(Fore.RED)


print("\n𝔤𝔯𝔬𝔲𝔭 𝔩𝔦𝔫𝔨")
GroupLink = input ("》")
print("_"*31)


data = open(FileName)
accounts = json.load(data)


identifier = os.urandom(20)
x= ("52" + identifier.hex() + hmac.new(bytes.fromhex("ae49550458d8e7c51d566916b04888bfb8b3ca7d"), b"\x52" + identifier, sha1).hexdigest()).upper()
dev = x
client=aminofix.Client(dev)


path = client.get_from_code(GroupLink)
comId = path.comId
chatId = path.objectId


def run():
	identifier = os.urandom(20)
	x= ("52" + identifier.hex() + hmac.new(bytes.fromhex("ae49550458d8e7c51d566916b04888bfb8b3ca7d"), b"\x52" + identifier, sha1).hexdigest()).upper()
	dev = x
	client=aminofix.Client(dev)
	
	try:
		client.login(email,password)
		subclient=aminofix.SubClient(comId=comId,profile=client.profile)
		for y in range(2):
			client.join_video_chat_as_viewer(comId=comId, chatId=chatId)
		print(f"\n𝔡𝔬𝔫𝔢 ✅ ")
	except Exception as E:
		print(E)
		pass


for account in accounts:
	email = account["email"]
	password = account["password"]
	deviceId = account["device"]
	
	F = []
	spam = Process(target=run)
	time.sleep(SleepTime)
	spam.start()
	F.append(spam)


for mhat in F:
	mhat.join()