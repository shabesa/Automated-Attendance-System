import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)

fileRead = open("settings.txt", "r", encoding="utf-8")
settings = json.load(fileRead)
fileRead.close()
email = settings['auth']['user']
password = settings['auth']['password']

def createuser(email, password):
    user = auth.create_user(email = email, password = password)

    print(f"User created successfully : {user.uid}")

#createuser(email, password)

user = auth.get_user_by_email(email)

print(f"User id is: {user.uid}")