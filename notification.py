
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAqZ7gPCs:APA91bE-UJ9LFH8N019ddYeicgwDSaugPgxQZpZHWGAEskT3RjeIVpKKu5w0p62PqL5GA3iNq2mZfJbl9hmUdCpZ-IZeDri3U1ZYeZ4MO6DsVRUtrwtdijmPdT6TcT10BxKXlJ8KbH1o")
registration_id = "fGpUU96lMeo:APA91bHp4J4SGUnpZzFveEABNXHMrbLuXiVh7PIqJpo62WcWE66eOm0SCDO0u--TRhQbHA6Zv0q7JtcU7W0-DdOeSk6bozKuzK6gGri5A76mtp79Ay43jOLSUyl3Qx-XnS-uPat1Zq_-"
message_title = "File Uploded"
message_body = "A new file has been upload. Do check it out."
result = push_service.notify_single_device(registration_id=registration_id, message_body=message_body,
                                           message_title=message_title)

