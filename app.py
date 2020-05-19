from flask import Flask, render_template, request
from googlesearch import search
import requests
import bs4
from bs4 import BeautifulSoup
from chatbot import *
import pickle
from listoperations import *
from mapping import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText =userText.lower()
    try:
        return str(mapping(userText))
    except Exception as e:
        return "I am having trouble understanding. Please refine your query ! <br> "+str(e)
if __name__ == "__main__":
    app.run()
