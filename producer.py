import pika
from faker import Faker

import connect
from models import Contact


fake = Faker()


connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="email_queue")
channel.queue_declare(queue="sms_queue")


for _ in range(10):
    method = fake.random_element(["email", "sms"])

    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
        phone=fake.phone_number(),
        preferred_method=method,
    )

    contact.save()

    queue = "email_queue" if method == "email" else "sms_queue"

    channel.basic_publish(
        exchange="",
        routing_key=queue,
        body=str(contact.id),
    )

    print(
        f"Contact created: {contact.fullname} | "
        f"{method} | {contact.phone}"
    )

    print(f"Message sent to {queue}: {contact.id}")


connection.close()

print("Producer finished")
