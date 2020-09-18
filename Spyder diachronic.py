# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:02:38 2020

@author: Sara
"""

import pandas as pd

df = pd.read_csv('DataSeerGrabPrizeData.csv')

df.describe()

df = df.dropna()

df.describe()

df.to_csv('grab_on_spyder.csv', index=False)

