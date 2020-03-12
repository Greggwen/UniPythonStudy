#!/usr/bin/python3

import redis


redis_client = redis.Redis(host='localhost', port=6379)


redis_client.set('welcome', 'Hello World!')
ret = redis_client.get('welcome')
print(ret)

# setrange: SETRANGE key offset value 
# 若offset偏移量在原字符串的范围内，则直接替换
redis_client.setrange('welcome', 6, 'Redis')
ret = redis_client.get('welcome')
print(ret)

# 若offset偏移量大于原字符串最大值，则与偏移量之间用零字节（“\x00”）填补
redis_client.setrange('welcome', 15, 'What are you doing?')
ret = redis_client.get('welcome')
print(ret)

# getrange：GETRANGE key start end
# 返回索引1到5的字符，包括索引为5的字符
f1t5 = redis_client.getrange('welcome', 1, 5)
print(f1t5)  # output "ello "

# 返回索引-5到-1的字符
minus = redis_client.getrange('welcome', -5, -1)
print(minus) # output "oing?"

# 不支持回绕操作，返回空
minus1 = redis_client.getrange('welcome', -1, -9)
print(minus1) # output ""

# 超过总长度的部分自动忽略
all = redis_client.getrange('welcome', 0, 1000)
print(all)


# INCR：为key存储的数字默认加 1  DECR：为key存储的数字减 1
redis_client.set('page_view', 1)
redis_client.incr('page_view')
page_view = redis_client.get('page_view')
print(page_view)

redis_client.incr('page_view')
page_view = redis_client.get('page_view')
print(page_view)

redis_client.incr('page_view')
page_view = redis_client.get('page_view')
print(page_view)

redis_client.incr('page_view')
page_view = redis_client.get('page_view')
print(page_view)

redis_client.incr('page_view', 10)
page_view = redis_client.get('page_view')
print(page_view)


redis_client.decr('page_view')
page_view = redis_client.get('page_view')
print(page_view)

redis_client.decr('page_view')
page_view = redis_client.get('page_view')
print(page_view)

# INCRBY ：为key存储的数字增加增量

redis_client.incrby('page_view', 20)
page_view = redis_client.get('page_view')
print(page_view)

redis_client.decrby('page_view', 11)
page_view = redis_client.get('page_view')
print(page_view)

# redis_client.decrby('page_view', 11.1)  # error： value is not an integer or out of range
# page_view = redis_client.get('page_view')
# print(page_view)

redis_client.set('decimal', 3.0)
decimal = redis_client.get('decimal')
print(decimal)

# 浮点数最多只保留小数点后的17位数字，
redis_client.incrbyfloat('decimal', 2.33)
decimal = redis_client.get('decimal')
print(decimal)


week_dict = {}
week_dict['Mon'] = "周一"
week_dict['Tue'] = "周二"
week_dict['Wen'] = "周三"
week_dict['Thur'] = "周四"
week_dict['Fri'] = "周五"
week_dict['Sat'] = "周六"
week_dict['Sun'] = "周日"
redis_client.mset(week_dict)
mret = redis_client.mget('Mon', 'Tue', 'Sun')
print(mret)
