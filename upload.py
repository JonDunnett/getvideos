# upload.py

from boxsdk import JWTAuth
from boxsdk import Client

# Configure JWT auth object
sdk = JWTAuth.from_settings_file('/home/jon/getvideos/292083_bl8esdvi_config.json')

# Get auth client
client = Client(sdk)

# PERFORM API ACTIONS WITH CLIENT
'''
# Set search config fields
search_term = 'SEARCH QUERY'
type = 'CONTENT TYPE'	# file, folder, or web_link
limit = 10
offset = 0

# Set search config fields
content = client.search().query(search_term, result_type=type, limit=limit, offset=offset)
'''


# Set folder values
folder_name = 'FOLDER NAME TO CREATE'
folder_id = 'FOLDER ID TO CREATE FOLDER IN'

# Create folder
folder = client.folder(folder_id=folder_id).create_subfolder(folder_name)

# Set upload values
file_path = 'PATH TO LOCAL FILE TO BE UPLOADED'
file_name = 'FILE NAME TO UPLOAD AS'
folder_id = 'FOLDER ID TO UPLOAD TO'

box_file = client.folder(folder_id).upload(file_path, file_name)
