# =============================================================================
# Here the goal is to compute the particle displacements as a function of time
# that is R(t) = |r(t) - r(0)|
# the code saves a file in the data folder with the schema 
# mentioned in the code
# =============================================================================


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

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_distances(filepath):

    # load the trj
    trj = ice.trajectory(filepath)
    trj.load()
    frames = trj.trj.index.get_level_values('frame').unique().to_numpy()

    # go particle by particle and compute the distance with respect to the initial position
    # as time evolves |r(t) - r(0)|
    # i also separate by horizontals and verticals
    
    ts_horizontal = [] # init
    ts_vertical = [] # init
    hid = [] # init
    vid = [] # init

    for pid, ptrj in trj.trj.groupby('id'):

        rels = ptrj[['cx','cy','cz']]
        dirs = ptrj[['dx','dy','dz']].to_numpy() / params['trap_sep'].magnitude # normalize to have unitary directions

        # to get the parallel component, I just need to compute the dot product of
        # rel . abs(dir)

        rparallel = np.sum(rels.values * np.abs(dirs),axis=1)

        if aux.is_horizontal(dirs[0]):
            # substract the initial position and take the norm
            d = np.abs((rparallel - rparallel[0]))
            ts_horizontal.append(d)
            hid.append(pid)
        else:
            d = np.abs((rparallel - rparallel[0]))
            ts_vertical.append(d)
            vid.append(pid)

    # now that we have everything is time to save into disk
    return frames, np.asarray(hid), np.asarray(vid), np.asarray(ts_horizontal), np.asarray(ts_vertical)


DRIVE = '/home/frieren/BIG/'
PROJECT = 'reentrancy'
SIZE = 10

DATA_PATH = os.path.join(DRIVE,PROJECT,'test11',str(SIZE))

total_times = [x for x in os.listdir(DATA_PATH) if isint(x)]

# this variable will make the headers only one time 
# since it will be converted to false after the first interation
make_headers = True


# go through all the possible times
for ttime in tqdm(total_times):
    print('total_time: ',ttime)
    # go through all the possible fields
    time_path = os.path.join(DATA_PATH,ttime)
    fields = [x for x in os.listdir(time_path) if x.endswith('mT')]

    for field in tqdm(fields):
        field_path = os.path.join(time_path,field)

        # go through the realizations
        for realization in tqdm(range(1,11)):
            rpath = os.path.join(field_path,f'xtrj{realization}.csv')
            ## do a bunch of stuff

            frames, hid, vid, tsh, tsv = get_distances(rpath)
            # i will put one particle per columns
            # and add the columns of
            # 1 ... N | total_time | field | realization | t | theta

            # first horizontal

            # dfh = pd.DataFrame(
            #     np.asarray([np.mean(tsh,axis=0),np.var(tsh,axis=0)]).transpose(),
            #     columns=['mean','var']
            # )
            dfh = pd.DataFrame(
                tsh.transpose(),
                columns=[hid]
            )
            dfh['total_time'] = [float(ttime)] * len(dfh)
            dfh['field'] = [float(field[:-2])] * len(dfh)
            dfh['realization'] = [realization] * len(dfh)
            dfh['t'] = frames / params['framespersec'].magnitude
            dfh['theta'] = frames / params['framespersec'].magnitude * np.pi/2/float(ttime) * 180/np.pi


            # do the save for verticals
            dfv = pd.DataFrame(
                tsv.transpose(),
                columns=[vid]
            )
            # dfv = pd.DataFrame(
            #     np.asarray([np.mean(tsv,axis=0),np.var(tsv,axis=0)]).transpose(),
            #     columns=['mean','var']
            # )
            dfv['total_time'] = [float(ttime)] * len(dfv)
            dfv['field'] = [float(field[:-2])] * len(dfh)
            dfv['realization'] = [realization] * len(dfv)
            dfv['t'] = frames / params['framespersec'].magnitude
            dfv['theta'] = frames / params['framespersec'].magnitude * np.pi/2/float(ttime) * 180/np.pi

            # save everything
            if make_headers:
                dfh.to_csv(os.path.join(DATA_PATH,'dis_hor_rp.csv'), index=False)
                dfv.to_csv(os.path.join(DATA_PATH,'dis_ver_rp.csv'), index=False)
                make_headers = False
            else:
                dfh.to_csv(os.path.join(DATA_PATH,'dis_hor_rp.csv'), mode='a', index=False, header=False)
                dfv.to_csv(os.path.join(DATA_PATH,'dis_ver_rp.csv'), mode='a', index=False, header=False)
    os.system('clear')
