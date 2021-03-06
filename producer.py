# reference: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
import pika

conneciton = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'hello')
channel.basic_publish(exchange = '', routing_key = 'hello', body = 'Hello World!')

print(" [x] Sent message: 'Hello World!'")
connection.close()
