import base64
import pandas as pd
import boto3
import json

creds = json.load(open('creds.json'))
comprehend = boto3.client(
    'comprehend',
    aws_access_key_id= creds['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'],
    aws_session_token=creds['AWS_SESSION_TOKEN'],
    region_name="eu-west-1"
)

def convert_df(df):
    return df.to_csv().encode('utf-8')


def get_csv_download_link(csv, filename):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """

    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download csv file</a>'
    return href

