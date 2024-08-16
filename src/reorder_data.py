import os
import sys
import shutil

DATA_PATH = '../data/test11/10'
complete = next(os.walk(DATA_PATH))[1]
ignore_folders = ['frames']

omegas = [omega for omega in complete if omega not in ignore_folders]

for omega in omegas:
    fields = next(os.walk(os.path.join(DATA_PATH,omega)))[1]

    for field in fields:
        cwd = os.path.join(DATA_PATH,omega,field)
        files = os.listdir(os.path.join(cwd,'vertices'))
        for file in files:
            fp = os.path.join(cwd,'vertices',file)
            shutil.move(fp,cwd)

        files = os.listdir(os.path.join(cwd,'trj'))
        for file in files:
            fp = os.path.join(cwd,'trj',file)
            shutil.move(fp,cwd)




