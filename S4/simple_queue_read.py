# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:27:39 2019

@author: bebertt
"""
import config
import os
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("Nombre de message : ")
    print(method.delivery_tag)
    
def simple_queue_read():
    
    amqp_url = config.amqp_url

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    
    channel.basic_consume(queue='presentation',
                         on_message_callback=callback,                          
                         auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
