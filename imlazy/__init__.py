import importlib
import pip
import subprocess

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


def stop_container(which):
    command = 'docker stop {}'.format(which)
    pieces = command.split(' ')
    print("Stopping {}...".format(which))
    subprocess.run(pieces)
    print("Stopped {}.".format(which))


def run_container(which):
    command = 'docker exec -it {} bash'.format(which)
    pieces = command.split(' ')
    print("Entering {}...".format(which))
    subprocess.run(pieces)
    print("Exiting {}...".format(which))


def rm_container(which):
    command = 'docker rm {}'.format(which)
    pieces = command.split(' ')
    print("rmping {}...".format(which))
    subprocess.run(pieces)
    print("rmped {}.".format(which))