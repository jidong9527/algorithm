# -*- coding:utf-8 -*-
# (c) 2018, Ji Dongdong <jidongdong@cnnic.cn>
#
# 模块用于冒泡排序.
"""冒泡排序算法的运作如下：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

时间复杂度：O(n*n)
"""


def bubble(data_list):
    for i in range(len(data_list)-1):
        for j in range(len(data_list)-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list


if __name__ == '__main__':
    data = [22, 1, 4, 3, 99, 34, 567, 21, 44, 10]
    result = bubble(data)
    print(result)