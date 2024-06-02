'''Write a program to clear the clutter inside a folder on your computer. 
You should use os module to rename all the png images from 1.png all the way till n.png 
where n is the number of png files in that folder. Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png'''

# Lets create a function to generalize that 

def clear_clatter_all(path):
    import os 
    os.chdir(path)
    
    files_by_ext = {}
    files_by_ext['No Ext'] = []
    # Loop through all files in the current directory
    for filename in os.listdir():
        # Check if the current file is a regular file
        if os.path.isfile(filename):
            # Get the extension of file 
            parts = filename.split(".")
            if len(parts) > 1:
                ext = parts[-1]
                if ext in files_by_ext.keys():
                    files_by_ext[ext].append(filename)
                else:
                    files_by_ext[ext] = [filename]
            else:
                files_by_ext['No Ext'].append(filename)
    
    for ext in files_by_ext.keys():
        files = files_by_ext[ext]
        i = 1
        for file in files:
            os.rename(file, f"{i}.{ext}")
            i += 1


def clatter_ext(path, ext):
    import os 
    os.chdir(path)
    i = 1
    for file in os.listdir():
        # Check if the current file is a regular file
        if os.path.isfile(file):
            if file.endswith(ext):
                os.rename(file, f"{i}.{ext}")
                i += 1

if __name__ == '__main__':
    path = '#####################'
    import os 
    os.chdir(path)
    for filename in os.listdir():
        # Check if the current file is a regular file
        if os.path.isfile(filename):
            print(filename)
    
    clatter_ext(path, 'pdf')

    for filename in os.listdir():
        # Check if the current file is a regular file
        if os.path.isfile(filename):
            print(filename)

    clear_clatter_all(path)
    for filename in os.listdir():
        # Check if the current file is a regular file
        if os.path.isfile(filename):
            print(filename)

# We checked the program and it works