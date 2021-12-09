from .getDepends import getDepends


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
