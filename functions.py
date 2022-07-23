import base64
import pandas as pd


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
