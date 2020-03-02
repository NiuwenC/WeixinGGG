# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 10:30
# @Author  : JackNiu
# @File    : Demo003_autograd.py
# @Software: PyCharm

import torch
x= torch.ones(2,2,requires_grad=True)
print(x)

a=torch.randn(2,2)
a=((a*3)/(a-1))

print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b = (a*a).sum()
print(b.grad_fn)


w = torch.randn(3, requires_grad=True)
y=w*2
print(y.data)
# norm 就是求p维范数
while y.data.norm()<1000:
    y=y*2
    print(y,y.data.norm())


print(y)

print(x.requires_grad)
print((x**2).requires_grad)
y=x.detach()
print(y.requires_grad)
print(x.eq(y).all())
with torch.no_grad():
    print((x**2).requires_grad)