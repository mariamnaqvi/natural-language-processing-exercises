# required imports
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_blog_articles (input):
    output = []
    
    for url in input:
        # collect the entire page
        headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # grab the title
        title = soup.title.string 
        # grab the content
        content = soup.find('div', class_='jupiterx-post-content')
        
        # add those to a dictionary
        data = {'title': title, 'content': content.text}
        # append to the list of dictionaries
        output.append(data)

        # convert output to df
        df = pd.DataFrame(output)
    # return the dataframe
    return df


def get_news_articles_for_one_category (category, url):
    output = []
    
    # collect the entire page
    headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find ALL of the card div elements, each one being a separate article
    divs = soup.find_all('div', class_='news-card z-depth-1')
    
    # for each div, get the data we need
    for article in divs:
        title = article.find('span', itemprop='headline')
        content = article.find('div', itemprop='articleBody')
        data = {'title': title.text, 'content': content.text, 'category': category}
        # add it to our output array
        output.append(data)
    return output

# build an aggregator function
def get_news_articles(input):
    final_output = []
    # loop through the dictionary and call the above function for each category/url pair
    for key, value in input.items():
        temp_list = get_news_articles_for_one_category(key, value)
        final_output += temp_list
     # convert final output to df
    df = pd.DataFrame(final_output)
    return df