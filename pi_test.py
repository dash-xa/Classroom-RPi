#!/usr/bin/env python3
"""
Shows basic usage of the Classroom API.

Creates a Classroom API service object and prints the names of the first
10 courses the user has access to.
"""

# classroom api
from classroom import *

# voice input
import logging
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import time

	
def stdout(s):
	aiy.audio.say(s)

def stdin(assistant, prompt = ''):
	stdout(prompt)
	status_ui.status('ready')
	print('waiting for press')
	status_ui.status('listening')
#	return assistant.recognize()[0]
	return input('please enter an input.')

def main():
	stdout('hello sir')
	global activeID
	with aiy.audio.get_recorder():
		while True:
			text = stdin(assistant, 'hello sir, how may I help you today')
			if not text:
				return

			stdout('okay, I heard' + text)
			
			if 'course' in text:	
					# show list of courses	
					if 'show' in text or 'list' in text:
						stdout('here are your courses:')
						for c in getCourses():
							stdout(c['name'])
							time.sleep(1)
					elif 'create' in text or 'add' in text or 'make' in text:
							title = stdin(assistant, 'no problem, sir. What would you like to title this course?')
							desc = stdin(assistant, 'Phenomenal. Any comments?')
							createCourse(title, desc)
							stdout('course created, sir')
			
			# assignment related stuff
			elif 'assignment' in text:

				# make sure there is active course set
				if not activeID:
					name = stdin(assistant, 'Pardon me sir, in what course?')
					activeID = getCourseIDByName(name)

				# list all assignments
				if 'show' in text or 'list' in text:
					stdout('Ok sir, showing your assignments: ')
					for ass in getAssignments():
						stdout('title: ' + ass['title'] + '. description: ' + ass['description'])

				# display specific assignment's criteria
				elif 'criteria' in text or 'what' in text:
					assname = stdin(assistant, 'what assignment are you looking for?')
					ass = getAssByName(assname, activeID)
					stdout('here is the criteria for assignment titled: ' + assname)
					time.sleep(1)
					stdout('here is the description sir: ' + ass['description'])

				elif 'add' or 'create' in text:
					stdout('ok, making new assignment.')
					title = stdin(assistant, 'what would you like to title your new assignment, sir?')
					desc = stdin(assistant, 'Phenomenal. Would you like to add any comments?')
					createAssignment(title, desc, activeID)
					stdout('assignment created, sir')

			# set active course
			elif 'active' in text:
				name = stdin(assistant, 'Certainly, sir. What is your new active course?')
				activeID = getCourseIDByName(name)
					
			
# get assistant stuffs
activeID = None
status_ui = aiy.voicehat.get_status_ui()
assistant = aiy.assistant.grpc.get_assistant()
button = aiy.voicehat.get_button()
if __name__ == '__main__':
	main()
