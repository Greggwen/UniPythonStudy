#!/usr/bin/python3

import redis

redis_client = redis.Redis(host='localhost', port=6379)


# HSET hash field value
redis_client.hset('month', 'Jan', 'January')
redis_client.hset('month', 'Feb', 'February')
redis_client.hset('month', 'Mar', 'March')
redis_client.hset('month', 'Apr', 'April')
redis_client.hset('month', 'May', 'May')

# HGET hash field
print(redis_client.hget('month', 'Jan'))
print(redis_client.hget('month', 'July'))

# 获取hash的所有field
print(redis_client.hkeys('month'))

# 获取hash的所有value
print(redis_client.hvals('month'))

# 获取hash的所有field和value
print(redis_client.hgetall('month'))


# HSETNX hash field value， 当field 不存在hash表时，将它设置为value