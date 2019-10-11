v = eval(input("Please input a number:"))

print(type(v))

str = "Hello Wrold"

if v == 0:
    print(str)
elif v > 0:
    strlen = len(str)
    startIndex = 0
    while startIndex < strlen:
        endIndex = startIndex + 2
        print(str[startIndex:endIndex])
        startIndex = startIndex + 2
else:
    strlen = len(str)
    i = 0
    while i <= strlen:
        print(str[i:(i+1)])
        i += 1
