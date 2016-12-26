# -*- encoding: utf-8 -*-
__author__ = 'Administrator'
__email__ = "liuwei412552703@163.com"


import json



def json2Obj(obj):

    pass

def obj2Json(json):

    pass




if __name__ == '__main__':
    data = {"spam" : "foo", "parrot" : 42}
    print(type(data))

    s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
    print(s['name'], "*" * 8, s['type'])
    print(s.keys())