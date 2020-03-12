#!/usr/bin/python3

import redis
import time

redis_client = redis.Redis(host='localhost', port=6379)

# set command
redis_client.set('first', 'first')
print(redis_client.get('first'))  # output "first"


# setnx: when key is not exists, the key will be seted to value, And when key is exists, value stay the same
redis_client.setnx('first', 'first nx')
print(redis_client.get('first'))  # output "first"

# equal to setnx
redis_client.set('first', 'first set nx', nx=True)
print(redis_client.get('first'))  # output "first"

# setex: sets thd value of key key to value and set expire time
redis_client.setex('first', 5, 'first set')
print(redis_client.get('first'))  # output "first set"，expire time is 5 seconds, the value will be replaced.

time.sleep(1)
print("after one second, the first content is ", redis_client.get('first'))  # output "None"

# Slimilar to set command，But psetex command will set expire time to milliseconds
redis_client.psetex("second", 500, "second set 500ms")
print(redis_client.get('second'))
time.sleep(1)
print(redis_client.get('second'))

# getset: sets the value of key is value, And returns the old value
redis_client.set('third', 'third set')
old_value = redis_client.getset('third', 'reset third value')

print('the key of old value is ', old_value)  # output "third set"
print('the key of new value is ', redis_client.get('third'))  # output "reset third set"

# strlen key : return the value's of key length
str_len = redis_client.strlen('third')
print(str_len) # output 17

str_len = redis_client.strlen('four')
print(str_len) # output 0


print("the value of the third key is: ", redis_client.get('third'))

# append: return the eventual value length
append_return = redis_client.append("third", "!Please retodo")

print(append_return)

print(redis_client.get('third'))

not_exists = redis_client.append("five", "the key of five not exists")
print(not_exists, redis_client.get('five'))