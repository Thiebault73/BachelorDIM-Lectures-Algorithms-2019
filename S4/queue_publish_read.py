# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:43:58 2019

@author: bebertt
"""
import argparse
import simple_queue_publish as publi
import simple_queue_read as read

parser = argparse.ArgumentParser(description="Publier ou lire un message")
parser.add_argument("-r", "--read", help="Lire un message", 
                    action="store_true")

parser.add_argument("-p", "--publi", help="Publier une message", 
                    action="store_true")

args = parser.parse_args()

if (args.read):
    read.simple_queue_read()
elif(args.publi):
    publi.simple_queue_publish()
else:
    print("Error")