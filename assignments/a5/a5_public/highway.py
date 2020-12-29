#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS224N 2018-19: Homework 5
"""

import torch
import torch.nn as nn

### YOUR CODE HERE for part 1h


class Highway(nn.Module):
    def __init__(self, word_embedding_dim=None, dropout_rate=0.3):
        super(Highway, self).__init__()
        self.word_embedding_dim = word_embedding_dim
        self.proj_layer = nn.Linear(in_features=self.word_embedding_dim,
                                    out_features=self.word_embedding_dim,
                                    bias=True)
        self.gate_layer = nn.Linear(in_features=self.word_embedding_dim,
                                    out_features=self.word_embedding_dim,
                                    bias=True)
        self.relu_layer = nn.ReLU()
        self.dropout_layer = nn.Dropout(p=dropout_rate)

    def forward(self, x):
        '''
        x: (batch, eword)
        '''
        x_proj = self.relu_layer(self.proj_layer(x))
        x_gate = torch.sigmoid(self.gate_layer(x))
        x_highway = torch.mul(x_proj, x_gate) + torch.mul(x, 1 - x_gate)
        x_highway = self.dropout_layer(x_highway)
        return x_highway


### END YOUR CODE

if __name__ == '__main__':
    highway = Highway(word_embedding_dim=10)
    x = torch.randn((5, 10))
    print(highway(x))
