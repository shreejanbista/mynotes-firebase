import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from pyfcm import FCMNotification
# Use the application default credentials
cred = credentials.Certificate("../my-notes.json")
firebase_admin.initialize_app(cred, {
  'projectId': 'my-notes-d3bed'
})

db = firestore.client()
docs = db.collection('token').stream()

lists = []

for doc in docs:

    doc = doc.to_dict()
    lists.append(*doc.values())

# print(lists)

for lt in lists :

    push_service = FCMNotification(api_key="AAAAqZ7gPCs:APA91bE-UJ9LFH8N019ddYeicgwDSaugPgxQZpZHWGAEskT3RjeIVpKKu5w0p62PqL5GA3iNq2mZfJbl9hmUdCpZ-IZeDri3U1ZYeZ4MO6DsVRUtrwtdijmPdT6TcT10BxKXlJ8KbH1o")
    message_title = "File Uploded"
    message_body = "A new file has been upload. Do check it out."
    result = push_service.notify_single_device(registration_id=lt, message_body=message_body,
                                               message_title=message_title)
    print(lt)
    print("")

