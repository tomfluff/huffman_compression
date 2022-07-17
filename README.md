# Huffman Compression
A simple Python implementation of Huffman compression of text, with compression ratio and KL-divergence.

### How to Run
To run the code, please use:
```
python main.py
```

## Huffman Code
Huffman compression uses text as an input, constructs the assumed character distribution and assigns new prefix-free codes based on the distributions. In such a way that more frequent characters would get a *binary* code using less *bits*. This is done by constructing a *Huffman Tree* and generating bit-codes based on the tree structure.

## Compression Ratio
Describes the ratio between the compressed text to the original size. In other words, what is the precentage of the compressed text (in bits) to the original text. For example, if based on 8-bit (1-byte) text, if the text "A" have been compressed from `0100 0001` to `0`, the compression ratio is: `1 / 8 = 0.125`.

## KL-Divergence
Defined as: 

$ D(p||q)=\sum_{x}{p(x)\log\frac{p(x)}{q(x)}} $

Describes the distance between two distributions, `p` the true distribution and `q` the assumed distribution. The larger the number the more different they are, thus the worse the compression would be.