import subprocess


def norestart_container(which):
    command = 'docker update --restart=no {}'.format(which)
    pieces = command.split(' ')
    print("Setting {} to not restart...".format(which))
    subprocess.run(pieces)
    print("Updated {}.".format(which))


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
    print("rm'ing {}...".format(which))
    subprocess.run(pieces)
    print("rm'ed {}.".format(which))


def docker_compose(which='local.yml', command='up'):
    command = 'docker-compose -f {} {}'.format(which, command)
    pieces = command.split(' ')
    print("Running {}...".format(which))
    subprocess.run(pieces)
    print("Ran {}.".format(which))

