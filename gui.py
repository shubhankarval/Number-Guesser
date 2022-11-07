'''
Copyright (c) 2022, Shubhankar Valimbe
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

'''

import PySimpleGUI as sg
from app import *

# All the stuff inside your window.

#enter range layout
layout1 = [  [sg.Text('Enter Number Range')],
            [sg.Text('From'), sg.Input(size=(11,1),do_not_clear=False),sg.Text('To'), sg.Input(size=(11,1),do_not_clear=False)],
            [sg.Button('Ok', key='range')] ]

#guessing layout
layout2 = [ [sg.Text('Guesses Left:'),sg.Text('',key='guessNum')],
            [sg.Text('Input Number:'),sg.Input(key="num",do_not_clear=False, size=(25,1))],
            [sg.Push(),sg.Button('Ok',key='guess'),sg.Push()],
            [sg.Text('',key='msg')]]

#final message layout
layout3 = [[sg.Text('', key='finalMsg')],
            [sg.Push(), sg.Button('Play Again', key='again'), sg.Push(), sg.Button('Exit'),sg.Push()]]

# base layout
layout = [  [sg.Column(layout1, key='-COL1-',element_justification='c'), 
            sg.Column(layout2, visible=False, key='-COL2-'), 
            sg.Column(layout3, visible=False, key='-COL3-')],
          ]

# Create the Window
window = sg.Window('Number Guesser', layout)
# Event Loop to process "events" and get the "values" of the inputs

guessLeft = -1
num = -1
col1, col2, col3 = window['-COL1-'], window['-COL2-'], window['-COL3-']

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event=="Exit": # if user closes window or clicks Exit
        break 

    elif event=='range':
        a,b = int(values[0]), int(values[1]) #getting range
        guessLeft = numGuess(a,b) 
        num = generateRandomInt(a,b)
        window['guessNum'].update(guessLeft)
        col1.update(visible=False)
        col2.update(visible=True)
    
    elif event == "guess":
        guessLeft-=1
        if guessLeft==0:
            if num==int(values['num']):
                window['finalMsg'].update("Congratulations! You guessed it right.")
            else:
                window['finalMsg'].update(f"The number was {num}. Better Luck Next Time!")
            col2.update(visible=False)
            col3.update(visible=True)

        else:
            window['guessNum'].update(guessLeft)
            if int(values['num']) > num:
                window['msg'].update("Try Again! Your guess was too high.")
            
            elif int(values['num']) < num:
                window['msg'].update("Try Again! Your guess was too low.")
            
            else:
                window['finalMsg'].update("Congratulations! You guessed it right.")
                col2.update(visible=False)
                col3.update(visible=True)
        
    elif event=="again":
        col3.update(visible=False)
        col1.update(visible=True)

    # print('You entered ', event , values)

window.close()