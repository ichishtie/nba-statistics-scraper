from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# Create an instance of Chrome WebDriver and then navigate to the NBA statistics page.
# Then, force the instance to explicitly wait in order to allow all elements to load into the DOM.
browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://stats.nba.com/leaders/?Season=2017-18&SeasonType=Regular%20Season&PerMode=Totals')
time.sleep(2)

# Locate and record the number of pages in the table
player_list = []
num_pages_element = browser.find_element_by_xpath("//div[@class='stats-table-pagination__info']")
list = [int(s) for s in num_pages_element.text.split() if s.isdigit()]
num_pages = (list.pop())

# Record the statistics for every individual player and append the player to the player list.
i = 1
j = 2
k = 1
outer_counter = str(i)
inner_counter = str(j)
while k <= num_pages:
    try:
        player = []

        while j <= 25:
            if j == 2:
                info = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
            else:
                info = float(browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text)
            player.append(info)
            j = j + 1
            inner_counter = str(j)

        player_list.append(player)
        j = 2
        inner_counter = str(j)
        i = i + 1
        outer_counter = str(i)
    except:
        element = browser.find_element_by_xpath("//a[@class='stats-table-pagination__next']")
        element.click()
        i = 1
        outer_counter = str(i)
        k = k + 1
        continue

browser.close()

# Write the player statistics to a CSV file
with open('player_stats.csv', 'w+') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter = ',')
    csvWriter.writerows(player_list)


