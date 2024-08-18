import requests
import csv
import json
import os
import pandas as pd
from google.cloud import storage


url = "https://zillow56.p.rapidapi.com/search"

querystring = {"location":"houston, tx","output":"json","status":"forSale","sortSelection":"priorityscore","listing_type":"by_agent","doz":"any"}

headers = {
	"x-rapidapi-key": "Enter the rapidapi key here",
	"x-rapidapi-host": "zillow56.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    try:
        # Convert the response to JSON format and extract the results
        data = response.json()
        results = data['results']

        # Define the columns for the DataFrame
        columns = [
            "bathrooms", "bedrooms", "city", "country", "homeStatus", "homeType",
            "latitude", "longitude", "livingArea", "lotAreaUnit", "lotAreaValue",
            "price", "rentZestimate", "state", "zipcode"
        ]

        # Create DataFrame and save it directly as a CSV
        csv_file_path = "properties.csv"
        pd.DataFrame(results, columns=columns).to_csv(csv_file_path, index=False, header=False)

        # Upload the CSV file to the GCS bucket
        bucket_name = 'demo-property01'
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(csv_file_path)
        blob.upload_from_filename(csv_file_path)
        
        print('File successfully uploaded to GCS bucket')

    except KeyError as ke:
        print(f"KeyError: {ke} - The expected key was not found in the response.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print(f"Request failed with status code {response.status_code}")
    

