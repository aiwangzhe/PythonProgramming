# -*- coding: UTF-8 -*-

from kafka import KafkaProducer
import json
import random

producer = KafkaProducer(
    value_serializer = lambda v:json.dumps(v).encode('utf-8'),
    bootstrap_servers = ['node5.leap.com:6667','node6.leap.com:6667','node7.leap.com:6667']
)

for i in range(100000):
    data = {
        "name":"wangdachui"+str(i),
        "age": random.randint(1, 100),
        "school":"qinghua",
        "id":i
    }
    producer.send('testmovedir',data)

producer.close()