This README is a guide to scrape a website and return specified results. 

To build the scraper, we required the following modules, labraries and packages
* Selenium webdriver for nevigating the web pages
* Chromedriver for using Chrome as the browser
* Datetime for creating timestamps
* uuid for unique ids
* os to create folders
* json to create a json file
* time for pacing the scraper

Milestones 1
* Setup the GIT environment for the project.

Milestone 2 
* First of all we chose the Agoda website since our objective is to find hotel features and prices for a specfic destination during set dates
* We decided to use Agoda to obtain our data from because the data is relevant to our personal ambitions to travel extensively.

Milestone 3 and 4 
* Create a class to perform the web scraping called Scraper.
* Initialize the class.
* Create methods to nevigate the webpage and to obtain the information needed.


Milestone 5 
* Add docstring to all methods 
* Create unit tests to test all public methods

Milestone 6 
* Downloaded and created a docker hub account 
* Build a docker image with all the dependancies for the application then pushed the docker container to docker hub




<img width="367" alt="docker-hub" src="https://user-images.githubusercontent.com/114100987/206197429-3d066086-0f21-4402-abcd-163dc952468e.png">





Milestone 7
* Set up the GitHub secrets following: https://docs.docker.com/build/ci/github-actions/
* Create the GitHub actions that will create a docker image and push it to the docker hub when pushed to main of the repository.






 


 
