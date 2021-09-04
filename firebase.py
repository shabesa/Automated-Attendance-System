import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
import json

class UpdateBase:
    
    def __init__(self):
        cred = credentials.Certificate('firebase-sdk.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        fileRead = open("settings.txt", "r", encoding="utf-8")
        settings = json.load(fileRead)
        fileRead.close()
        self.email = settings['auth']['user']
        self.password = settings['auth']['password']

    def createuser(self):
        user = auth.create_user(email = self.email, password = self.password)
        print(f"User created successfully : {user.uid}")

    def addData(self, date, name, time, verification, status):
        doc_ref = self.db.collection(date).document()
        doc_ref.set({
            u'Name': name,
            u'Time': time,
            u'Verification': verification,
            u'Status' : status
        })

    def readData(self, date):
        users_ref = self.db.collection(date)
        docs = users_ref.stream()

        for doc in docs:
            documents = doc.to_dict()
            print(documents)
        return documents

# UpdateBase().readData('date')
# UpdateBase().addData('16-07-2021', 'Kishore', '05:10:05', 1)



