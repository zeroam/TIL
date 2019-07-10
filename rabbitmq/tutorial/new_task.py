import sys
import pika

credentials = pika.PlainCredentials('admin', '1q2w3e')
parameters = pika.ConnectionParameters('192.168.1.197', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World"
channel.basic_publish(exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2, # make message persistent
    ))

print(' [x] Sent %r' % message)
connection.close()