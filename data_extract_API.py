import requests
import csv
import json
import os
import pandas as pd
from google.cloud import storage

#####################################################################################
####### Part 1 -  Extracting data from Rapid API

# import requests


# url = "https://zillow56.p.rapidapi.com/search"

# querystring = {"location":"houston, tx","output":"json","status":"forSale","sortSelection":"priorityscore","listing_type":"by_agent","doz":"any"}

# headers = {
# 	"x-rapidapi-key": "Enter the rapidapi key here",
# 	"x-rapidapi-host": "zillow56.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)


# if response.status_code == 200:
#     # Convert the response to JSON format
#     data = response.json()
    
#     # Define the path for the output JSON file
#     file_path = "response.json"
    
#     # Write the JSON data to the file
#     with open(file_path, 'w') as json_file:
#         json.dump(data, json_file, indent=4)  # indent=4 for pretty-printing
    
#     print(f"Response saved to {file_path}")
# else:
#     print(f"Request failed with status code {response.status_code}")


#####################################################################################
####### Comment Part 1
####### Part 2 - Storing fetched data into CSV file

# with open('response.json', 'r') as json_file:
#     data = json.load(json_file)

# results = data['results']

# columns = [
#     "bathrooms", "bedrooms", "city", "country", "homeStatus", "homeType",
#     "latitude", "longitude", "livingArea", "lotAreaUnit", "lotAreaValue",
#     "price", "rentZestimate", "state", "zipcode"
# ]

# df = pd.DataFrame(results, columns=columns)

# print(df.shape)

# csv_file_path = "properties.csv"

# df.to_csv(csv_file_path, index=False, header=False)



#####################################################################################
####### Comment Part 2
####### Part 3 - Loading data into GCS bucket
# credential_path = "Enter the path of JSON file downloaded from Google cloud"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


# try:
#     csv_filename = 'properties.csv'

#     bucket_name = 'demo-property01'
#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)

#     destination_blob_name = f'{csv_filename}'

#     blob = bucket.blob(destination_blob_name)
#     blob.upload_from_filename(csv_filename)
    
#     print('File successfully uploaded to GCS bucket')
# except Exception as e:
#     print(e)




