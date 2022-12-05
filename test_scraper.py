from typing import Dict, List
from scrape_agoda import Scraper 
import unittest


class ScraperTestCase(unittest.TestCase):

    def setUp(self):
        self.scraper_obj = Scraper()
        

    def test_cases(self):
        self.scraper_obj.__init__()
        self.scraper_obj.accept_cookie()
        self.scraper_obj.top_reviewed()
        self.scraper_obj.scroller()


    def test_list_of_hotel_links(self):
        hotel_link_list = self.scraper_obj.list_of_hotel_links()
        self.assertIsInstance(hotel_link_list, List)

    def test_page_crawler(self):
        extended_hotel_link_list = self.scraper_obj.page_crawler()
        self.assertIsInstance(extended_hotel_link_list, List)

    def test_get_price(self):
       dictionary_price = self.scraper_obj.get_price()
       self.assertIsInstance(dictionary_price, Dict)  

    def test_get_hotelname(self):
        dictionary_hotelname = self.scraper_obj.get_hotelname()
        self.assertIsInstance(dictionary_hotelname, Dict)

    def test_get_location(self):
        dictionary_location = self.scraper_obj.get_location()
        self.assertIsInstance(dictionary_location, Dict)   

    def test_get_rating(self):
        dictionary_rating = self.scraper_obj.get_rating()
        self.assertIsInstance(dictionary_rating, Dict)     

    def test_image_url(self):
        dictionary_images = self.scraper_obj.image_url()
        self.assertIsInstance(dictionary_images, Dict)

    def test_timestamp(self):
       dictionary_timestamp = self.scraper_obj.timestamp()
       self.assertIsInstance(dictionary_timestamp, Dict)    

    def test_unique_id(self):
        dictionary_id = self.scraper_obj.unique_id()
        self.assertIsInstance(dictionary_id, Dict)
 


if __name__ == '__main__':
    unittest.main()



        