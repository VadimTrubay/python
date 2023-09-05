import pika
import pickle
import time

from produser import User

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_messages')

    def callback(ch, method, properties, body):
        message = pickle.loads(body)
        print(f" [x] Received {message}")
        time.sleep(1)
        print(f" [x] Done: {method.delivery_tag}")
        user = User.objects(id=message['id']).first()
        user.update(status = True)
        # ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='email_messages', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
