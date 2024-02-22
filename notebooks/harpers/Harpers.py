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

# # Harpers

import pandas as pd
import charset_normalizer
from csv import QUOTE_NONE

# +
# Figure out the encoding using charset normalizer
with open('../../data/harpers_ASCII.txt','rb') as raw:
    res = charset_normalizer.detect(raw.read(1000))

print(res)
# -

# Import the data in default UTF-8 encoding
data = pd.read_csv('../../data/harpers_ASCII.txt',sep='\t',header=None)

print(data)

# Save the file in UTF-8 format
data.to_csv('../../data/harper_utf-8_encoded.txt',sep='\t',header=None,index=False,quoting=QUOTE_NONE,escapechar='\\')




