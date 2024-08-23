import sys

args = sys.argv[1:]
print(args)


result = 0
for i in args:
    #result += int(i)
    result = result + int(i)
print(result)