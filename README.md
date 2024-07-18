# PID-Controller-Simulation


PID controller is a name commonly given to a three-term controller. P stands for the proportional term, I for the integral term, and D for the derivative term in the controller [1]. PID controllers are probably the most widely used industrial controller. Even complex industrial control systems may comprise a control network whose main control building block is a PID control module [1].  

This repository contains a MATLAB application (GUI) as well as Python code that can be used as an educational tool to understand, visualize, and test the concept of PID controllers in a real-life example.  The application is inspired by the system built in [2]. In this tool, the PID controller will attempt to balance a green ball on a red moving bar. The position of the ball is measured, and the slope of the bar is modified (increased or decreased) in order to balance the green ball at a position defined by the user. 

## Matlab
In Matlab the simulation provided here, the user can control:  
  1. the initial position of the ball   
  2. the initial slope of the bar	  
  3. the desired position at which the ball should stop	  
  4. the PID controller’s gains, namely, Kp, Ki, and Kd gains that correspond to P, I, and D terms, respectively  
	

## Python

As for the Python code, first install the 'controller' package using:
```
python -m pip install -e  ".\PID-Controller-Simulation\Python"
```
Once installed, use the following command line to learn how to use the package:
```
python controller -h
```
You will get:
```
usage: python -m controller [-h] [-t TYPE] [-e EXAMPLE] [--kp KP] [--ki KI] [--kd KD]
                            [--final-position FINAL_POSITION] [-i ITERATIONS]

An example code:
python -m controller -t "PID" -e "ball"

options:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  The controller type.
  -e EXAMPLE, --example EXAMPLE
                        The example on which the controller is tested.
  --kp KP               Gain of the `propotion` part of the PID controller.
  --ki KI               Gain of the `integration` part of the PID controller.
  --kd KD               Gain of the `derivative` part of the PID controller.
  --final-position FINAL_POSITION
                        Ball`s final position when using the `ball` example. Choose values between -3 and 3.
  -i ITERATIONS, --iterations ITERATIONS
                        Maximum number of iterations before program stops.
```

Therefore, to use a PID controller to balance a ball, you can use the following command line:
```
python -m controller -t "PID" -e "ball" --kp 0.1 --ki 0.1 --kd 0.4 --final-position 0 -i 100                                                                                                                        
```

If you want to run the Python GUI, use the following command line:
```
python \controller\GUI.py
```

The repository also contains a '.exe' file (PID.exe) that can run the simulator directly. 


**Reference:**

[1] Crowe, J., Chen, G. R., Ferdous, R., Greenwood, D. R., Grimble, M. J., Huang, H. P., ... & Zhang, Y. (2005). PID control: new identification and design methods. Springer-Verlag London Limited.

[2] Electronoobs. (2019, July 20). PID Balance+Ball | full explanation & tuning [Video]. YouTube. https://www.youtube.com/watch?v=JFTJ2SS4xyA
