import json
import urllib.request
import os
import datetime

my_filename = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
my_path = 'C:/Users/kambo/Desktop/Data-Collection-Pipeline/raw_data/hotels/images/'

class Downloader:
    ''' This class downloads images from urls in a dictionary and saves them to a folder '''

    def __init__(self) -> None:
        self.img_list = []
        self.count = 0

    def load_file(self):
        '''This method opens the json file and appends the urls to an empty list'''
        with open(r"C:\Users\kambo\Desktop\Data-Collection-Pipeline\raw_data\hotels\data.json") as file:
            data = json.load(file)  
        for link in data['Image URL']:
            self.img_list.append(link)

    
    def folder(self):
        '''Creates a folder called images in a specified path'''
        newpath = r'C:\Users\kambo\Desktop\Data-Collection-Pipeline\raw_data\hotels\images'
        if not os.path.exists(newpath):
            os.mkdir(newpath)    

    def images_download(self):
        '''Downloads the images from the urls and save them in the folder created above'''
        for url in self.img_list:
            my_fullpath = my_path + my_filename + '_' +str(self.count) + '.jpg' 
            urllib.request.urlretrieve(url, my_fullpath)
            self.count +=1

def download():
    load = Downloader()
    load.load_file()
    load.folder()
    load.images_download()

if __name__ == '__main__':
    download()