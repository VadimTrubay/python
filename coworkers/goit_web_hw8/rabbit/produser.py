import pika
import pickle

from faker import Faker
from mongoengine import *
from datetime import datetime
from random import choice

import connect

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_messages')
channel.queue_declare(queue='sms_messages')

fake = Faker('uk-UA')
NUMBER_USER = 20
CHOICE_SEND = ['sms', 'email']

class User(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone = StringField(max_length = 20)
    status = BooleanField(default = False)
    choice_sending = StringField(choices = CHOICE_SEND, default = 'email')
    
def seed_users():
    for _ in range(NUMBER_USER):
        user = User(fullname=fake.name(), 
                        email = fake.email(),
                        phone = fake.phone_number(),
                        choice_sending = choice(CHOICE_SEND)
                        ).save()
def main():
   
    for us in User.objects():
        message = {'id': us.id,
                   'message': f'Вітаю {us.fullname}',
                   'date': datetime.now().isoformat()
                   }
        if us.choice_sending == 'email':
            channel.basic_publish(exchange='', routing_key='email_messages',
                                body=pickle.dumps(message),
                                properties=pika.BasicProperties(
                                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                                ))
            print(" [x] Sent %r" % message)
        else:
            channel.basic_publish(exchange='', routing_key='sms_messages',
                                  body=pickle.dumps(message),
                                  properties=pika.BasicProperties(
                                      delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                                  ))
            print(" [x] Sent %r" % message)
    # print(" [x] Sent message")
    connection.close()
    

if __name__ == '__main__':
    if not User.objects:
        seed_users()
    main()