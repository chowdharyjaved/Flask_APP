from flask import Flask
import pickle

app=Flask(__name__)

with open('abc', 'rb') as f:

    model=pickle.load(f)