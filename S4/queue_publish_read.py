# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:43:58 2019

@author: bebertt
"""
import config
import argparse
import os
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)



amqp_url=config.amqp_url


# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
                          
print(" [x] Sent 'Hello World!'")
    
connection.close()
