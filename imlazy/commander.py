import subprocess


def run_command(command):
    pieces = command.split(' ')
    print("Running Command: {}".format(command))
    subprocess.run(pieces)
