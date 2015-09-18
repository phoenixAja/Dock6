import os, sys
from rdkit import *

def run_ms():
    os.system("dms rec_noH.pdb -n -w 1.4 -v -o rec.ms")

def run_spheres():
    os.system("sphgen")

def run_box():
    os.system("showbox < box.in")
    
def run_grid():
    os.system("grid -i grid.in -o grid.out")

def run_dock_6.7(num):
    os.system("dock6 -i anchor_and_grow_"+str(num)+".in -o anchor_and_grow_"+str(num)+".out")

        
        
        
        
        
    
