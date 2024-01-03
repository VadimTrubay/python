import time
import connect
import pika
from datetime import datetime
import json
from faker import Faker
from models import Contact


fake_data = Faker('en_US')

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters
                                     (host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.exchange_declare(exchange='email_service', exchange_type='direct')
channel.queue_declare(queue='email_queue', durable=True)
channel.queue_bind(exchange='email_service', queue='email_queue')


def generate_fake_contact():
    for _ in range(10):
        contact = Contact(name=fake_data.name(), email=fake_data.email())
        contact.save()


def main():
    contacts = Contact.objects()
    for contact in contacts:
        message = {
            "id": str(contact.id),
            "payload": [contact.name, contact.email],
            "date": datetime.now().isoformat(),
            "text": f'Hello, {contact.name}'
            }

        channel.basic_publish(
            exchange='email_service',
            routing_key='email_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
        print("Sent %r" % message)
        time.sleep(0.2)
    connection.close()


if __name__ == '__main__':
    main()
    generate_fake_contact()
    print('database successfully to added')