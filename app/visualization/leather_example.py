#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Administrator'
__email__ = "liuwei412552703@163.com"

import random
import leather

import sys

#防止中文乱码编译不通过
reload(sys)
sys.setdefaultencoding('utf-8')


# 散点图
def svgpic_dots():
    dot_data = [(random.randint(0, 250), random.randint(0, 250)) for i in range(100)]

    chart = leather.Chart('Colorized dots')
    chart.add_dots(dot_data, fill_color=colorizer)
    chart.to_svg('dotschar.svg')


# 散点图示例 2
def svgpic2_dots():
    data = [(0, 3), (4, 5), (7, 9), (8, 4)]
    chart = leather.Chart('Simple pairs')
    chart.add_dots(data)
    chart.to_svg('simple_pairs.svg')


# 折线图
def svgpic_line():
    data = [(0, 3), (4, 5), (7, 9), (8, 4)]
    chart = leather.Chart('折线图')
    chart.add_line(data)
    chart.to_svg('/lines.svg')


def mixing_shapes():
    line_data = [(0, 1),(2, 5),(4, 4),(8, 3)]
    dot_data = [(1, 3),(2, 5),(6, 9),(10, 4)]

    chart = leather.Chart('Mixed shapes')
    chart.add_line(line_data, name="横轴")
    chart.add_dots(dot_data, name="纵轴")
    chart.to_svg('/mixed_shapes.svg')



def colorizer(d):
    return 'rgb(%i, %i, %i)' % (d.x, d.y, 150)


if __name__ == '__main__':
    # 生成一个图表
    # svgpic_dots()
    # svgpic2_dots()

    # svgpic_line()
    mixing_shapes()
