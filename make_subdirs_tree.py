#!/usr/bin/env python3

"""
Simple code for creating a tree of sub_dirs
"""

### ---------------------------------------- ###

def getFolderStructure():
    
    # Finding directories and their level in the hierarchy
    directories = [directory[0] for directory in walk(top='./')]
    dir_levels = [current_dir.count('/') - 1 for current_dir in directories]
    dir_levels[0] = -1
    
    # Building structure
    structure = []
    n_spaces = 4
    for n, current_dir in enumerate(directories):
        
        if n == 0: # First element (root)
            
            structure.append(current_dir)
        
        else:
            
            # Extracting info
            basename = current_dir.split('/')[-1]
            current_level = dir_levels[n]
            next_element_level = dir_levels[n + 1] if n + 1 != len(directories) else dir_levels[n] - 1
            
            # Building new line of the structure
            line_elements = []
            for l in range(current_level + 1):
                
                if l < dir_levels[n]:
                    
                    if l in dir_levels[n:]:
                        
                        new_element = f"\u2502{' ' * (n_spaces - 1)}"
                    
                    else:
                        
                        new_element = f"{' ' * n_spaces}"
                    
                else:
                    
                    if current_level > next_element_level or l not in dir_levels[n + 1:]:
                        
                        new_element = '\u2514' + '\u2500' * (n_spaces - 2) + ' ' + basename
                    
                    else:
                        
                        new_element = '\u251c' + '\u2500' * (n_spaces - 2) + ' ' + basename
                
                line_elements.append(new_element)
            
            structure.append(''.join(line_elements))
        
    structure = '\n'.join(structure)
    
    return structure

### ------------------MAIN------------------ ###

from os import walk

folder_structure = getFolderStructure()

print(folder_structure)