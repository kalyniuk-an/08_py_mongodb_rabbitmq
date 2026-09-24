import json

import pika

from notifications import send_email, send_sms

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="notifications")


def callback(ch, method, properties, body):
    notification = json.loads(body.decode())

    notification_type = notification["notification_type"]

    if notification_type == "email":
        send_email(notification)

    elif notification_type == "sms":
        send_sms(notification)

    else:
        print("Unknown notification type")


channel.basic_consume(
    queue="notifications",
    on_message_callback=callback,
    auto_ack=True,
)

print("Waiting for notifications...")

channel.start_consuming()
