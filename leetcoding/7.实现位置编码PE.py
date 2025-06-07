# 第一步 实现位置编码
# 这种设计让模型可以学习到不同位置之间的相对关系。

import torch
import torch.nn as nn
import torch.nn.functional as F
import math


# 继承自 PyTorch 的 nn.Module 类
# d_model :每个词嵌入的维度（通常设为 512 或其他固定值）。
# max_seq_len:是一个句子的最大长度（最多包含多少个词）
class PositionalEncoder(nn.Module):
    def __init__(self, d_model, max_seq_len=80):
        super().__init__()  # 调用父类（即 nn.Module）的构造函数，以确保 PyTorch 能正确管理模型参数。
        self.d_model = d_model  # 保存 d_model 为类的一个属性，方便后面使用。

        # 根据 pos 和 i 创建一个常量的 PE 矩阵
        pe = torch.zeros(max_seq_len, d_model)
        # 填充 pe 矩阵
        # pos 是词的位置（第几个词）
        # i 是维度索引
        for pos in range(max_seq_len):
            for i in range(0, d_model, 2):
                pe[pos, i] = math.sin(pos/(1000**((2*i)/d_model)))
                pe[pos, i+1] = math.cos(pos/(1000**((2*i)/d_model)))

        pe = pe.unsqueeze(0) # 增加一个 batch 维度，变成 [1, max_seq_len, d_model]，以便后续可以直接加到输入上。
        self.register_buffer('pe',pe) # 把 pe 注册为模型的一部分，这样它不会被当作可训练参数，但会随模型一起保存和加载（如 .pt 文件）。

        def forward(self, x):
            # 使得单词嵌入表示相对大一些
            # 对输入的词向量进行缩放，放大了 sqrt(d_model) 倍，是为了让位置编码与词向量在数值范围上匹配。
            x = x * math.sqrt(self.d_model)
            # 增加位置常量到单词嵌入表示中

            seq_len = x.size(1) # 获取当前输入序列的长度 seq_len
            # 从预计算好的位置编码中取出前 seq_len个位置编码
            # x = x + Variable(self.pe[:,:seq_len], require_grad=False).cuda()
            x = x + self.pe[:, :seq_len].detach().cuda()  # 强制使用GPU
            # x = x + self.pe[:, :seq_len]  # 不强制使用GPU

            return x

# 提问
# 为什么pe = pe.unsqueeze(0)之后维度变为[1, max_seq_len, d_model]，还能x = x + self.pe[:, :seq_len] 将pe加到词向量上？

"""
# 批处理 batch_size 和 广播机制 broadcasting

假设 输入词向量 x 的形状是:
x.shape = [batch_size, seq_len, d_model]
比如：[32, 20, 512] 表示 batch 中有 32 句话，每句话最多 20 个词，每个词用 512 维的向量表示。
位置编码矩阵PE是这样构建的
"
pe = torch.zeros(max_seq_len, d_model)  # shape: [max_seq_len, d_model]
pe = pe.unsqueeze(0)                    # shape: [1, max_seq_len, d_model]
"
这样做的目的是为了能够和 batched 输入 相加。
所以现在 self.pe 的形状是：[1, max_seq_len, d_model]
"
pe = self.pe[:, :seq_len]  # 取出前 seq_len 个位置
x = x + pe
"
假设当前输入句子长度是 seq_len=10，那么 pe[:, :10] 的形状是：[1, 10, 512]
而 x 的形状是：[batch_size, 10, 512]，比如 [32, 10, 512]

# 为什么可以相加？—— 广播机制（Broadcasting）
PyTorch 会自动将 pe 的形状从 [1, 10, 512] 广播（broadcast） 到 [32, 10, 512]，与 x 对齐后再做加法。

✅ 广播规则简单理解：
如果两个张量的维度不同，PyTorch 会从最右边开始对齐维度，然后在维度为 1 的地方进行“复制扩展”。
张量	形状
x	[32, 10, 512]
pe	[1, 10, 512]
第一维（batch）：1 → 自动扩展成 32
第二维（seq_len）：10 ↔ 10，匹配
第三维（d_model）：512 ↔ 512，匹配
✅ 所以它们可以相加！
举个例子
"
x.shape = [2, 3, 4]  # batch_size=2, seq_len=3, d_model=4
pe.shape = [1, 3, 4]
"
当执行 x + pe 时，PyTorch 会把 pe 复制一份变成 [2, 3, 4]，然后再加到 x 上。整个过程不需要显式复制，而是通过广播高效完成。


总之：
- unsqueeze(0) 是为了让位置编码能兼容 batch 维度，
- 而通过 广播机制（Broadcasting），我们可以直接将其加到词向量上，无需手动复制。
"""
