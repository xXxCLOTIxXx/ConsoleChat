import requests, time
from threading import Thread
import random
import string
url = 'http://127.0.0.1:5000'



before = {"chat": [{"name": "none", "message": "none", "messageId": "none"}]}
messageReq = ''
name=input("Ник>> ")
def get_message(num):
	while True:
		global before
		global messageReq
		time.sleep(num)
		return_ = requests.get(f'{url}/get/message').json()
		if return_ == before:
			pass
		else:
			IDold = []
			IDnew = []
			try:
				len1 = len(return_['chat'])
				len2 = len(before['chat'])
				for i in range(len1):
					IDnew.append(return_['chat'][i]['messageId'])
				for i in range(len2):
					IDold.append(return_['chat'][i]['messageId'])
				newID = list(set(IDnew).difference(IDold))


				for i in range(len(return_['chat'])):
					try:
						if return_['chat'][i]['messageId'] in newID:
							message = return_['chat'][i]['message']
							name = return_['chat'][i]['name']
							if messageReq == message:
								pass
							else:
								print("\n\n",name, ": ", message,"\n\n")
					except:
						pass
			except:
				pass
			before = return_

def send_message(name):
	while True:
		global messageReq
		messageReq=input('')
		requests.get(f'{url}/post/message?name={name}&message={messageReq}').json()
		print("\n")

Thread(target=get_message, args=(0.5,)).start()

Thread(target=send_message, args=(name,)).start()

