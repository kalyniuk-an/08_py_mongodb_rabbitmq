import pika

import connect
from models import Contact


connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="email_queue")


def send_email(contact):
    print(
        f"Email sent to {contact.fullname} "
        f"({contact.email})"
    )


def callback(ch, method, properties, body):
    contact_id = body.decode()

    contact = Contact.objects(id=contact_id).first()

    if not contact:
        print(f"Contact not found: {contact_id}")
        return

    send_email(contact)

    contact.sent = True
    contact.save()

    print(f"Contact {contact.id} marked as sent")


channel.basic_consume(
    queue="email_queue",
    on_message_callback=callback,
    auto_ack=True,
)

print("Waiting for email messages...")

channel.start_consuming()