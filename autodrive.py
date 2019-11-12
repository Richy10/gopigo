#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
from builtins import input

'''
## License
 GoPiGo for the Raspberry Pi: an open source robotics platform for the Raspberry Pi.
 Copyright (C) 2017  Dexter Industries
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''

from gopigo import *
import sys
from getch import getch,pause 
import atexit
from picamera import PiCamera
from time import sleep
atexit.register(stop)

def print_menu():
    print( "  w :   Move the GoPiGo forward")
    print( "  a :   Turn the GoPiGo left")
    print( "  s :   Move the GoPiGo back")
    print( "  d :   Turn the GoPiGo right")
    print( "  n :   Rotate the GoPiGo left in place")
    print( "  m :   Rotate the GoPiGo right in place")
    print( "  x :   Stop the GoPiGo")
    print( "  t :   Increase the speed by 10 (default 200, min:0 max 255)")
    print( "  g :   Reduce the speed by 10")
    print( "  v :   Print the voltage of the batteries (should be greater than 10)")
    print( "  c :   Start Cam")
    print( "  v :   Stop Cam")
    print( "  f :   Point camera forward")
    print( "  b :   180' Scan")
    print( "  y :   Nightmode")
    print( "  u :   Auto exposure")
    
    
    
#print_menu()
print("\n Turning on the systems");
time.sleep(.2);
print(".");
time.sleep(.2);
print(".");
time.sleep(.2);
print(".");
print( "\nSystems Online ...");
time.sleep(.2);
print("Initializing Toretto.exe");

#camera = PiCamera()
#camera.rotation = 180
sensor_pos = 90; #the position of the servo to point forward 
rotation_var = 10; #Span 10 degrees at the time 
rotation_flag = 0; #Did it rotate or did it do reverse?
flag = 0;          #Value of how long it turned, to calculate how much to turn the wheels
value_before_impact = 30; #How long before it stops when it detects a wall
sleep_time = .1;    
servo(90);  #Point the servo forward
#set_left_speed(163)
#set_right_speed(123)
#fwd();
while True:

#change the speed according to your motor needs
#to balance / make it go straight

	set_left_speed(153)
	set_right_speed(123)
	#elif a=='u':
	#	print( '{}cm'.format(us_dist(15)))

	if us_dist(15) > value_before_impact:
		fwd();
	
	#print( '{}cm'.format(us_dist(15)))
    #main loops, scans 10 to the left, then 20 to the right, then 30 to the left ...
    #if it doesnt find a clear path it goes back and turns to the left 
	if us_dist(15) < value_before_impact:
		
		stop();
		flag = sensor_pos+rotation_var;
		time.sleep(sleep_time)
		servo(flag);
		if us_dist(15) < value_before_impact:
			flag = sensor_pos-rotation_var*2;
			servo(flag);
			time.sleep(sleep_time)
			if us_dist(15) < value_before_impact:
				flag = sensor_pos+rotation_var*3;
				servo(flag);
				time.sleep(sleep_time)
				if us_dist(15) < value_before_impact:
					flag = sensor_pos-rotation_var*4;
					servo(flag);
					time.sleep(sleep_time)
					if us_dist(15) < value_before_impact:
						flag = sensor_pos+rotation_var*5;
						servo(flag);
						time.sleep(sleep_time)
						if us_dist(15) < value_before_impact:
							flag = sensor_pos-rotation_var*6;
							servo(flag);
							time.sleep(sleep_time)
							if us_dist(15) < value_before_impact:
								flag = sensor_pos+rotation_var*7;
								servo(flag);
								time.sleep(sleep_time)
								if us_dist(15) < value_before_impact:
									flag = sensor_pos-rotation_var*8;
									servo(flag);
									time.sleep(sleep_time)
									if us_dist(15) < value_before_impact:
										flag = sensor_pos+rotation_var*9;
										servo(flag);
										time.sleep(sleep_time)
										if us_dist(15) < value_before_impact:
											flag = sensor_pos-rotation_var*10;
											servo(flag);
											time.sleep(sleep_time)
											if us_dist(15) < value_before_impact:
												flag = sensor_pos+rotation_var*11;
												servo(flag);
												time.sleep(sleep_time)
												if us_dist(15) < value_before_impact:
													flag = sensor_pos-rotation_var*12;
													servo(flag);
													time.sleep(sleep_time)
													if us_dist(15) < value_before_impact:
														flag = sensor_pos+rotation_var*13;
														servo(flag);
														time.sleep(sleep_time)
														if us_dist(15) < value_before_impact:
															flag = sensor_pos-rotation_var*14;
															servo(flag);
															
															if us_dist(15) < value_before_impact:
																bwd();
																time.sleep(1.5)
																turn_left(90);
																rotation_flag = 1;
																time.sleep(1.5)
		if rotation_flag == 0:
			if flag > 91:
				flag = flag - 90;
				turn_left(flag);
				time.sleep(.5)
			
			else:
				flag = 90 - flag;
				turn_right(flag);
				time.sleep(.5)


		else:
			rotation_flag = 0;
			
		servo(90);
		time.sleep(sleep_time)
		time.sleep(sleep_time)

		#fwd();
		
	# a = getch()
	# print('You pressed:', a)
	
	# if a=='w':
		# fwd();  #time.sleep(.500); stop()
	# elif a=='a':
		# left(); #time.sleep(.500); stop()
	# elif a=='c':
		# camera.start_preview()
	# elif a=='v':
		# camera.stop_preview()
	# elif a=='d':
		# right(); #   time.sleep(.500); stop()
	# elif a=='s':
		# bwd(); # time.sleep(.500); stop()
	# elif a=='x':
		# stop()
	# elif a=='t':
		# increase_speed()
	# elif a=='g':
		# decrease_speed()
	# elif a=='v':
		# print( "{}V".format(volt()))
	# elif a=='z':
		# sys.exit()
	# elif a=='i':
		# motor_fwd()
	# elif a=='k':
		# motor_bwd()
	# elif a=='n':
		# left_rot()
	# elif a=='m':
		# right_rot()
	# elif a=='f': #servo test
		# for i in range(90):
			# servo(i)
			# print( i)
			# time.sleep(sleep_time)
	# elif a=='b': #servo test
		# for i in range(180):
			# servo(i)
			# print( i)
			# time.sleep(sleep_time)
	#elif a=='y':
		#camera.exposure_mode = 'night'
	#elif a=='u':
		#camera.exposure_mode = 'auto' 

	time.sleep(.1)





