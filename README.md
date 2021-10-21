# streamlit-twitter-scraper

![MADE WITH PYTHON](http://ForTheBadge.com/images/badges/made-with-python.svg)  ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourGitHubName/yourRepo/yourApp/)
   ![MIT LICENSE](https://badgen.net//badge/license/MIT/green)   ![MAINTAINED BADGE](https://img.shields.io/badge/Maintained%3F-yes-green.svg)   

 Disclaimer:
  This project is built for research purposes only. I, ***Mpho Kubeka*** , as the developer am not responsible for any misuse of this project. I believe that this kind of   technology should be accessible if needed for the correct reasons.
  
 ### This project is built using 
 * Streamlit
 * Twint
 * Pandas
 * base64

## Hosted on AWS:
[Link](http://13.244.233.247:8501/)

## Article on Medium
[How to build a beautiful Twitter scraping web app using Streamlit and Twint.](https://medium.com/@dataprojectswithMJ/how-to-build-a-beautiful-twitter-scraping-web-app-using-streamlit-and-twint-44a725d3be07)
 
  
## A web app to scrape past Tweets
![Screenshot from 2021-10-15 17-46-50](https://user-images.githubusercontent.com/92593501/137516457-e67e1897-b592-4b1d-9402-3e863fa2cd16.png)


### Requesting Tweets is really easy:
![Screenshot from 2021-10-15 17-47-04](https://user-images.githubusercontent.com/92593501/137516507-1306cd05-54ed-4aa9-ae5b-cc8ce1268d9f.png)
I have been going through some issues with the slider. Whenever a number is chosen, the scraper always goes over the specified amount. This issue is on top of my priorities list.)

### The Output 1:
![Screenshot from 2021-10-15 17-47-14](https://user-images.githubusercontent.com/92593501/137516705-d368a655-164d-45e8-b7c4-716e5f5b74aa.png)
This is in table form showing the Tweet as well as the time the Tweet was made.

### Output 2:
![download-link](https://user-images.githubusercontent.com/92593501/137518592-703f0cf4-8190-4260-a52a-a198cda39a0c.png)

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
