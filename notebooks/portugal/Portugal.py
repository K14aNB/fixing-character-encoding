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

# # Portugal enfermo por vicios, e abusos de ambos os sexos

import pandas as pd
import charset_normalizer
from csv import QUOTE_NONE

# +
# Figure out the encoding using charset normalizer
with open('../../data/portugal_ISO-8859-1.txt','rb') as raw:
    res = charset_normalizer.detect(raw.read(10000))

print(res)
# -

# Import the data in latin_1 encoding
data = pd.read_csv('../../data/portugal_ISO-8859-1.txt',sep='\t',header=None,encoding='latin_1')

print(data)

# Save the file in UTF-8 format
data.to_csv('../../data/portugal_utf-8_encoded.txt', sep='\t',header=None,index=False,quoting=QUOTE_NONE,escapechar='\\')


