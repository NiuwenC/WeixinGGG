# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 16:21
# @Author  : JackNiu
# @File    : Demo005_neural_networks.py
# @Software: PyCharm

'''
 feed-forward : 前馈神经网络
'''
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        #1个输入图像通道，6个输出通道，3*3的卷积立方体
        self.conv1= nn.Conv2d(1,6,3)
        self.conv2= nn.Conv2d(6,16,3)

        self.fc1 = nn.Linear(16*6*6,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)

    def forward(self, x):
        # Max polling over a(2,2) window
        x = F.max_pool2d(F.relu(self.conv1(x),(2,2)))
        #
        x = F.max_pool2d(F.relu(self.conv2(x)),2)
        x = x.view(-1,self.num_flat_features(x))
        x= F.relu(self.fc1(x))
        x= F.relu(self.fc2(x))
        x=self.fc3(x)
        return x

    def num_flat_features(self,x):
        size= x.size()[1:]
        num_features=1
        for s in size:
            num_features *=s
        return num_features

net = Net()
print(net)

params = list(net.parameters())
print(len(params))
print(params[0].size())
