import pika
import uuid
import sys
import time


class FibonacciRpcClient(object):

    def __init__(self):
        credentials = pika.PlainCredentials('admin', '1q2w3e')
        parameters = pika.ConnectionParameters('192.168.1.197', 5672, '/', credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n)
        )
        count = 0
        while self.response is None:
            if (count >= 50):
                break
            self.connection.process_data_events()
            time.sleep(0.1)
            count += 1
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print('Usages: python %s [number]' % sys.argv[0])
    #response = fibonacci_rpc.call(30)
    sys.exit(1)

n = int(sys.argv[1])
print(" [x] Requesting fib(%d)" % n)
response = fibonacci_rpc.call(n)
print(" [.] Got %r" % response)