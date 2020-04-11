# Brightcove - Python

This repository contains tools and modules written in Python to deal with Brightcove related APIs and simplifying tasks such as iterating over the full video library and performing actions on the videos.

Tested versions of Python: 2.7.17 and 3.8.2

# Notable files

**account_config.json**: this is a configuration file used by all the scripts and tools. It contains the Video Cloud account ID, API Client ID and Client Secret as well as, optionally, any other data you want to pass on to your scripts. For example a list of video IDs to be deleted or shared or whatever your script needs to do with a list of videos. The example file in this repository already contains a "video_ids" array which is used by the example scripts to process a specific set of video IDs if it is present in the JSON. If it is not present, or the first entry is "all", then the shell module mackee.py will process all videos in your Video Cloud account.

The scripts will look for this exact file in your home folder by default. If it is present they will use the account information contained in the file. Alternatively you can pass the path/name of a custom config file to the module using the -i command line parameter. One exception is bulkIngest.py where you pass a custom config file using the --config parameter.

**mackee.py**: this is a shell module which provides functionality to iterate over all videos in your Video Cloud library or over a subset, specified either by a search query parameter or by a list of video IDs or reference IDs provided in a config file. If executed by itself it will simply list the videos in the library.

**notifications.py**: this is a simple tool to manage CMS notification subscriptions. It is using mackee.py for the CMS API communication.

**bulkIngest.py**: this is a tool which allows you to ingest all videos contained in an S3 bucket, a Dropbox folder or a local folder into you Video Cloud account. It also allows what I call delta-ingest: this allows you to run the tool over the same source location again and ignore already ingested video files. To do so it will create a SQLite database called bulkingest.sqlite in your home folder. You can also use this database to review ingest history.

**downloadVideos.py**: this tool allows you to download the highest resolution MP4 renditions from videos stored in Video Cloud.

All the other scripts are simple examples of how to use the mackee.py module to simplify some common tasks, such as find all Legacy Delivery videos, find all 360/VR videos, etc etc.

# Support

These tools are not created, maintained or supported by Brightcove. Do not reach out to their support team as they will not be able to help you. Instead, post your query or bug report in the Issues section.

# Disclaimer

All code is provided as-is and purely as example. Use it at your own risk.