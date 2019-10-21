# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:11:22 2019

@author: bebertt
"""
import config
import os
import pika

    
def simple_queue_publish():
    amqp_url=config.amqp_url
    
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    
    channel.queue_declare(queue='presentation')
    
    
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=config.userName)
                              
    print(" [x] Sent 'Hello World!'")
        
    connection.close()
