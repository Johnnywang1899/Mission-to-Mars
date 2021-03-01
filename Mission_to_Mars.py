# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup

# Import pandas
import pandas as pd

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'D:\Chromedriver\chromedriver_win32\chromedriver.exe'}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Check if certain tags are included in the returned result
browser.is_element_present_by_css('ul.item_list li.slide')

# Set soup for parsing
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_ = 'content_title').get_text()
news_title

# Use the parement slement to find the paragraph text
news_p = slide_elem.find('div', class_ = 'article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_ = 'fancybox-image'). get('src')

# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

# Read the table from the html file
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns = ['description', 'value']
df.set_index('description', inplace = True)

# Conver the dataframe to html file format
df.to_html()

# Quite browser control
browser.quit()
