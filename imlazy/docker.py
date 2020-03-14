import subprocess


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