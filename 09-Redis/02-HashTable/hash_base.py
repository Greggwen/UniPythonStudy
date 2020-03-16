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

redis_client.hsetnx('month', 'Jan', 'Jan.')
redis_client.hsetnx('month', 'July', 'July')

print(redis_client.hget('month', 'Jan'))  # output "January"
print(redis_client.hget('month', 'July')) # output "July"


# HEXISTS hash field ， 检测field是否在hash中
print(redis_client.hexists('month', 'Jan'))
print(redis_client.hexists('month', 'Oct'))

# HDEL hash field ，删除hash中的field，支持同时删除多个，并返回删除成功的个数，不存在的field会被忽略

ret = redis_client.hdel('month', 'Jan', 'July', 'Mar')

print('--------------------------------')
print(ret)
print(redis_client.hget('month', 'Jan'))
print(redis_client.hget('month', 'July'))
print(redis_client.hget('month', 'Mar'))

# HLEN key 获取field 个数
print(redis_client.hlen('month'))

# HSTRLEN hash field，返回hash中给定field的值的长度
print(redis_client.hstrlen('month', 'May'))

# HINCRBY hash field increment_value
redis_client.hincrby('counter', 'page_view', 10)

print(redis_client.hget('counter', 'page_view'))

redis_client.hincrby('counter', 'page_view', 10)

print(redis_client.hget('counter', 'page_view'))

# HINCRBYFLOAT hash field incremtn_value
redis_client.hincrbyfloat('milk', 'price', 10.0)
print(redis_client.hget('milk', 'price'))
redis_client.hincrbyfloat('milk', 'price', 0.2)
print(redis_client.hget('milk', 'price'))

