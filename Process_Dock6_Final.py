#!/usr/bin/python
#Author: Phoenix Logan
#Usage: name file you want data parsed on as sys.argv[1] identifiers in quotes ex: "AB-|SMSF"
#ex run python Process_Dock6_Final.py dock_xing.out "AB-|SMSF"    

import os, sys, re
import pandas as pd

def make_lists(seps, line_num):
    """split list by certain parameter and remove excess white space"""
    mol_list = re.split(seps, line_num)
    #remove excess white space
    mol_split_lst = [x for x in mol_list if x != ""]
    return mol_split_lst

def get_data(fh, identifiers):
    """ Get grid and secondary scores from each unique molecular entry"""
    energy_dict = {}
    fh = open(fh,  "r")
    lines = [line for line in fh]
    for i in range(len(lines)-1):
        #search for all instances of molecular ID 
        if re.match("Molecule: ("+identifiers+")[0-9]+", lines[i]) and i < (len(lines) - 8):
            mol_lst = make_lists("[:,\n]", lines[i])
            if re.match("\s+Grid Score:\s+(-)?[0-9]+\.[0-9]+", lines[i+9]):
                grid_lst = make_lists("[\s+,\n]", lines[i+9])
                if mol_lst[1] not in energy_dict.keys():
                    energy_dict[mol_lst[1]] = ["Grid Score: "+grid_lst[2]]
                elif "Grid Score "+grid_lst[2] not in energy_dict[mol_lst[1]]:
                    energy_dict[mol_lst[1]].append("2nd Grid Score: "+grid_lst[2])
                else:
                    pass
            elif re.match("\s+GB/SA Score:\s+(-)?[0-9]+\.[0-9]+", lines[i+3]):
                GBSA_lst = make_lists("[\s+,\n]", lines[i+3])
                energy_dict[mol_lst[1]].append("GB/SA Score: "+GBSA_lst[2])
            else:
                pass
        else:
            pass
    return energy_dict
        
def write_results(file_ID, energy_dict):
    """Write results of parsed data to file"""
    fhn = open("Dock6_Scores.txt"+str(file_ID), "a")
    for i in energy_dict.keys():
        str_mol = i+"|"
        for i in energy_dict[i]:
            str_mol += str(i)+"|"
        str_mol += "\n"
        fhn.write(str_mol)
    fhn.close()

def main():
    energy_dict = get_data(sys.argv[1], sys.argv[2])
    write_results(2, energy_dict)
    
if __name__ == '__main__':
    main()
