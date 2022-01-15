import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='task_queue_1', durable=True)
message = ' '.join(sys.argv[1:]) or b"Hello world"

channel.basic_publish(exchange='', body=message, routing_key='task_queue_1', properties=pika.BasicProperties(
    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
))

print(f"[{message=}] send")
connection.close()
