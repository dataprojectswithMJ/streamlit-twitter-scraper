import streamlit as st
import twint
import pandas as pd
import base64

st.image('dark_banner.png')
st.subheader("""
Let's scrape some Tweets... Hope Twitter doesn't ban me :smile:
""")


@st.cache
def get_table_download_link(df, filename):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """

    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download csv file</a>'
    return href


with st.form(key='Twitter_form'):
    search_term = st.text_input('What do you want to search for?')
    limit = st.slider('How many tweets do you want to get?', 0, 500, step=20)
    output_csv = st.radio('Save a CSV file?', ['Yes', 'No'])
    file_name = st.text_input('Name the CSV file:')
    submit_button = st.form_submit_button(label='Search')

    if submit_button:
        c = twint.Config()

        c.Search = search_term
        c.Limit = limit

        if output_csv == 'Yes':
            c.Store_csv = True

        if c.Store_csv:
            c.Output = f'{file_name}.csv'

        twint.run.Search(c)

        data = pd.read_csv(f'{file_name}.csv', usecols=['date', 'tweet'])
        st.table(data)

        st.markdown(get_table_download_link(data, file_name), unsafe_allow_html=True)
