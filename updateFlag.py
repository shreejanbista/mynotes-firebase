import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pprint import pprint as pp
from firebase_admin import firestore

from pyfcm import FCMNotification


def upflag():
    cred = credentials.Certificate("../my-notes.json")

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://my-notes-d3bed.firebaseio.com/',
        'projectId': 'my-notes-d3bed'
    })

    data = db.reference("storageData").get()
    count = 0

    folder_names= []
    for key, i in data.items():
        if (i.get("flag")) == "0":
            count = count + 1
            print(count)

            file_name = i.get("noteName")
            folder_names.append(file_name)

    print(folder_names)

    dbData = db.reference("storageData")
    folders = os.listdir("downloadedPDF/")
    pp(folders)

    for key in folders:
        data = {
            key + '/flag': '1'
        }

        dbData.update(data)


    dbs = firestore.client()
    docs = dbs.collection('token').stream()

    lists = []

    for doc in docs:
        doc = doc.to_dict()
        lists.append(*doc.values())

    # print(lists)
    inc = 0
    for lt in lists:
        push_service = FCMNotification(
            api_key="AAAAqZ7gPCs:APA91bE-UJ9LFH8N019ddYeicgwDSaugPgxQZpZHWGAEskT3RjeIVpKKu5w0p62PqL5GA3iNq2mZfJbl9hmUdCpZ-IZeDri3U1ZYeZ4MO6DsVRUtrwtdijmPdT6TcT10BxKXlJ8KbH1o")
        message_title = "Something New, Something Spicy"
        for smth in range(count):
            message_body = folder_names[smth] + " has been uploaded."

            result = push_service.notify_single_device(registration_id=lt, message_body=message_body,
                                                   message_title=message_title)

        inc = inc + 1
        print(inc)

upflag()



