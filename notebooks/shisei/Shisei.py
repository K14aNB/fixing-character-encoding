# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: ipyenv
#     language: python
#     name: python3
# ---

# # Shisei

import pandas as pd
import charset_normalizer

# +
# Figure out the encoding using charset_normalizer
with open('../../data/shisei_UTF-8.txt','rb') as raw:
    res = charset_normalizer.detect(raw.read(100000))

print(res)
# -

# Import the data in UTF-8 encoding
data = pd.read_csv('../../data/shisei_UTF-8.txt', sep='\t', header=None)

print(data)


