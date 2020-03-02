# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 10:20
# @Author  : JackNiu
# @File    : Demo002_basic_convert.py
# @Software: PyCharm
import numpy as np
import torch

a= torch.ones(5)
print(a)
print(a.size())
b = a.numpy()
print(b)
print(b.shape)

c= np.ones(5)
d = torch.from_numpy(c)
np.add(c,1,out=c)
print(c)
print(d)


print(torch.cuda.is_available())