from sys import path
from os.path import dirname, realpath, join, exists
from os import mkdir

__version__ = '1.0.0'

PATH_DIRETORIO = realpath(dirname(__file__))
path.insert(0, PATH_DIRETORIO)

PATH_ARQUIVOS = join(PATH_DIRETORIO,'arquivos')

if not exists(PATH_ARQUIVOS):
    mkdir(PATH_ARQUIVOS)


