# this script is a continuation of take_distances.py
# the goal here it to compute the same thing across realizations

import os
import sys

import numpy as np
import pandas as pd
sys.path.insert(0, '../../../icenumerics/')
sys.path.insert(0, '../auxnumerics/')
sys.path.insert(0, '../')

import icenumerics as ice
import concurrent.futures
import auxiliary as aux
import vertices as vrt

from parameters import params
from tqdm import tqdm
import importlib
import argparse

ureg = ice.ureg
idx = pd.IndexSlice

DRIVE = '/home/frieren/BIG/'
PROJECT = 'reentrancy'
SIZE = 10

DATA_PATH = os.path.join(DRIVE,PROJECT,'test11',str(SIZE))

# loading the horizontal data
print('doing horizontals')
hor = pd.read_csv(os.path.join(DATA_PATH,'sum_hor.csv'))


# here the goal is to get the average across realizations
# for all possible ttimes (omegas) and fields
# mean | var | total_time | field | current time | theta

hor_global = [] # init

# loop through all different times
for ttime, df_t in hor.groupby('total_time'):
    # then explore by all possible fields
    for field, df_tf in df_t.groupby('field'):
        # finally go through all realizations
        for ct,df_tfr in df_tf.groupby('t'):
            # now i can finally take the average across realizations
            mean = df_tfr['mean'].mean()
            var = df_tfr['mean'].var()
            theta = df_tfr['theta'].to_list()[0]
            cdata = [mean, var, ttime, field, ct, theta]
            
            hor_global.append(cdata)

horav = pd.DataFrame(hor_global, columns = ['mean','var','total_time','field','current_time','theta'])
horav.to_csv(os.path.join(DATA_PATH,'horav.csv'),index=False)

# do the same but for the vertical
print('doing verticals')
ver = pd.read_csv(os.path.join(DATA_PATH,'sum_ver.csv'))

ver_global = [] # init

# loop through all different times
for ttime, df_t in ver.groupby('total_time'):
    # then explore by all possible fields
    for field, df_tf in df_t.groupby('field'):
        # finally go through all realizations
        for ct,df_tfr in df_tf.groupby('t'):
            # now i can finally take the average across realizations
            mean = df_tfr['mean'].mean()
            var = df_tfr['mean'].var()
            theta = df_tfr['theta'].to_list()[0]
            cdata = [mean, var, ttime, field, ct, theta]
            
            ver_global.append(cdata)

verav = pd.DataFrame(ver_global, columns = ['mean','var','total_time','field','current_time','theta'])
verav.to_csv(os.path.join(DATA_PATH,'verav.csv'),index=False)


