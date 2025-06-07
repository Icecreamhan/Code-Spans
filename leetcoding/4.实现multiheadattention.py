# 第二步 实现多头注意力层
"""
在编码输入序列中每一个单词的表示的过程中，
q_i 查询
k_i 键
v_i 值
这三个元素用于计算上下文单词所对应的权重得分，
这些权重反映了在编码当前单词表示时，对于上下文不同 部分所需要的关注程度

为了防止过大的匹配分数在后续softmax计算过程中导致的梯度爆炸以及收敛效率差的问题，
会除以缩放因子 d^(1/2),以稳定优化，

多头自注意力机制，以关注上下文的不同侧面
1、在不同的子空间中分别计算并得到不同的上下文相关的单词序列表示
2、经过线性变换，用于综合不同子空间中的上下文表示并形成自注意力层最终的输出。
"""
import math

import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiHeadAttention(nn.module):
    def __init__(self, heads, d_model, dropout=0.1):
        super().__init__()

        self.d_model = d_model  # 输入向量的维度，通常是512
        self.d_k = d_model // heads     # 每个注意力头的维度，每个head 的维度，向下取整除
        self.h = heads  # 注意力头的数量，例如 8

        self.q_linear = nn.Linear(d_model, d_model)  # Query线性变换
        self.v_linear = nn.Linear(d_model, d_model)  # Value线性变换
        self.k_linear = nn.Linear(d_model, d_model)  # Key线性变换
        self.dropout = nn.Dropout(dropout)  # Dropout层
        self.out = nn.Linear(d_model, d_model)  # 输出线性变换

    @staticmethod
    def attention(q, k, v, d_k, mask=None, dropout=None):
        scores = torch.matmul(q, k.transpose(-2, -1))  # 计算点积
        scores = scores/math.sqrt(d_k)  # 缩放,d_k 是每个头的维度，根号d_k是为了防止内积过大导致的梯度消失

        # 掩盖掉那些为了填补长度增加的单元，使其通过 softmax 计算后为 0
        # mask是用来屏蔽填充或未来信息（解码器中防止看到后续词）
        if mask is not None:
            mask = mask.unsqueeze(1)  # 扩展mask
            scores = scores.masked_fill(mask == 0, -1e9)  # 掩码的位置设为极小值

        scores = F.softmax(scores, dim=-1)  # softmax归一化

        if dropout is not None:
            scores = dropout(scores)  # 防止过拟合

        output = torch.matmul(scores, v)  # 加权求和得到输出
        return output

    def forward(self, q, k, v, mask=None):
        bs = q.size(0)  # batch_size

        # 进行线性操作,并拆分到/划分为 h 个头
        k = self.k_linear(k).view(bs, -1, self.h, self.d_k)  # 形状变为 [batch_size,num_heads,seq_len,d_k]
        q = self.q_linear(q).view(bs, -1, self.h, self.d_k)
        v = self.v_linear(v).view(bs, -1, self.h, self.d_k)

        # 矩阵转置，以便计算 attention
        k = k.transpose(1, 2)
        q = q.transpose(1, 2)
        v = v.transpose(1, 2)
# [bs,seq_len,h,d_k] ——> [bs,h,seq_len,d_k]
        # 计算attention
        scores = attention(q, k, v, self.d_k, mask, self.dropout)

        # 连接多个头并输入到最后的线性层
# all attention outputs ——> [bs,seq_len,h*d_k] = [bs,seq_len,d_model]
        concat = scores.transpose(1,2).contiguous().view(bs, -1, self.d_model)

        output = self.out(concat)

        return output

