import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import errno
import requests

from pprint import pprint as pp

cred = credentials.Certificate("../my-notes.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://my-notes-d3bed.firebaseio.com/'
})

# ref = db.reference("storageData")
data = db.reference("storageData").get()

for key , i in data.items():

    pp(key)
    pp(i.get("flag"))
    file_name = i.get("noteName")

    if (i.get("flag")) == "0":
        try:
            os.makedirs("downloadedPDF/" + key)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

        a = i.get("url")
        file = requests.get(a)

        with open("downloadedPDF/" + key + "/" +file_name , "wb") as pdf:
            for chunk in file.iter_content(chunk_size=1024):

                # writing one chunk at a time to pdf file
                if chunk:
                    pdf.write(chunk)

# import updateFlag
#
# updateFlag.upflag()