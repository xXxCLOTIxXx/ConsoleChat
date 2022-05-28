from flask import Flask, render_template, url_for, request, redirect, abort, make_response, session
import json
import random
import string

def generateId(amount: int):
	code = ""
	for x in range(amount):
		code = code + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
	return code

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def root():
	return "Working..."

@app.route("/get/message", methods=["get"])
def getMess():
	with open("database.json", "r") as file:
		chat = json.load(file)
	return chat

@app.route("/post/message")
def postMess():
	name = request.args.get('name')
	message = request.args.get('message')
	messageId = request.args.get('messageId')
	for_json = {"name": name, "message": message, "messageId": generateId(16)}
	with open("database.json", "r") as file:
		chat = json.load(file)
	chat['chat'].append(for_json)
	with open("database.json", "w") as file:
		json.dump(chat,file)
	return chat