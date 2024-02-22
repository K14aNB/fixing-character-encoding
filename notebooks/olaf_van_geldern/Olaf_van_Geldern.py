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

# # Olaf van Geldern

import pandas as pd
import charset_normalizer
from csv import QUOTE_NONE

# Figure out the encoding using charset normalizer
with open('../../data/olaf_Windows-1251.txt','rb') as raw:
    res = charset_normalizer.detect(raw.read(10000))
print(res)

# Import the data in Windows-1251 encoding
data = pd.read_csv('../../data/olaf_Windows-1251.txt',sep='\t',header=None,encoding='Windows-1251')

print(data)

# Save the file in UTF-8 format
data.to_csv('../../data/olaf_utf-8_encoded.txt', sep='\t', header=None, index=False,quoting=QUOTE_NONE,escapechar='\\')


