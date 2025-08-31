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
    """
    A class to scrape product reviews from Flipkart.
    """
    def __init__(self, output_dir="data"):
        """Initialize the FlipkartScraper class.

        Args:
            output_dir (str, optional): The directory to save scraped data. Defaults to "data".
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def get_top_reviews(self, product_url,  count=2):
        """Get the top reviews for a product.                       

        Args:
            product_url (_type_): _description_
            count (int, optional): _description_. Defaults to 2.
        """
        pass
    
    def scrape_flipkart_products(self, query, max_products=1, review_count=2):
        """Scrape Flipkart products based on a search query.                

        Args:
            query (_type_): _description_   
            max_products (int, optional): _description_. Defaults to 1.
            review_count (int, optional): _description_. Defaults to 2.
        """
        pass
    
    def save_to_csv(self, data, filename="product_reviews.csv"):
        """Save the scraped product reviews to a CSV file.

        Args    :
            data         (_type_): _description_
            filename (str, optional): _description_. Defaults to "product_reviews.csv".
        """
        pass
    
    