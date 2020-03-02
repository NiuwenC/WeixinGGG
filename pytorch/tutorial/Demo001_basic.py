# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 9:54
# @Author  : JackNiu
# @File    : Demo001_basic.py
# @Software: PyCharm

import torch
x= torch.empty(5,3)
print(x)

y=torch.rand(5,3)
print(y)

z= torch.zeros(5,3,dtype=torch.long)
print(z)

# 直接根据数据创建tensor
w= torch.tensor([5.5,3])
print(w)

a=z.new_ones(5,3,dtype=torch.double)
print(a)

b= torch.randn_like(a,dtype=torch.float)
print(b)

# Resize : reshape操作，
x= torch.randn(4,4)
y=x.view(16)
z= x.view(-1,8)
print(x,y,z)
print(x.size(),y.size(),z.size())

# If you have a one element tensor, use .item() to get the value as a Python number
x= torch.randn(1)
print(x)
print(x.item())

# 将一个torch tensor 转换为 numpy 数组

a= torch.ones(5)
print(a)
print(a.size())
b = a.numpy()
print(b)
print(b.shape)