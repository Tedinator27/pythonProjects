'''
This code is designed to webscrap Ebay for the cheapest m1 macbooks. The link to this page 
is in the LINK variable 
Credits: Internet made Coder on YouTube
'''
from bs4 import BeautifulSoup #BeautifulSoup is a package that is used for parsing HTML content 
import requests #this is for making HTTP requests to the eBay website
import numpy as np #numerical operations and handling arrays 
import csv #used for reading and writing data in CSV format
from datetime import datetime #used for getting the current date and time 

LINK = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=m1+macbook+air&_sacat=0"


def get_prices_by_link(link):
    r = requests.get(link) #http get request is sent to the provided URL
    page_parse = BeautifulSoup(r.text, 'html.parser') #this stores the html content 
    search_results = page_parse.find("ul",{"class":"srp-results"}).find_all("li",{"class":"s-item"})

    item_prices = []

    for result in search_results: #loop to look through the website 
        price_as_text = result.find("span",{"class":"s-item__price"}).text
        if "to" in price_as_text:
            continue
        price = float(price_as_text[1:].replace(",",""))
        item_prices.append(price) #this is the list of all the prices that are on the site 
    return item_prices

def remove_outliers(prices, m=2): #if the price is more than 2 standard deviations away from the main price, then it will be filtered out 
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def get_average(prices): #calculates the average of all the prices that are within the standard deviation 
    return np.mean(prices)

def save_to_file(prices):
    fields=[datetime.today().strftime("%B-%D-%Y"),np.around(get_average(prices),2)] #creates a row of data that includes the current date and the average price is rounded to 2 decimal places
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields) #appends this row to a csv file named "prices.csv" using the 'csv.writer' module

if __name__ == "__main__":
    prices = get_prices_by_link(LINK)
    prices_without_outliers = remove_outliers(prices)
    averagePrice = get_average(prices_without_outliers)
    print("This is the average price of everything on the page: " + str(averagePrice))
    print("")
    print("These are all the prices: " + str(prices))
    save_to_file(prices)