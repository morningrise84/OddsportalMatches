import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Selenium Config
path = r"""C:\Users\whatever\chromedriver.exe""" # provide path to chromedriver.exe here
s = Service(path)
driver = webdriver.Chrome(service=s)
url = 'https://www.oddsportal.com/tennis/portugal/atp-estoril/' # provide page with the next standings ex. https://www.oddsportal.com/tennis/portugal/atp-estoril/
driver.get(url)

# Oddsportal Scraping
elements = driver.find_elements(by=By.CSS_SELECTOR, value='.flex.hover\\:bg-\\[\\#f9e9cc\\].group.border-l.border-r.border-black-borders.min-h-\\[40px\\]')
lines_of_text = [e.text.split('\n') for e in elements]
formatted_lines_of_text = [','.join(line) for line in lines_of_text]

# CSV Preparation
with open('oddsportal.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'Player 1', '-', 'Player 2', 'Odds 1', 'Odds 2', 'Bs'])
    for line in formatted_lines_of_text:
        writer.writerow(line.split(','))

# Quit the webdriver
driver.quit()
