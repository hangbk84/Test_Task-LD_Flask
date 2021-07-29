from flask import Flask, render_template, request, redirect
import os
from selenium import webdriver
import time
from flask import Blueprint
from bs4 import BeautifulSoup as soup 
import logging
from logging.handlers import RotatingFileHandler
from flask import current_app

flask_app = Blueprint('flask_app', __name__)

@flask_app.route('/')

def index():
    return render_template('index.html')


# # Distance Page
@flask_app.route('/distance/<fr>/<to>', methods=['GET', 'POST'])
def distance(fr,to):
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    if ((fr == 'Moscow') and (to=='Moscow')) :
        current_app.logger.info('%s The specified address is located inside the MKAD, the distance does not need to be calculated')
        return '0'

#   #selenium bot function returns result    
    else:
        if (fr==to):
            current_app.logger.info('%s Cannot calculate in the same address')
            return '0'
        else:
            if ((fr=='') or (to=='')):
                current_app.logger.info('Error')
                return '0'
            else:
                result = from_to(fr,to)
                current_app.logger.info('%s The result is ',result)
                return result

def from_to(fr,to):
    url = 'https://www.google.fr/maps/dir/{}/{}/data=!4m2!4m1!3e0'.format(fr, to)
    # # Chromedrive setting
    driver = webdriver.Chrome(executable_path = r'D:/chromedriver/chromedriver.exe') 
#     # Connect to the page
    driver.get(url)
#     # Wait 1 sec to ensure full page is loaded
    time.sleep(1)
#     # Soupify source code
    page_soup = soup(driver.page_source, "html.parser")
#     # Extract Distance
    css_dist = "div[class^='section-directions-trip-distance'] > div"
#     # Distance value + unit
    distance = page_soup.select_one(css_dist).text
#     # Format dictionnary
    result = {"distance": distance}

    return result


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    flask_app.run(debug=True, port=5000)