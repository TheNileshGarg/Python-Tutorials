## import 
# import - this command loads code from a python module into current script 

import pandas

# to select interpreter - ctrl + shift + p -> python : select interpreter

# once module is imported you can use any of it's functions using dot notation 
#pandas.read_csv()

# import a particlar function from module 
from math import pi, sqrt
print(sqrt(12))

# import everything 
from math import * 
# it is not recommended as it can create confusion and make it harder to understand where functions 
# are coming from 
# like you will use sqrt instead of math.sqrt() but ydk where it is coming from 

# import module name using an alias 
# used when module name is big or unconentional 
import numpy as np 

a = np.zeros((1,2))
print(a)

# The dir function 
print(dir(np))
# Gives the list of all the variables and functions in that module 

# you can create your own file and import functions from it too 
