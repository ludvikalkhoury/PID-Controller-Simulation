## PID-Controller-MATLAB-Simulation


PID controller is a name commonly given to a three-term controller. P stands for the proportional term, I for the integral term, and D for the derivative term in the controller [1]. PID controllers are probably the most widely used industrial controller. Even complex industrial control systems may comprise a control network whose main control building block is a PID control module [1].  

In this repository, I will provide a MATLAB application (GUI) that can be used as an educational tool to understand, visualize, and test the concept of PID controllers in a real-life example.  The application is inspired by the system built in [^2]. In this tool, the PID controller will attempt to balance a green ball on a red moving bar. The position of the ball is measured, and the slope of the bar is modified (increased or decreased) in order to balance the green ball at a position defined by the user. 

In the simulation provided here, the user can control:  
  1. the initial position of the ball   
  2. the initial slope of the bar	  
  3. the desired position at which the ball should stop	  
  4. the PID controller’s gains, namely, Kp, Ki, and Kd gains that correspond to P, I, and D terms, respectively  
	
	

**Reference:**

[1] Crowe, J., Chen, G. R., Ferdous, R., Greenwood, D. R., Grimble, M. J., Huang, H. P., ... & Zhang, Y. (2005). PID control: new identification and design methods. Springer-Verlag London Limited.

[2] Electronoobs. (2019, July 20). PID Balance+Ball | full explanation & tuning [Video]. YouTube. https://www.youtube.com/watch?v=JFTJ2SS4xyA
