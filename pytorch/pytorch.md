## Pytorch教程
### Getting Started
基本操作: 和Tensorflow不同的地方

    import torch
    x= torch.empty(5,3)
    print(x)
    这里能直接输出由pytorch构建的数据，和tensorflow不同，tf需要启动一个session进而去使用
    

<h1>Tensor 和 numpy的转换</h1>

    a= torch.ones(5)
    print(a)
    print(a.size())
    b = a.numpy()
    print(b)
    print(b.shape)
    
   
<h1>AUTOGRAD</h1>
pytorch中神经网络包中最核心的是AUTOGRAD包，autograd包为所有在tensor上的运算提供了自动求导的支持，
这是一个逐步运行的框架，也就意味着后向传播过程是按照你的代码定义的，并且单个循环可以不同

    如果想跟踪训练，则使用 .requires_grads=True
    .backward() 自动计算梯度，.grad属性中获取
    .detch() 停止tensor的历史记录
    为了防止追踪历史（并且使用内存），你也可以将代码块包含在with torch.no_grad():中。这对于评估模型时是很有用的，因为模型也许拥有可训练的参数使用了requires_grad=True,但是这种情况下我们不需要梯度。
    
    Function
    Tensor和Function是相互关联的并一起组成非循环图，编码了所有计算的历史，
    每个tensor拥有一个属性.grad_fn,该属性引用创建tensor的Function
    如果使用户自己创建的，就是None
    
    计算导数，在一个Tensor上调用.backward() 
    
如下：

    tensor([[1., 1.],
        [1., 1.]], requires_grad=True)
    y=x+2
    y
    tensor([[3., 3.],
        [3., 3.]], grad_fn=<AddBackward0>)
    
    
<h1>Gradients</h1>
标量: out.backward() is equivalent to out.backward(torch.tensor(1.)).

