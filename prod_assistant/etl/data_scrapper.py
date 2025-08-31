from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import selenium.webdriver.common.by as By   
import selenium.webdriver.common.keys as Keys
import selenium.webdriver.common.action_chains as ActionChains
import csv
import time
import re
import os


class FlipkartScraper:
    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def get_top_reviews(self,product_url,count=2):
        pass
    
    def scrape_flipkart_products(self, query, max_products=1, review_count=2):
        pass
    
    def save_to_csv(self, data, filename="product_reviews.csv"):
        pass
    
    