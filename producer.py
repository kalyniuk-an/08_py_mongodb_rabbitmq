import json

import pika

from models_notification import Notification


connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="notifications")


notification = Notification(
    user_id="123",
    message="Hello! This is a test notification.",
    notification_type="sms",
)

message = json.dumps(notification.__dict__)

channel.basic_publish(
    exchange="",
    routing_key="notifications",
    body=message,
)

print("Notification sent")

connection.close()
