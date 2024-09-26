# ================================================
# Here the goal is to take some very big files
# and make them smaller by saving a subset 
# of rows that follow a particular contidion
# ================================================

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

# ===================================== #

DRIVE = '/home/frieren/BIG/'
PROJECT = 'reentrancy'
TEST = 'test11'
SIZE = 10

DATA_PATH = os.path.join(DRIVE,PROJECT,TEST,str(SIZE))
fh = open(os.path.join(DATA_PATH,'dis_ver.csv'),'r')

target = os.path.join(DATA_PATH,'disver_20mT.csv')

# for reference, the field column is the 101 element, 0-based index

# the logic is go line by line
for line in fh:
    sep_line = line.split(',')
    field_value = sep_line[101]

    # if the line contains the field value i am interested in 
    # then write that line
    if field_value=='20mT' or field_value=='field':
        with open(target,'a') as file_obj:
            file_obj.write(line)

fh.close()


