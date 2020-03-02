# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 14:01
# @Author  : JackNiu
# @File    : Demo004_gutograde_analysis.py
# @Software: PyCharm

import torch

'''
如果想进行求导运算，在Variable上调用.backward()

'''
# x=torch.ones(2,2,requires_grad=True)
# y=x+2
#
# z= y*y*3
# out = z.mean()
#
# out.backward()
# print(x,y,z)
# print(x.grad) # 输出out对x的求导结果
# print(y.grad)# y不是自动求导变量


'''
如果有更多的元素，需要制定一个和tensor的形状匹配的grad_output （y在指定方向投影对x的导数）
'''

x= torch.randn(3,requires_grad=True)
y=x*2
while y.data.norm() <1000:
    y= y*2
    print(y)


v = torch.tensor([0.1,1.0,0.001], dtype=torch.float)
y.backward(v)
print(x.grad)

