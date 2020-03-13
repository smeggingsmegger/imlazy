#!/usr/bin/env python
import subprocess

try:
    import docker
except ImportError:
    subprocess.run(['pip', 'install', 'docker'])
    import docker

try:
    import PySimpleGUI as sg
except ImportError:
    subprocess.run(['pip', 'install', 'pysimplegui'])
    import PySimpleGUI as sg


sg.theme('DarkAmber')

# All the stuff inside your window.
layout = []

client = docker.from_env()
containers = [c.name for c in client.containers.list()]
for container in containers:
    layout.append([sg.Text(container)])

layout.append([sg.Button('Ok'), sg.Button('Cancel')])
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Running Docker Containers', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    # print('You entered ', values[0])

window.close()