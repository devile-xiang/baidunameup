
#encoding:utf-8






import random
from urllib import parse



def getkey(txtname):
    a=open(txtname)


    array=a.readlines()

    newarray=[]
    for i in array:

        # print(i.strip())
        newarray.append(i.strip('\n'))

    # print(newarray)
    # print(len(newarray))

    number=random.randint(0,len(newarray)-1)
    # print(number)
    keyname=newarray[number]
    # print(keyname)


    stringname=keyname.encode()

    urlkeyname=parse.quote(stringname)
    # print(urlkeyname)
    #返回随机关键词
    return urlkeyname


