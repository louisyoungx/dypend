
# dypend  [![Visits][visits-badge]](github-page) [![Version][version-badge]][version-link] [![MIT License][license-badge]](LICENSE.md)

**dypend** Load dependent libraries dynamically.

A few days ago, I encountered many users feedback in an open source project. The Problem is they can not install the dependencies, such as execute `pip install -r requirements.txt` but nothing happened.

There are many problems like the wrong config of env that can cause this result and it's troublesome to check them one by one.

To solve this problem once and for all, we usually go to `site-packages` and put the required packages in the project root directory.

it's crude, not elegant.

So I wanted to load packages dynamically. if package do not exist, use `pip` to download them. 

I searched Google roughly, it seems no one have mention this method, and I feel it's convenient to use, so I share it.

> Although dypend is packaged for everyone to download, however that it depends on pip, which is against the intention of doing dynamic dependencies.
>
> So I recommend using the `Quick Start - Run by injecting code` approach

## Quick start

### Run by `pip install`

Download the `dypend`  package from `PyPI` .

```shell
pip install dypend
```

Freeze `requirements.txt`  file.

```shell
pip freeze > requirements.txt
```

import `dypend` at the top of the project's entry file, without changing any other code.

```python
import dypend
```

 ``dypend`` will check packages in ``requirements.txt`` is available or not in your Python environment, if not, ``dypend`` will call ``pip`` to download them.

### Run by injecting code

Freeze `requirements.txt`  file.

```shell
pip freeze >  requirements.txt
```

Add the following code to the top of the project's entry file, without changing any other code.

```python
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
def importLib():
    """Load python dependent libraries dynamically"""

    libList = getDepends()

    from pip._internal import main as pip_main
    import importlib

    def install(package):
        pip_main(['install', package])

    createVar = locals()

    for lib in libList:
        print(lib)
        try:
            createVar[lib["name"]] = importlib.import_module(lib["name"])
        except Exception as e:
            try:
                install(f'{lib["name"]}=={lib["version"]}')
                createVar[lib["name"]] = importlib.import_module(lib["name"])
            except Exception as e:
                print(e)
importLib
```

 ``dypend`` will check packages in ``requirements.txt`` is available or not in your Python environment, if not, ``dypend`` will call ``pip`` to download them.
 

[github-page]: https://github.com/louisyoungx/dypend
[version-badge]: https://img.shields.io/pypi/v/dypend.svg?label=version
[version-link]: https://pypi.python.org/pypi/dypend/
[license-badge]: https://img.shields.io/badge/license-MIT-007EC7.svg
[visits-badge]: https://badges.pufler.dev/visits/louisyoungx/dypend
