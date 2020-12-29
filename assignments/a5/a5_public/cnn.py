#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS224N 2018-19: Homework 5
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

### YOUR CODE HERE for part 1i


class CNN(nn.Module):
    def __init__(self,
                 kernel_size=5,
                 word_embedding_dim=None,
                 char_embedding_dim=None):
        super(CNN, self).__init__()
        self.kernel_size = kernel_size
        self.word_embedding_dim = word_embedding_dim
        self.char_embedding_dim = char_embedding_dim
        self.conv1d = nn.Conv1d(in_channels=self.char_embedding_dim,
                                out_channels=self.word_embedding_dim,
                                kernel_size=self.kernel_size,
                                bias=True)

    def forward(self, x):
        '''
        x: (batch, max_word_length, embedding_size)
        return: (batch, embedding_size)
        '''
        x = x.permute(0, 2, 1)
        x = F.relu(self.conv1d(x))
        x = torch.max_pool1d(x, kernel_size=x.shape[-1]).squeeze(dim=-1)
        return x


### END YOUR CODE

if __name__ == '__main__':
    cnn = CNN(word_embedding_dim=20, char_embedding_dim=50)
    x = torch.randn((5, 6, 50))
    print(cnn(x), cnn(x).shape)