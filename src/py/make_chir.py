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
DRIVE = '/mnt/BIG/'
PROJECT = 'reentrancy'
TEST = 'test11'
SIZE = 10

DATA_PATH = os.path.join(DRIVE, PROJECT, TEST, str(SIZE))
OMEGAS = [d for d in os.listdir(DATA_PATH) if os.path.isdir(os.path.join(DATA_PATH,d))]
REALIZATIONS = list(range(1,11))

a = params['lattice_constant'].magnitude

makeheaders = True
for w in tqdm(OMEGAS, desc='Total time'):
    tqdm.write(f'Current value {w} s')
    # I will focus on 20mT
    # here wf_path is for w and field
    fields = [x[:-2] for x in os.listdir(os.path.join(DATA_PATH,w)) if x.endswith('mT')]

    for field in tqdm(fields, desc='Field'):


        wf_path = os.path.join(DATA_PATH,w,f'{field}mT')
        cumm_chirs = []
        for r in REALIZATIONS:
            # load the trj file
            trj = ice.trajectory(os.path.join(wf_path,f'xtrj{r}.csv'))
            trj.load()
            frames = trj.trj.index.get_level_values('frame').unique().to_list()

            # create the shifted lattice at center of squares
            chir_lattice = vrt.create_lattice(params['lattice_constant'].magnitude, int(SIZE), spos=(a/2,a/2))

            for frame in frames:

                # why am i computing lots of stuff for all frames?
                # the centers don't necesarily come in the same order each frame
                # i did not want to fix that, so i just went full wasting computing effort mode

                sel_trj = trj.trj.xs(frame,level='frame')
                centers, dirs, rels = vrt.trj2numpy(sel_trj)
                dirs = dirs / np.max(dirs)
                # create the indices for linked spins
                # thankfully applies the same as previously
                idx_lattice = vrt.indices_lattice(chir_lattice, centers, params['lattice_constant'].magnitude, int(SIZE))
                idx_lattice = np.asarray(idx_lattice,dtype=int)
                # compute the chirality of that
                chir = vrt.charge_op(vrt.get_chir_lattice(dirs,idx_lattice))
                # realization | timestamp | kappa | field | total_time
                data = [r, sel_trj.t[0], chir, field, w]
                cumm_chirs.append(data)

        # after all realizations, just save
        df = pd.DataFrame(cumm_chirs, columns=['realization', 't', 'kappa', 'field', 'total_time'])
        if makeheaders:
            df.to_csv(os.path.join(DATA_PATH, 'chirs_all.csv'), index=False)
            makeheaders = False
        else:
            df.to_csv(os.path.join(DATA_PATH, 'chirs_all.csv'), mode='a',index=False, header=False)

    os.system('clear')

