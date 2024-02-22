# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: ipyenv
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Die Furstin

# %%
import pandas as pd
import charset_normalizer

# %%
# Figure out the encoding using charset_normalizer
with open('../../data/die_ISO-8859-1.txt', 'rb') as raw:
    result = charset_normalizer.detect(raw.read(10000))

print(result)

# %%
# Try Importing dataset
data = pd.read_csv('../../data/die_ISO-8859-1.txt', sep='\t', header=None,encoding='latin_1')

# %%
# Print the data
print(data)


# %%
# Save the file in UTF-8 encoded format
data.to_csv('../../data/die_utf-8_encoded.txt', index=False, header=None, sep='\t')

# %%
