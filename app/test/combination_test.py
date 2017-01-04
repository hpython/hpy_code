#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Administrator'
__email__ = "liuwei412552703@163.com"

from itertools import combinations, permutations

if __name__ == '__main__':

    #全排列
    for v in list(permutations(['a', 'b', 'c', 'd', 'e', 'f'], 3)):
        print(v)

    # 无序
    for v in list(combinations([1, 2, 3], 2)):
        print(v)
