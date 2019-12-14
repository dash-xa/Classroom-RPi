
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

TEST_ID = "14801393984"
T = ''
# returns list of dictionaries (assignment)
def getAssignments(i = TEST_ID):
	return service.courses().courseWork().list(courseId = i).execute()['courseWork']
def createAssignment(title, desc,id):
	courseWork = {
		'title': title,  
		'description': desc,  
		'materials': [  
		{'link': { 'url': 'http://example.com/ant-colonies' }},  
		{'link': { 'url': 'http://example.com/ant-quiz' }}  
		],  
		'workType': 'ASSIGNMENT',  
		'state': 'PUBLISHED',
		}
	courseWork = service.courses().courseWork().create(courseId = id, body=courseWork).execute()
	return courseWork
	# show assignment ID
	#print('Assignment created with ID {0}'.format(courseWork.get('id')))
def getCourses():
	# service = getService()
	results = service.courses().list(pageSize=10).execute()
	courses = results.get('courses', [])	
	# return getService().courses().list(pageSize = 10).execute().get('courses', [])
	return courses

def getCourseIDByName(name):
	for c in courses:
		if name.lower() in c['name'].lower():
			return c['id']
	return None

def getCourseByName(name):
	for c in courses:
		if name in c['name']:
			return c
	return None

def getAssByName(name, id):
	for ass in getAssignments(id):
		if name in ass['title']:
			return ass
	return None

def createCourse(title, desc):
	course = {
    'name': title,
    'section': '',
    'descriptionHeading': '',
    'description': desc,
    'room': '',
    'ownerId': 'me',
    'courseState': 'PROVISIONED'
	}
	service.courses().create(body=course).execute()
	return course


# Setup the Classroom API
SCOPES = 'https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.coursework.students'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
	flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
	creds = tools.run_flow(flow, store)
service =  build('classroom', 'v1', http=creds.authorize(Http()))
courses = getCourses()

# Call the Classroom API
# courses
# createAssignment('testAssignment', 'this is a test description')
# for ass in getAssignments():
# 	print('title: ' + ass['title'] + ' description: ' + ass['description'])