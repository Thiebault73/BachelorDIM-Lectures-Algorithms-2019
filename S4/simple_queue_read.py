# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:27:39 2019

@author: bebertt
"""
import config
import os
import pika
amqp_url = config.amqp_url
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(queue='hello',
                      on_message_callback=callback,                          
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
