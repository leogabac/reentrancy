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

DATA_PATH = os.path.join(DRIVE, PROJECT, TEST, str(SIZE))
OMEGAS = [d for d in os.listdir(DATA_PATH) if os.path.isdir(os.path.join(DATA_PATH,d))]
REALIZATIONS = list(range(1,11))

makeheaders = True
for w in OMEGAS:
    print(f'total_time = {w}')
    # I will focus on 20mT
    # here wf_path is for w and field
    fields = [x[:-2] for x in os.listdir(os.path.join(DATA_PATH,w)) if x.endswith('mT')]
    #field = 20 # hardcoded for the time being
    for field in tqdm(fields):
        wf_path = os.path.join(DATA_PATH,w,f'{field}mT')
        # here I wil go trj by trj computing the OP
        # TODO: get this from the vrt file directly
        cumm_kappa = []
        for r in REALIZATIONS:

            # load the trj file
            trj = ice.trajectory(os.path.join(wf_path,f'xtrj{r}.csv'))
            trj.load()
            frames = trj.trj.index.get_level_values('frame').unique().to_list()
            for frame in frames:
                sel_trj = trj.trj.xs(frame,level='frame')

                # now compute the stuff
                centers, dirs, rels = vrt.trj2numpy(sel_trj)
                dirs = dirs / np.max(dirs)
                vrt_lattice = vrt.create_lattice(params['lattice_constant'].magnitude, int(SIZE))
                idx_lattice = vrt.indices_lattice(vrt_lattice, centers, params['lattice_constant'].magnitude, int(SIZE))
                kappa = vrt.charge_op(vrt.get_charge_lattice(idx_lattice, dirs))
                # realization | timestamp | kappa | field | total_time
                data = [r, sel_trj.t[0], kappa, field, w]
                cumm_kappa.append(data)

        # after all realizations, just save
        df = pd.DataFrame(cumm_kappa, columns=['realization', 't', 'kappa', 'field', 'total_time'])
        if makeheaders:
            df.to_csv(os.path.join(DATA_PATH, 'kappa_all.csv'), index=False)
            makeheaders = False
        else:
            df.to_csv(os.path.join(DATA_PATH, 'kappa_all.csv'), mode='a',index=False, header=False)
