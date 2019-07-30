4#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Mark Njoroge
Student Number: NJRMAR003
Prac: Prac 1
Date: 22/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools

values = list(itertools.product(range(2), repeat=3))    #creates list of outputs
output_list = [11,12,13]     #list of output pins
input_list = [35,36]	      #list of input pins
current = 0       #initialises current value in count

GPIO.setmode(GPIO.BOARD)
GPIO.setup(output_list,GPIO.OUT)		#sets up output pins
GPIO.setup(input_list,GPIO.IN,pull_up_down=GPIO.PUD_UP)			#sets up input pins

def LEDon():			#simple function that turns LED on and off
	GPIO.output(11, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(11, GPIO.LOW)
	time.sleep(1)


def callback_1(self):  			#callback function that subtracts from the value
	print("subtracted")
	global current
	if current == 0:
		current = 7
	else:
		current -= 1
	GPIO.output(output_list,values[current])


def callback_2(self):			#callback function that adds to the value
	print("added")
	global current
	if current == 7:
		current = 0
	else:
		current +=1
	GPIO.output(output_list,values[current])

GPIO.add_event_detect(35,GPIO.FALLING,callback=callback_1,bouncetime=300)	#detects when a button is pressed
GPIO.add_event_detect(36,GPIO.FALLING,callback=callback_2,bouncetime=300)


# Logic that you write
def main():
    print("write your logic here")

    time.sleep(10)
#    LEDon()

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.output(output_list,GPIO.LOW)
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
