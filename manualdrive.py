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
    
    
    
print_menu()
print( "\nPlease drive safely")
#camera = PiCamera()
#camera.rotation = 180

while True:

    
    a = getch()
    print('You pressed:', a)
    
    if a=='w':
        fwd();  #time.sleep(.500); stop()
    elif a=='a':
        left(); #time.sleep(.500); stop()
    elif a=='c':
        camera.start_preview()
    elif a=='v':
        camera.stop_preview()
    elif a=='d':
        right(); #   time.sleep(.500); stop()
    elif a=='s':
        bwd(); # time.sleep(.500); stop()
    elif a=='x':
        stop()
    elif a=='t':
        increase_speed()
    elif a=='g':
        decrease_speed()
    elif a=='v':
        print( "{}V".format(volt()))
    elif a=='z':
        sys.exit()
    elif a=='i':
        motor_fwd()
    elif a=='k':
        motor_bwd()
    elif a=='n':
        left_rot()
    elif a=='m':
        right_rot()
    elif a =='u':
	print( '{}cm'.format(us_dist(15)))
    elif a=='f': #servo test
        for i in range(90):
            servo(i)
            print( i)
            time.sleep(.02)
    elif a=='b': #servo test
        for i in range(180):
            servo(i)
            print( i)
            time.sleep(.02)
    #elif a=='y':
        #camera.exposure_mode = 'night'
    #elif a=='u':
        #camera.exposure_mode = 'auto' 

    time.sleep(.1)




