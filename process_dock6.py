import os 
import sys
import re
import pandas as pd


def get_data(fh):
    lines = []
    molecules = []
    grid_scores = []
    energy_dict = {}
    fh = open(fh,  "r")
    for line in fh:
        lines.append(line)
    for i in range(len(lines)-1):
        if re.match("Molecule: CHEMBL[0-9]+", lines[i]):
            if re.match("\s+Grid Score:\s+(-)?[0-9][0-9]\.[0-9]+", lines[i+1]):
                mol_lst = re.split("[:,\n]", lines[i])
                mol_lst = [x for x in mol_lst if x != ""]
                grid_lst = re.split("[\s+,\n]", lines[i+1])
                grid_lst = [x for x in grid_lst if x != ""]
                if mol_lst[1] not in energy_dict.keys():
                    energy_dict[mol_lst[1]] = [float(grid_lst[2])]
                else:
                    if float(grid_lst[2]) not in energy_dict[mol_lst[1]]:
                        energy_dict[mol_lst[1]].append(float(grid_lst[2]))
                    else:
                        pass
            else:
                print "no Match"
        else:
            pass

    df_lines = pd.DataFrame(lines)
    #print df_lines
    print molecules 
    fhn = open("highest_grid_scores.txt", "a")
    get_secondary(molecules, lines)
    for i in energy_dict.keys():
        str_mol = i+":"
        max_grid = str(min(energy_dict[i]))
        str_mol += max_grid+"\n"
        fhn.write(str_mol)   
        
    fhn.close()                           
def get_secondary(mol_id, lines):
    for i in mol_id:
        mol_df = pd.DataFrame(lines)
        print mol_df
        mol_ins = mol_df[mol_df["A"]].str.contains(i)
        print mol_ins
    


          
def main():
    get_data("dock_xing.out")

if __name__ == '__main__':
    main()