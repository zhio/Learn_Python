#生成激活码
import random
import string

def GenKey(length):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])

def SaveKey(content):
    f = open('Result Key.txt','a')
    f.write(content)
    f.write('\n')
    f.close

if __name__ == '__main__':
    for i in range(20):
        value = GenKey(20)
        print(value)
        SaveKey(value)