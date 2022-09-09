import streamlit as st
import twint
import pandas as pd
import json
from functions import convert_df, comprehend
import botocore


# Set page name and favicon
st.set_page_config(page_title='Twitter scraper',page_icon=':iphone:')


st.image('dark_banner.png')
st.subheader("""
Let's scrape some Tweets... Hope Twitter doesn't ban me :smile:
""")

languages = []
sentiments = []

# customize form
with st.form(key='Twitter_form'):
    search_term = st.text_input('What do you want to search for?')
    limit = st.slider('How many tweets do you want to get?', 0, 500, step=20)
    output_csv = st.radio('Save a CSV file?', ['Yes', 'No'])
    file_name = st.text_input('Name the CSV file:')
    submit_button = st.form_submit_button(label='Search')

    if submit_button:
        # configure twint
        c = twint.Config()

        c.Search = search_term
        c.Limit = limit

        c.Store_csv = True

        if c.Store_csv:
            c.Output = f'{file_name}.csv'

        twint.run.Search(c)

        data = pd.read_csv(f'{file_name}.csv', usecols=['date', 'tweet'])

        for x in data['tweet']:
            # Get language of the tweet
            lang = comprehend.detect_dominant_language(Text=x)['Languages'][0]['LanguageCode']
            languages.append(lang)
            print(f'Language detected: {lang}')
        data['languages']=languages

            # Get the sentiment of the tweet
        for x in range(len(data['tweet'])):
            try:
                sent = comprehend.detect_sentiment(
                                                    Text=data['tweet'][x],
                                                    LanguageCode= data['languages'][x]
                                                    )['Sentiment']
                sentiments.append(sent)
                print(f'Sentiment detected:{sent}')
            except botocore.exceptions.ClientError as error:
                print(f'Error: {error}')
                sentiments.append(error)
        data['sentiment']= sentiments
        st.table(data)


try:
    st.download_button(label='Download results', data=convert_df(data), file_name = f'{file_name}.csv', mime='text/csv')
except:
    pass
