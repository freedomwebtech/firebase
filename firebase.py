import pyrebase
from distance import distance


config = {
    "apiKey": "AIzaSyCZE61YtZWt_lMaZiOq6ANFvLCyrNWYVEQ",
    "authDomain": "sanket-e9152.firebaseapp.com",
    "databaseURL": "https://sanket-e9152-default-rtdb.firebaseio.com",
    "projectId": "sanket-e9152",
    "storageBucket": "sanket-e9152.appspot.com",
    "messagingSenderId": "47809698488",
    "appId": "1:47809698488:web:753c4c7fe364de610e324d"
    

};


firebase = pyrebase.initialize_app(config)



storage = firebase.storage()
database = firebase.database()
a = distance()
print (a)
database.child("DB object name")
data = {"key1": a}
database.set(data)
