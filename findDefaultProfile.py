#!/usr/bin/env python3
import sys
import argparse
from mackee import OAuth
from mackee import IngestProfiles
from mackee import LoadAccountInfo
from mackee import videos_from_file
from mackee import eprint

# init the argument parsing
parser = argparse.ArgumentParser(prog=sys.argv[0])
parser.add_argument('--config', metavar='<config filename>', type=str, help='Name and path of account config information file')
parser.add_argument('--account', metavar='<Brightcove Account ID>', type=str, help='Brightcove Account ID to use (if different from ID in config)')
parser.add_argument('--xls', metavar='<XLS/CSV file>', type=str, help='file with account IDs in account_id column')

# parse the args
args = parser.parse_args()

# get account info from config file
account_id, client_id, client_secret, opts = LoadAccountInfo(args.config)

# if account ID was provided override the one from config
if(args.account):
	account_id = args.account

# create a Ingest Profiles API instance
ingestProfiles = IngestProfiles( OAuth(account_id=account_id,client_id=client_id, client_secret=client_secret) )

# list of account IDs to check
acc_ids = []

# if list is empty try to get it from xls or config JSON
if(not acc_ids):
	# if we have an xls/csv
	if(args.xls):
		acc_ids = videos_from_file(args.xls, column_name='account_id')

	# otherwise just use the options from the config file
	elif(opts):
		acc_ids = opts.get('target_account_ids')

if(acc_ids):
	print('account_id, display_name, name')
	for acc_id in acc_ids:

		response = ingestProfiles.GetDefaultProfile(accountID=acc_id)
		if(response.status_code == 200):
			dpid = response.json().get('default_profile_id')

			response = ingestProfiles.GetIngestProfile(accountID=acc_id, profileID=dpid)
			if(response.status_code == 200):
				displayName = response.json().get('display_name')
				name = response.json().get('name')
				print(f'{acc_id}, {displayName}, {name}')
else:
	eprint('No account IDs provided.')