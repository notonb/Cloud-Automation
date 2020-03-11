How to setup?
-------------
pip install click
copy okta_common.py from https://ghe.spehosting.com/Core/core-infra-brownfield-vm/blob/OKTA_LIB/layers/okta_common/python/lib/python3.7/site-packages/okta_common.py 
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
python copscli.py listGroupMembers --groupname aws_838069673214_speAdmin

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
python copscli.py listApps --prefix Cloud --suffix speAdmin

List User Groups
-----------------
python copscli.py listUserGroups --help
python copscli.py listUserGroups --login
python copscli.py listUserGroups --login Notonesh_Bhattacharya@spe.sony.com

AssignUserGroup
---------------
python copscli.py assignUserToGroup --help
python copscli.py assignUserToGroup --login Notonesh_Bhattacharya@spe.sony.com --groupname osgOktaOrgAdmin

python copscli.py assignUserToGroup --login Notonesh_Bhattacharya@spe.sony.com --groupname tfe_spe_tv_sptb2b_prd_plan