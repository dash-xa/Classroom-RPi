# classroom api
from classroom import *

# voice input
import time

def stdout(s):
	print(s)
def stdin(prompt = ''):
	return input(prompt)	

def main():
	global activeID

	stdout('hello sir')

	while True:
		text = stdin('how may I help you today?')
		if not text:
			return

		if 'course' in text:	
				# show list of courses	
				if 'show' in text or 'list' in text:
					stdout('here are your courses:')
					for c in getCourses():
						stdout(c['name'])
						time.sleep(1)
				elif 'create' in text or 'add' in text or 'make' in text:
						title = stdin('no problem, sir. What would you like to title this course?')
						desc = stdin('Phenomenal. Any comments?')
						createCourse(title, desc)
						stdout('course created, sir')
		
		# assignment related stuff
		elif 'assignment' in text:

			# make sure there is active course set
			if not activeID:
					name = stdin('Pardon me sir, in what course?')
					activeID = getCourseIDByName(name)

			# list all assignments
			if 'show' in text or 'list' in text:
				stdout('Ok sir, showing your assignments: ')
				for ass in getAssignments():
					stdout('title: ' + ass['title'] + '. description: ' + ass['description'])

			# display specific assignment's criteria
			elif 'criteria' in text or 'what' in text:
				assname = stdin('what assignment are you looking for?')
				ass = getAssByName(assname, activeID)
				stdout('here is the criteria for assignment titled: ' + assname)
				time.sleep(1)
				stdout('here is the description sir: ' + ass['description'])

			elif 'add' or 'create' in text:
				stdout('ok, making new assignment.')
				title = stdin('what would you like to title your new assignment, sir?')
				desc = stdin('Phenomenal. Would you like to add any comments?')
				createAssignment(title, desc, activeID)
				stdout('assignment created, sir')

		# set active course
		elif 'active' in text:
			name = stdin('Certainly, sir. What is your new active course?')
			activeID = getCourseIDByName(name)
			
activeID = None
main()
