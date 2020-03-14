import importlib
import pip

if int(pip.__version__.split('.')[0])>9:
    from pip._internal import main
else:
    from pip import main


def install(package):
    main(['install', package])


def import_package(pkgname):
    pkg = importlib.import_module(pkgname)
    return pkg
    

def import_or_install(pkgname):
    try:
        return import_package(pkgname)
    except ImportError:
        try:
            main(["install", "--user", pkgname])
            return import_package(pkgname)
        except SystemExit as e:
            print("Couldn't install {}".format(pkgname))
            raise e
