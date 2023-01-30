"""
In order to accomplish the assignment, the robot will look 
for tokens in front of it and grab the nearest one.
Once the robot has grabbed the silver token, it will look for 
a gold token in front of it, move near it, and release the 
silver token once it is close enough.
Silver tokens will be placed next to gold tokens until every 
silver token is next to a different gold token.

"""


#import libraries
from __future__ import print_function # for print()
import time # for time.sleep()
import os # for clearing the screen
from sr.robot import * # for robot object


# define global variables
R = Robot() # robot object
my_time = .5 # turn and drive time
my_speed = 25 # turn and drive speed
angle_th = 4.0 # angle threshold
distance_th = 0.4 # distance threshold
silver_token_list = [] # array to store the code of collected silver tokens
gold_token_list = [] # array to store the code of gold tokeens


# drive the robot forward/backwards
def drive(speed, seconds):
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0

# turn the robot left/right
def turn(speed, seconds):
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = -speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0





# interface function
# this function prints the robot's interface
# it takes a command as input and prints the corresponding message
def interface(command):
	os.system('clear')
	print('###################################################################')
	print("##                         Robot's interface                     ##")
	print('###################################################################\n\n')

	if command is "start":
		print('Lets put sliver tokens next to the gold tokens')
		time.sleep(2)

	if command is "notoken":
		print('Ops there is no token in my range!!!')

	elif command is "goldtoken":
		print('I found a gold token')

	elif command is "nogoldtoken":
		print('ther is no gold token in my range!!!')

	elif command is "deliver":
		print('I am delivering the silver token next to the gold token')

	elif command is "silvertoken":
		print('I found a silver token')

	elif command is "nosilvertoken":
		print('Ops there is no silver token in my range!!!')

	elif command is "grab":
		print('I grabbed the silver token \nLets deliver it to a gold token')

	elif command is "release":
		print('Yes.. I put the silver token next to the gold token')

	elif command is "problem":
		print('Ops there is a problem, I cannot grab the token!!!')

	elif command is "left":
		print("I am turning left a bit")

	elif command is "right":
		print("I am turning right a bit")

	elif command is "finish":
		print("I delivered silver all tokens successfully!!!")





# grab_silver_tokens function takes the number of silver tokens as input
# then locate a silver token, grab it and deliver it to a gold token
def grab_silver_tokens(n_tokens):

	grab_flag = False
	token_code = -1


	# while loop runs until all tokens have been collected
	while n_tokens > 0:

		# if a silver token has not been grabbed yet, search for one
		if not grab_flag:
			# search for a silver token
			distance, rotation_y, token_code = search_token(MARKER_TOKEN_SILVER, silver_token_list)
			# while loop runs until a silver token is found by turning and moving the robot
			while distance == -1 or token_code == -1:
				turn(my_speed, my_time)
				drive(my_speed, my_time)
				distance, rotation_y, token_code = search_token(MARKER_TOKEN_SILVER, silver_token_list)
				if token_code != -1:
					# if a silver token is found, print the interface 
					interface("silvertoken")
				else:
					# if no silver token is found, print the interface
					interface("nosilvertoken")
				time.sleep(1)
				
		else:
			distance, rotation_y = refresh_position(MARKER_TOKEN_SILVER,token_code)

		grab_flag = True

		# Grab the silver token and deliver it to the gold token if it is close enough
		if distance < distance_th:
			if R.grab():

				interface("grab")
				drive(-my_speed, my_time)
				turn(my_speed, my_time)
				go_to_gold(token_code) # search for a gold token and deliver the silver token to it
				n_tokens -= 1
				drive(-my_speed, my_time)
				turn(my_speed, my_time)
				grab_flag = False

			else:
				interface("problem")
				exit()
		# if the silver token is not close enough, move the robot towards it
		# and turn it to face the silver token		
		elif rotation_y < -angle_th:
			interface("left")
			turn(-1.5, my_time)
		elif rotation_y > angle_th:
			interface("right")
			turn(1.5, my_time)
		else:
			drive(my_speed, my_time)


# token_type: type of the token to be searched for
# token_list: list of tokens that have already been marked
# return: distance, angle and code of the nearest token
# This function finds unmarked tokens and returns their distance, angle, and code
def search_token(token_type, token_list):
	distance = 100
	rotation_y = 0
	token_code = -1

	for token in R.see():
		# if the token is unmarked and in the range of the robot, update the distance, angle and code of token
		if (token.dist < distance) and (token.info.marker_type is token_type) and (token.info.code not in token_list):
			distance = token.dist
			token_code = token.info.code
			rotation_y = token.rot_y

	# if no token is found, return -1, -1, -1
	if distance >= 100:
		interface("notoken")
		return -1, -1, token_code
	else:
		# if a token is found, return its distance, angle and code
		return distance, rotation_y, token_code




# token_type: type of the token to be searched for
# target_code: code of the token to be searched for
# return: distance and angle of the token
# This function finds the token with the given code and returns its distance and angle
def refresh_position(token_type,target_code):
	for token in R.see():
		if (token.info.code == target_code) and (token.info.marker_type is token_type):
			return token.dist, token.rot_y
		
	return -1, -1



# token_code: code of the silver token
# This function finds a gold token and delivers the silver token to it
# if no gold token is found, the robot turns and moves until one is found
def go_to_gold(token_code):
	gold_token = False
	find_gold_flag = False
	gold_token_code = -1

	# while loop runs until the silver token is delivered to a gold token
	while not gold_token:
		if not find_gold_flag:
			distance, rotation_y, gold_token_code = search_token(MARKER_TOKEN_GOLD, gold_token_list)

			# while loop runs until a gold token is found by turning and moving the robot
			while distance == -1 or gold_token_code == -1:
				turn(my_speed, my_time)
				drive(my_speed, my_time)
				distance, rotation_y, gold_token_code = search_token(MARKER_TOKEN_GOLD, gold_token_list)
				if gold_token_code != -1:
					# if a gold token is found, print the interface
					interface("goldtoken")
				else:
					# if no gold token is found, print the interface
					interface("nogoldtoken")
				time.sleep(1)
		else:
			# if a gold token is found, print the interface
			# and refresh the position of the gold token
			# to make sure the robot is still facing it
			interface("deliver")
			distance, rotation_y = refresh_position(MARKER_TOKEN_GOLD,gold_token_code)

		find_gold_flag = True

		#if the gold token is close enough, release the silver token and save them in their list 
		if distance < distance_th * 1.5:
			gold_token = True
			
			#this function releases the token
			R.release()
			interface("release")

			#marks the moved silver token and visited gold token
			silver_token_list.append(token_code)
			gold_token_list.append(gold_token_code)
			find_gold_flag = False

		# if the gold token is not close enough, move the robot towards it
		# and turn it to face the gold token
		elif rotation_y < -angle_th:
			interface("left")
			turn(-2, my_time)
		elif rotation_y > angle_th:
			interface("right")
			turn(2, my_time)

		# if the robot is facing the gold token, move it towards it
		else:
			drive(25, my_time)


interface("start")
# This function is used to grab all 6 silver tokens and deliver them to the gold token
grab_silver_tokens(6)
interface("finish")