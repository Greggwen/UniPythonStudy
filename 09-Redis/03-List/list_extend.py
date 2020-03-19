#!/usr/bin/python3

import redis

redis_client = redis.Redis(host='localhost', port=6379)


print(redis_client.lrange('language', 0, 19))


# LINSERT key BEFORE | AFTER pivot value
# 将值 value 插入到列表 key 当中，位于值 pivot 之前或之后。
# 当 pivot 不存在于列表 key 时，不执行任何操作。
# 当 key 不存在时， key 被视为空列表，不执行任何操作。
# 如果 key 不是列表类型，返回一个错误。
redis_client.linsert('language', 'BEFORE', 'Javas', 'SQL')

print(redis_client.lrange('language', 0, 19))


# redis_client.lset('language', 2, 'Ruby')
# print(redis_client.lrange('language', 0, 19))
# redis_client.lset('language', 9, 'Perl')
# print(redis_client.lrange('language', 0, 19))

# redis_client.lpush('command', 'update system ....')
# redis_client.lpush('request', 'visit page')

# ret = redis_client.blpop(['command', 'request', 'visit'], 200)
# print(ret)

print(redis_client.exists('job'))
print(redis_client.exists('command'))

# LPOP key[key...] timeout 列表阻塞式弹出
print(redis_client.blpop(['job', 'command'], 5))


