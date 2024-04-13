from django.shortcuts import render
import pyrebase
import random

config = {
  "apiKey": "AIzaSyAevdCt7R1IrOvjkbex3cUj16F7sJzS2Uw",
  "authDomain": "oceanenergyharvesting.firebaseapp.com",
  "databaseURL": "https://oceanenergyharvesting-default-rtdb.firebaseio.com",
  "projectId": "oceanenergyharvesting",
  "storageBucket": "oceanenergyharvesting.appspot.com",
  "messagingSenderId": "920849633915",
  "appId": "1:920849633915:web:eb0120021c6fbf1bdc48de",
  "measurementId": "G-23MK7XS1W0"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def home(request):
    current = database.child('current').get().val()
    voltage = database.child('voltage').get().val()
    # current = round(random.random() - 0.9, 3)
    # voltage = round(random.random() - 0.9, 3) 
    wattage = round(current*voltage, 3)
    
    return render(request,"app/index.html",{"current":current,"voltage":voltage, "wattage": wattage})
