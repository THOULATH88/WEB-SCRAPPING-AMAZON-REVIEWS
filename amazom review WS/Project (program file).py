# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:42:30 2023

@author: Administrator
"""

import re
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup  # BeautifulSoup should be imported from 'bs4', not 'BeautifulSoup4'
from wordcloud import WordCloud, STOPWORDS

# Creating an empty reviews list
amazon_reviews = []

for i in range(1, 5):
    ip = []  # You don't need this line, and it's causing an indentation issue
    url = "https://www.amazon.in/Mi-163-9-Inches-Ultra-Android/product-reviews/B08B9GQMHZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Use the correct method 'findAll', not 'findALL'
    reviews = soup.findAll("span", attrs={"class": "a-size-base review-text review-text-content"})

    # Extracting the content under specific tags
    for i in range(len(reviews)):
        ip.append(reviews[i].text)  # Correct the syntax for appending text
        amazon_reviews = amazon_reviews + ip

# Adding the reviews of one page to an empty list which will contain all the reviews in the future
# Writing reviews in a text file
with open(r"D:/ML subject material/Dataset/Reviews23.tsv", "w", encoding="utf8") as output:
    output.write("\n".join(amazon_reviews))  # Write each review on a new line

# Joining all the reviews into a single paragraph
ip_rev_string = " ".join(amazon_reviews)

# Removing unwanted symbols in case they exist
ip_rev_string = re.sub("[^A-Za-z]+", " ", ip_rev_string).lower()  # Correct the regex pattern
ip_rev_string = re.sub("[0-9]+", " ", ip_rev_string)  # Correct the regex pattern

# Split the paragraph into words
ip_reviews_words = ip_rev_string.split()

# Here we're going to eliminate the stop words
stop_words = set(STOPWORDS)
ip_reviews_words = [w for w in ip_reviews_words if not w in stop_words]

# Joining all the words back into a single paragraph
ip_rev_string = " ".join(ip_reviews_words)

# Word cloud can be performed on string inputs. That's why we have combined everything into a single paragraph.
# Create a simple word cloud

plt.figure(dpi=300)
wordcloud_ip = WordCloud(
    background_color='white',
    width=1920,
    height=1080
).generate(ip_rev_string)

plt.imshow(wordcloud_ip)
plt.show()
