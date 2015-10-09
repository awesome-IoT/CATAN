#!/usr/bin/env python

# Native
import os
from distutils.core import setup

# CATAN
import catan.globals as G

def get_packages(rel_dir):

    packages = [rel_dir]
    for x in os.walk(rel_dir):
        # break into parts
        base = list(os.path.split(x[0]))
        if base[0] == "":
            del base[0]

        for mod_name in x[1]:
            packages.append( ".".join(base + [mod_name]) )

    return packages

def get_data_files(rel_dir):
    """
        Get a list of data files to include in install package
    """
    install_list = []
    for x in os.walk(rel_dir):
        directory = x[0]
        install_files = []
        
        # Get all the .py files
        for filename in x[2]:
            if not filename.endswith(".pyc"):
                install_files.append( os.path.join(directory, filename) )
        
        if len(install_files) > 0:
            install_path = os.path.join(G.DIR_ROOT,directory)
            install_list.append( (install_path, install_files) )
        
    
    return install_list

data_files = []
data_files += get_data_files(G.DIR_EXAMPLES)
data_files += get_data_files(G.DIR_CONF)
data_files += get_data_files(G.DIR_BINARIES)
data_files += get_data_files(G.DIR_SCRIPTS)
# Web stuff
data_files += get_data_files("webserver")


setup(name='CATAN',
      version='1.0',
      description='This package contains all of the communication libraries for CATAN.',
      author='Chad Spensky',
      author_email='chad.spensky@ll.mit.edu',
      url='N/A',
      data_files = data_files,
      packages=get_packages('catan'),
     )
