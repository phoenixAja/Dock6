
import os
import sys
import pandas as pd
from pandas import DataFrame, Series

def read_mmol2(fh):
    mmol2 = pd.read_table(fh, header=False)
    mmol2_2 = DataFrame(mmol2)
    atom_list = mmol2_2[mmol2_2["#   Created by UNITY Export Utility"] == "@<TRIPOS>ATOM"].index.tolist()
    bond_list = mmol2_2[mmol2_2["#   Created by UNITY Export Utility"] == "@<TRIPOS>BOND"].index.tolist()
    molecule_list = mmol2_2[mmol2_2["#   Created by UNITY Export Utility"] == "@<TRIPOS>MOLECULE"].index.tolist()
    print molecule_list, bond_list, atom_list
    
    sections = []
    w_sections = []
    for i in range(len(atom_list)-1):
        range_int = [atom_list[i]+1, bond_list[i]]
        range_w = [molecule_list[i], molecule_list[i+1]-1]
        sections.append(range_int) 
        w_sections.append(range_w)
    print w_sections

    mmol2_dict = {}
    mmol2_whole = {}
    for i in range(len(sections)-1):
        df_edit = mmol2_2.loc[range(sections[i][0], sections[i][1])]
        df_edit2 = mmol2_2.loc[range(w_sections[i][0], w_sections[i][1])]
        mmol2_dict[i] = df_edit    
        mmol2_whole[i] = df_edit2
        
    for i in mmol2_dict.keys():
        j = mmol2_dict.get(i)["#   Created by UNITY Export Utility"].str.split('\s+')
        mmol2_dict[i] = j
        
        
    for i in mmol2_dict.keys():
        val = mmol2_dict[i]
        z_coords = []
        for k in val:
            z_num = float(k[4])
            z_coords.append(z_num)
        if sum(z_coords) == 0.0000:
            f = open("flat_"+str(i), "w")
            mmol2_whole.get(i).to_csv("flat_"+str(i)+".mol2", index=False)
            del(mmol2_whole[i])
        for value in mmol2_whole.values():
            with open("mmol2_parsed.mol2", "a") as fh:
                value.to_csv(fh, mode= "a", header = False, index=False)
            
            
            
             

 
def main():
    read_mmol2("only_one_flat.mol2")
    
    
if __name__ == "__main__":
    main()
    