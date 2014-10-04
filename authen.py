import pprint
from linkedin import linkedin # pip install python-linkedin
# Define CONSUMER_KEY, CONSUMER_SECRET,
# USER_TOKEN, and USER_SECRET from the credentials
# provided in your LinkedIn application
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
USER_TOKEN = ''
USER_SECRET = ''
RETURN_URL = 'http://localhost:3000' # Not required for developer authentication
# Instantiate the developer authentication class
auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())
app = linkedin.LinkedInApplication(auth) # Use the app...
app.get_profile()

pp = pprint.PrettyPrinter(indent=1)

print app.get_profile()

profile_data = app.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'connections' ,'num-connections', 'skills', 'educations'])

location = profile_data['location']
city = location['name']

##pp.pprint(profile_data)
connections = profile_data['connections']
values = connections['values']

for value in values:
	##pp.pprint(value)
	print "----- "
	print " "
	firstN = value['firstName']
	lastN = value['lastName']
	defaultVal = 'On Earth :-)'
	place = value.get('location',defaultVal)
	if place == defaultVal:
		continue
	city2 = place['name']
	print firstN + " " + lastN 
	print city2

##pp.pprint(values)


print city


print " "
print " --------------------------- "
print "Company Info"
updates = app.get_company_updates(1035, params={'count': 2})

print type(updates)
pp.pprint(updates)


	
