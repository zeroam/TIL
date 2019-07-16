import pika

credentials = pika.PlainCredentials('admin', '1q2w3e')
parameters = pika.ConnectionParameters('192.168.1.197', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    if n > 35:
        response = -1 
    else:
        response = fib(n)

    ch.basic_publish(exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id= \
            props.correlation_id),
        body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(" [.] publish fib(%d)" % n)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()