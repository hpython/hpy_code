#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Administrator'
__email__ = "liuwei412552703@163.com"

# 首先载入pandas
import pandas as pd

# 我们将载入seaborn,但是因为载入时会有警告出现，因此先载入warnings，忽略警告
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt


sns.set(style="white", color_codes=True)

# 载入数据
iris = pd.read_csv("./data/users.csv") # 数据现在为 DataFrame格式

# 用head函数看一下数据结构啥样
iris.head()


# 让我们用counts功能看下一共有多少种花
count = iris["Species"].value_counts()
print("合计:", count)


# 使用 .plot 做散点图
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")#数据为萼片的长和宽 结果如下


# 开始使用seaborn了它能同时显示直方图噢
sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)


# 我们还可以用seaborn's FacetGrid 标记不同的种类噢
#hue英文是色彩的意思
#注意这里的plt哦
sns.FacetGrid(iris, hue="Species", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()


#  Seaborn中的boxplot，可以画箱线图，可以看出不同种类的分布情况
sns.boxplot(x="Species", y="PetalLengthCm", data=iris)



# 利用striplot可以锦上添花，加上散点图
#
# 使振动值jitter=True 使各个散点分开，要不然会是一条直线
#
# 注意这里将坐标图用ax来保存了哦，这样第二次才会在原来的基础上加点
ax = sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
ax = sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="gray")


# 这图可以变现出密度的分布
sns.violinplot(x="Species", y="PetalLengthCm", data=iris, size=6)


# 通过这个曲线图可以看出不同特征值时的分布密度
sns.FacetGrid(iris, hue="Species", size=6).map(sns.kdeplot, "PetalLengthCm").add_legend()


# 修改参数dige_kind
sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3, diag_kind="kde")


if __name__ == '__main__':
    print("running......")