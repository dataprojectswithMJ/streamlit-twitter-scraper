# Twitter Sentiment Analysis Web App
## streamlit-twitter-scraper

![MADE WITH PYTHON](http://ForTheBadge.com/images/badges/made-with-python.svg)  ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dataprojectswithmj-streamlit-twitter-scraper-app-y4efs3.streamlitapp.com/)
   ![MIT LICENSE](https://badgen.net//badge/license/MIT/green)   ![MAINTAINED BADGE](https://img.shields.io/badge/Maintained%3F-yes-green.svg)   

 Disclaimer:
  This project is built for research purposes only. I, ***Mpho J Kubeka*** , as the developer am not responsible for any misuse of this project. I believe that this kind of   technology should be accessible if needed for the correct reasons.
  
 ### This project is built using 
 * Streamlit
 * Twint
 * Pandas
 * base64

## Hosted on Streamlit Cloud [(read more about Streamlit Cloud)](https://streamlit.io/cloud):
[Streamlit Twitter Scraper](https://dataprojectswithmj-streamlit-twitter-scraper-app-y4efs3.streamlitapp.com/)

## Article on Medium
[How to build a beautiful Twitter scraping web app using Streamlit and Twint.](https://medium.com/@dataprojectswithMJ/how-to-build-a-beautiful-twitter-scraping-web-app-using-streamlit-and-twint-44a725d3be07)
 
  
## A web app to scrape past Tweets
![Screenshot from 2021-10-15 17-46-50](https://user-images.githubusercontent.com/92593501/137516457-e67e1897-b592-4b1d-9402-3e863fa2cd16.png)


### Requesting Tweets is really easy:
<img width="700" alt="Screenshot 2022-09-09 at 12 59 12" src="https://user-images.githubusercontent.com/92593501/189335562-4694dd35-6351-457f-890c-f10f21ce00eb.png">
I have been going through some issues with the slider. Whenever a number is chosen, the scraper always goes over the specified amount. This issue is on top of my priorities list.)

### The Output 1:
<img width="784" alt="Screenshot 2022-09-09 at 12 55 04" src="https://user-images.githubusercontent.com/92593501/189335237-f6c1c47c-c162-4fd9-8dbc-5750b7cc1c16.png">
This is in table form showing the Tweet, date when the tweet was made, the language code of the tweet as well as the sentiment. In the case of an error, the error will be included in the field.

### Output 2:
![Screenshot 2022-07-23 at 17 14 04](https://user-images.githubusercontent.com/92593501/180611114-7010540e-aa48-4781-9678-bed32247acad.png)


The file can be downloaded.However the option to save file as CSV has to be ***YES***.
At the moment only CSV formats can be exported. I am incorporating other output formats such as:

* JSON
* Excel
* SQLite

## Installation

### Pip
> pip3 install requirements.txt

#### When installing Twint. Follow the following steps to get the modified version of Twint. This is because Twint can get the Limit of tweets incorrect and this modification fixes that.
 1. Go to the Twint file
 2. Navigate into the other smaller **twint** file
 3. Run
   > python3 setup.py install #insert sudo if Linux

### Run Streamlit
> streamlit run app.py
