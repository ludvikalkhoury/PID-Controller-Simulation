"""
An example code:
python -m controller -t "PID" -e "ball"

"""

import argparse
import warnings
import os


parser1 = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter, prog='python -m pyX')


parser1.add_argument( "-t", "--type", default='PID', type=str, help='The controller type.')
parser1.add_argument( "-e", "--example", default='ball', type=str, help='The example on which the controller is tested.')

parser1.add_argument( "--kp", default=0.1,  type=float, help='Gain of the `propotion` part of the PID controller.')
parser1.add_argument( "--ki", default=0.18, type=float, help='Gain of the `integration` part of the PID controller.')
parser1.add_argument( "--kd", default=0.45, type=float, help='Gain of the `derivative` part of the PID controller.')
parser1.add_argument( "--final-position", default=0, type=int, help='Ball`s final position when using the `ball` example. Choose values between -3 and 3.')

parser1.add_argument( '-i', "--iterations", default=50, type=int, help='Maximum number of iterations before program stops.')

OPTS1 = parser1.parse_args()

import numpy as np
import mne 
from controller.library import controller


myController = controller(	type=OPTS1.type, 
							example=OPTS1.example, 
							iterations=OPTS1.iterations )

myController.Run( kp=OPTS1.kp, ki=OPTS1.ki, kd=OPTS1.kd, Ball_Final_Pos = OPTS1.final_position)




