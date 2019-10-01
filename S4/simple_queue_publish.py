# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:11:22 2019

@author: bebertt
"""
import config
import os
import pika

mode='_SEND'

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
amqp_url=config.amqp_url

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='presentation')


if mode == '_SEND':
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=config.userName)
                          
    print(" [x] Sent 'Hello World!'")
    
    connection.close()
else:
        
    channel.basic_consume(queue='presentation',
                          on_message_callback=callback,                          
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
