#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS224N 2018-19: Homework 5
model_embeddings.py: Embeddings for the NMT model
Pencheng Yin <pcyin@cs.cmu.edu>
Sahil Chopra <schopra8@stanford.edu>
Anand Dhoot <anandd@stanford.edu>
Michael Hahn <mhahn2@stanford.edu>
"""

import torch.nn as nn

# Do not change these imports; your module names should be
#   `CNN` in the file `cnn.py`
#   `Highway` in the file `highway.py`
# Uncomment the following two imports once you're ready to run part 1(j)

from cnn import CNN
from highway import Highway

import torch
# End "do not change"


class ModelEmbeddings(nn.Module):
    """
    Class that converts input words to their CNN-based embeddings.
    """
    def __init__(self, embed_size, vocab):
        """
        Init the Embedding layer for one language
        @param embed_size (int): Embedding size (dimensionality) for the output 
        @param vocab (VocabEntry): VocabEntry object. See vocab.py for documentation.
        """
        super(ModelEmbeddings, self).__init__()

        ## A4 code
        # pad_token_idx = vocab.src['<pad>']
        # self.embeddings = nn.Embedding(len(vocab.src), embed_size, padding_idx=pad_token_idx)
        ## End A4 code

        ### YOUR CODE HERE for part 1j

        self.embed_size = embed_size
        self.char_embed_size = 50

        self.cnn = CNN(kernel_size=5,
                       word_embedding_dim=self.embed_size,
                       char_embedding_dim=self.char_embed_size)
        self.highway = Highway(word_embedding_dim=self.embed_size)

        pad_char_idx = vocab.char2id['<pad>']
        self.embeddings = nn.Embedding(len(vocab.char2id),
                                       self.char_embed_size,
                                       padding_idx=pad_char_idx)

        ### END YOUR CODE

    def forward(self, input: torch.Tensor):
        """
        Looks up character-based CNN embeddings for the words in a batch of sentences.
        @param input: Tensor of integers of shape (sentence_length, batch_size, max_word_length) where
            each integer is an index into the character vocabulary

        @param output: Tensor of shape (sentence_length, batch_size, embed_size), containing the 
            CNN-based embeddings for each word of the sentences in the batch
        """
        ## A4 code
        # output = self.embeddings(input)
        # return output
        ## End A4 code

        ### YOUR CODE HERE for part 1j

        sentence_length, batch_size = input.shape[0], input.shape[1]
        initial_embeddings = self.embeddings(
            input
        )  # (sentence_len, batch_size, max_word_length, embedding_size)
        initial_embeddings = initial_embeddings.reshape(
            (-1, initial_embeddings.shape[-2], self.char_embed_size))
        x_conv_out = self.cnn(initial_embeddings)
        x_word_emb = self.highway(x_conv_out).reshape(sentence_length,
                                                      batch_size, -1)

        return x_word_emb
        ### END YOUR CODE
