import os
import re

REQUIREMENTS = os.getcwd() + '/requirements.txt'


def getDepends():
    requirements = open(REQUIREMENTS, 'r')
    libs = requirements.readlines()
    libList = []
    for lib in libs:
        try:
            name = re.search("^.+(?===)", lib).group(0)
            version = re.search("(?<===).+$", lib).group(0)
            libDict = {
                "name": name,
                "version": version
            }
            libList.append(libDict)
        except:
            continue
    return libList
