import os 
import sys
import re
import pandas as pd


def get_data(fh):
    lines = []
    energy_dict = {}
    fh = open(fh,  "r")
    for line in fh:
        lines.append(line)
    for i in range(len(lines)-1):
        if re.match("Molecule: AB-[0-9]+", lines[i]):
            mol_lst = re.split("[:,\n]", lines[i])
            mol_lst = [x for x in mol_lst if x != ""]
            #print lines[i+6]
            if re.match("\s+Grid Score:\s+(-)?[0-9][0-9]\.[0-9]+", lines[i+6]):
                grid_lst = re.split("[\s+,\n]", lines[i+6])
                grid_lst = [x for x in grid_lst if x != ""]
                if mol_lst[1] not in energy_dict.keys():
                    energy_dict[mol_lst[1]] = [float(grid_lst[2])]
                else:
                    if float(grid_lst[2]) not in energy_dict[mol_lst[1]]:
                        energy_dict[mol_lst[1]].append(float(grid_lst[2]))
                    else:
                        pass
            elif re.match("/s+GB//SA Score:\s+(-)?[0-9][0-9]\.[0-9]+", lines[i+2]):
                energy_dict[mol_lst[i]] = lines[i+2]
            else:
                pass
        else:
            pass

    print energy_dict
    fhn = open("highest_grid_scores.txt", "a")
    for i in energy_dict.keys():
        str_mol = i+":"
        for i in energy_dict[i]:
            str_mol += i
        str_mol += "\n"
        fhn.write(str_mol)      
    fhn.close()              
         
def main():
    get_data("dock_xing.out")

if __name__ == '__main__':
    main()