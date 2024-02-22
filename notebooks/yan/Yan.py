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

# # Yan shi jia xun

import pandas as pd
import charset_normalizer
from csv import QUOTE_NONE

# +
# Figure out the encoding using charset_normalizer
with open('../../data/yan_BIG-5.txt','rb') as raw:
    res = charset_normalizer.detect(raw.read(100000))

print(res)
# -

# Import the data in Big5 encoding
data = pd.read_csv('../../data/yan_Big-5.txt',sep='\t',header=None,encoding='Big5')

print(data)

# Save the file in UTF-8 format
data.to_csv('../../data/yan_utf-8_encoded.txt', sep='\t', header=None, index=False,quoting=QUOTE_NONE,escapechar='\\')
