import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pprint import pprint as pp


def upflag():
    cred = credentials.Certificate("../my-notes.json")

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://my-notes-d3bed.firebaseio.com/'
    })

    dbData = db.reference("storageData")
    folders = os.listdir("downloadedPDF/")
    pp(folders)

    for key in folders:
        data = {
            key + '/flag': '1'
        }

        dbData.update(data)


upflag()
