# You may work on a project which uses different version of packages than the ones you 
# use on your default working environment 

# Virtual Environment - Allows you to create different working spaces on same machine 
# Allowing you to work on multiple projects with different dependencies and packages without conflict 

# Virtual environment basically installs python from your computer and then you can install packages 
# as per requirements 

# Type conda-V to check version of conda 

## Create a virtual environment 
# conda create -n envname python=x.x anaconda

## Activate the environment 
# conda activate envname 

## Install packages into environment 
# conda install -n yourenvname package
# you can install specific version of any package in virtual environment 

## Deactivate the virtual environment 
# conda deactivate 

## Delete Virtual Environment 
# conda remove -n envname -all

## Creating a yml file which contains all packages and dependency details 
# conda env export > environment.yml
# you can change yml file name 

## Create a New Environment from environment.yml
# conda env create -f environment.yml

## Update an Existing Environment from environment.yml
# conda env update -f environment.yml
# file name can vary , environment name will be one created from the yml file. 


# Also while deploying, server is set up with same environment as 
# the virtual environment for that project 


# When you activate a virtual environment, you are using those set of packages and not the 
# other ones on your machine
# A virtual environment has no relation to another virtual environment on machine 
