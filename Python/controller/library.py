import pickle
import time 

import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style
from tqdm import tqdm




class controller:
	Version = '1.0.0'  # @VERSION_INFO@
	
	def __init__(self, 	type 		= None,
						example 	= None,
						iterations  = None):
		self.type		= type
		self.example	= example
		self.iterations = iterations
		


	def Copy(self):
		c = copy.deepcopy( self )
		print(Fore.BLUE + 'Object copied!')
		return c
		

	def Run(self, **kwargs):
		if self.type.lower() == 'pid':
			
			if self.example.lower() == 'ball':
				self.PID(**kwargs)
			else:
				print('Other examples are not supported at this moment')
				
		else:
			print('Other controller types are not supported at this moment')



		return self
			
			


	def PID(self, kp=0.1, ki=0.18, kd=0.45, Ball_Final_Pos=0):
		
		print(Ball_Final_Pos)
		alpha = 1*+20

		m = []; m.append( np.tan( np.deg2rad (alpha) ) );

		b = 0
		l = 5
		Ball_r = 0.2
		Init_ = 4


		x = np.arange(-l*np.cos(np.arctan ( np.deg2rad(m))), l*np.cos(np.arctan ( np.deg2rad(m))), 0.01)
		y = m*x + b
		
		Ball_posX = []
		Ball_posX.append( Init_ )
		Ball_posY = m[-1]*Ball_posX[-1] + (b+Ball_r);




		m.append(m[-1]); m.append(m[-1]); 

		Ball_posX.append( Ball_posX[-1] );  Ball_posX.append( Ball_posX[-1] );  Ball_posX.append( Ball_posX[-1] ); 
		Error = []; Error.append( Ball_Final_Pos - Ball_posX[-1] );
		Error.append( Error[-1] ), Error.append( Error[-1] )
		
		Mv_Error = []	
		Mv_Error.append(np.nan), Mv_Error.append(np.nan), Mv_Error.append(np.nan)			
		mvpts = 10
		

		
		plt.figure(figsize=(3, 6))		
		curr_it = 1
		while(Ball_posX[-1] >-l*np.cos( np.deg2rad(alpha) ) and Ball_posX[-1] < l*np.cos( np.deg2rad(alpha) )) and curr_it < self.iterations:
			plt.clf()
		
			x = np.arange(-l*np.cos(np.arctan (m[-1])), l*np.cos(np.arctan (m[-1])), 0.01)
			y = m[-1]*x + b;
			
			plt.subplot(2,1,1)
			plt.plot(x, y, 'r', 'LineWidth', 2)
			plt.plot([-5, 5],[0, 0],'k:')
			plt.plot([0, 0],[-5, 5],'k:')
			th = np.arange(0, 2*np.pi, 0.1)
			xunit = l * np.cos(th) ;
			yunit = l * np.sin(th) ;
			plt.plot(xunit, yunit,'b.')
			plt.plot(Ball_posX[-1], Ball_posY, 'go')
			for i in [-4,-3,-2,-1,0,1,2,3,4]:
				plt.plot([i,i], [-0.2,0.2], color='k', linewidth=1)
				plt.text(i-0.2, -0.7, str(i), color='k', fontsize=7)
			
			plt.yticks([])
			plt.title('PID Controller')
			
			#NanList = [np.nan]*mvpts
			#Mv_Error = NanList + Mv_Error

			
			plt.subplot(2,1,2)
			plt.plot(Error,  'g')
			plt.plot([0,len(Error)], [0, 0],    'k:')
			#plt.plot(Mv_Error, 'k')
			plt.ylim([-5, 5])
			plt.xlabel('Iterations')
			plt.title('Ball`s position error')

			


			Error.append( Ball_posX[-1] - Ball_Final_Pos )
			
			P2 = kp*Error[-1]
			I2 = ki*np.cumsum(Error)/len(Error)
			D2 = kd*(Error[-1] - Error[-2])
			m_up = m[-1] + (P2 + D2 + I2[-1])
			
			
			
			"""
			if len(Mv_Error) > mvpts:
				Mv_Error = movmean( Error , mvpts).tolist()
			else:

				Mv_Error.append(np.nan)
			
			"""



			
			
			if m_up > 0.5:
				m_up = 0.5;
			elif m_up < -0.5:
				m_up = -0.5;
			
			
			if m[-1] > 0.001:
				Ball_posX[-1] = Ball_posX[-1] - 3*m[-1]**2;
			elif m[-1] < -0.001:
				Ball_posX[-1] = Ball_posX[-1] + 3*m[-1]**2;
			else:
				Ball_posX[-1] = Ball_posX[-1];
		
			
			
			m.append(m_up)
			Ball_posX.append(Ball_posX[-1]) 

			Ball_posY = m[-1]*Ball_posX[-1] + b + Ball_r
			
			
			
			plt.show(block=False)
			plt.pause(0.05)
			curr_it = curr_it + 1
		
		else:
			plt.show()


		
		return self
		





def movmean(data, window_size):
    cumsum = np.cumsum(np.insert(data, 0, 0)) 
    return (cumsum[window_size:] - cumsum[:-window_size]) / window_size






