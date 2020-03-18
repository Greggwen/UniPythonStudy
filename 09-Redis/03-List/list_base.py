#!/usr/bin/python3

import redis

redis_client = redis.Redis(host='localhost', port=6379)


# LPUSH key value [value]  将一个或多个值插入到列表key的表头
# LPUSHX key value  将值 value 插入到列表 key 的表头，当且仅当 key 存在并且是一个列表。

print("================ LPUSH & LPUSHX =================")
# redis_client.lpush('language', 'Python')
# redis_client.lpush('language', 'Golang')
# redis_client.lpush('language', 'Java')

# print(redis_client.lrange('language', 0, 2))

# redis_client.lpush('language', 'PHP', 'Jaavscript', 'Lua')

print(redis_client.lrange('language', 0, 19))
print(redis_client.llen('language'))

# redis_client.lpushx('language', 'Swift')
print(redis_client.lrange('language', 0, 19))


# redis_client.lpushx('fruit', 'Apple')
print(redis_client.lrange('fruit', 0, 2))

print("================ RPUSH & RPUSHX =================")

# redis_client.rpush('language', 'Kotlin')
# redis_client.rpushx('language', 'Groovy')
print(redis_client.lrange('language', 0, 19))

redis_client.rpushx('fruit', 'Banana')
print(redis_client.lrange('fruit', 0, 2))


print("================ LPOP & RPOP & RPOPLPUSH =================")

# lfirst = redis_client.lpop('language')
# print(lfirst)

# remain_value = redis_client.lrange('language', 0, 19)
# print(remain_value)

# rfirst = redis_client.rpop('language')
# print(rfirst)

# remain_value = redis_client.lrange('language', 0, 19)
# print(remain_value)

# RPOPLPUSH source destination 将列表source最后一个元素弹出，插入到destination列表的表头
remain_value = redis_client.lrange('language', 0, -1) # 查看列表所有元素
print(remain_value)

# ret = redis_client.rpoplpush('language', 'single')
# print(ret)

print(redis_client.lrange('single', 0, -1))


# RPOPLPUSH  source与destination若是同一个列表，则表示，将表尾的元素移动到表头，可以视做列表的旋转操作
# ret = redis_client.rpoplpush('language', 'language')
# print(ret)
remain_value = redis_client.lrange('language', 0, -1)
print(remain_value)


print("================ llen & lindex & lrem =================================")
print(redis_client.llen('language'))  # 获取列表的长度
print(redis_client.lindex('language', 3)) # 获取列表下标为3的元素

# redis_client.lpush('language', 'PHP')
# redis_client.rpush('language', 'PHP')
print(redis_client.lrange('language', 0, -1))

# LREM key count value  从表头开始向表尾搜索，删除value是 PHP 的两个元素。
# 若count > 0 表示从表头向表尾搜索，并删除count个value的值
# 若count < 0 表示从表尾向表头搜索，并删除count个value的值
# 若count = 0 表示移除列表中所有value的值
redis_client.lrem('language', 2, 'PHP')  