import re


def open_file(mol_file):
    energy_dict = {}
    fh = open(mol_file, "r")
    fh_lines = fh.readlines()
    fh.close()
    for i in range(len(fh_lines)):
        fh_lines[i].split("\s+")
        if fh_lines[i][0] == "#" and fh_lines[i][1] == "Name:":
            if fh_lines[i] not in energy_dict.keys():
                energy_dict[fh_lines[i]] = fh_lines[i+1]
    print energy_dict        
                             
        
    
def main():
    #run functions
    open_file("anchor_and_grow_scored.mol2")
    
if __name__ == "__main__":
    main()        