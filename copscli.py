import click
import okta_common as oc
import requests

# Okta preview settings
# secret_name = "okta_preview"
# secret_key = "api_key"

# Okta Production settings
secret_name = "Okta_Production"        
secret_key = "Okta_Prd"

region_name = "us-west-2"
try:
	secret = oc.get_secret(secret_name, region_name)[secret_key]
except UnboundLocalError:
	print('Set the credentials before using copscli..')
	exit(0)
except:
	print('Set the credentials before using copscli..')
	exit(0)

@click.group()
def operations():
	"""Commands for instances"""
	
@operations.command('listGroups')
@click.option('--prefix', default = '', help="Group name starts with")
@click.option('--suffix', default = '', help="Group name ends with")
@click.option('--anywhere', default = '', help="Any string in the group name")

def list_groups(prefix, suffix, anywhere):
	"List Okta groups"
	groups = oc.list_okta_groups(secret)
	print("\n        Group Name")
	print("------------------------------------------")
	for group in groups:
		group_name = group['group_name']
		if group_name.startswith(prefix) and group_name.endswith(suffix) and anywhere.lower() in group_name.lower():
			print(f"{group['group_name']}")

@operations.command('listGroupMembers')
@click.option('--groupname', default = '', help="Group name")
def list_group_members(groupname):
	"List Okta group Members"
	if groupname:
		try:
			group_members = oc.list_group_members(groupname, secret)
		except requests.exceptions.HTTPError:
			print("Group doesn't exists")
		else:
			print("\n        Group Members")
			print("------------------------------------------")
			for group_member in group_members:
				print(group_member)
	else:
		print('Provide groupname')

@operations.command('listUsers')
@click.option('--login', default = '', help="user login")
def list_users(login):
	"List Okta Users"
	users = oc.list_users(secret)
	print("\n            User Login                   Status         Created                Activated                LastLogin")
	print("--------------------------------------------------------------------------------------------------------------------")
	if login:
		for user in users:
			if login.lower() in user['profile']['login'].lower():
				print(user['profile']['login'].rjust(35, ' '), user['status'].rjust(12,' '), user['created'], user['activated'], user['lastLogin'])
	else:
		for user in users:
			print(user['profile']['login'].rjust(35, ' '), user['status'].rjust(12,' '), user['created'], user['activated'], user['lastLogin'])
#			print(user)

@operations.command('listApps')
@click.option('--prefix', default = '', help="Group name prefix if any")
@click.option('--suffix', default = '', help="Group name suffix if any")
def list_apps(prefix, suffix):
	"List Okta Apps"
	apps = oc.list_apps(secret)
	print("\n        Application Name")
	print("------------------------------------------")
	for app in apps:
		app_name = app['label']
		if app_name.lower().startswith(prefix.lower()) and app_name.lower().endswith(suffix.lower()):
			print(app_name)

@operations.command('listUserGroups')
@click.option('--login', default = '', help="Group name prefix if any")
def list_user_group(login):
	"Which group user belongs to"
	try:
		groups = oc.list_user_groups(login, secret)
	except requests.exceptions.HTTPError:
		print("Login doesn't exists")
	else:
		print("\n        Group")
		print("------------------------------------------")
		for group in groups:
			print(group)

@operations.command('assignUserToGroup')
@click.option('--login', help="Login id of the user")
@click.option('--groupname', help="Group name")
def assign_user_to_group(login, groupname):
	"Assign User to Group"
	try:
		result = oc.assign_user_to_group(login, groupname, secret)
	except requests.exceptions.HTTPError:
		print('Okta error..')
	else:
		if result:
			print(f"{login} added to {groupname} successfully.")
		else:
			print("Something went wrong.")

if __name__ == '__main__':
	operations()
