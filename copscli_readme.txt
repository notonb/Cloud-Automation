How to setup?
-------------
pip install click
copy okta_common.py from /python/lib/python3.7/site-packages/okta_common.py 
    to site_packages folder

How to use copscli?
-------------------
get the credentials using gimme-aws-creds -k
set the environment variables with the updated credentials

Okta Cli help
-------------
python copscli.py --help

List Groups
----------
python copscli.py listGroups --help
python copscli.py listGroups --prefix tfe --suffix plan
python copscli.py listGroups --anywhere hana

List Group Members
-------------
python copscli.py listGroupMembers --help
python copscli.py listGroupMembers
python copscli.py listGroupMembers --groupname <role_name>

List Users
----------
python copscli.py listUsers --help
python copscli.py listUsers
python copscli.py listUsers --login bhatt

List Apps
----------
python copscli.py listApps --help
python copscli.py listApps
python copscli.py listApps --prefix AWS
python copscli.py listApps --prefix Cloud --suffix <rolename>

List User Groups
-----------------
python copscli.py listUserGroups --help
python copscli.py listUserGroups --login
python copscli.py listUserGroups --login <email>

AssignUserGroup
---------------
python copscli.py assignUserToGroup --help
python copscli.py assignUserToGroup --login <email> --groupname <groupname>

python copscli.py assignUserToGroup --login <email> --groupname <groupname>
