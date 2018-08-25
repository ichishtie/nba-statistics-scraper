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
        player_name = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(player_name)
        j = j + 1
        inner_counter = str(j)

        games_played = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(games_played)
        j = j + 1
        inner_counter = str(j)

        minutes_played = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(minutes_played)
        j = j + 1
        inner_counter = str(j)

        points_made = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(points_made)
        j = j + 1
        inner_counter = str(j)

        field_goals_made = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(field_goals_made)
        j = j + 1
        inner_counter = str(j)

        field_goals_attempted = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(field_goals_attempted)
        j = j + 1
        inner_counter = str(j)

        field_goal_percentage = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(field_goal_percentage)
        j = j + 1
        inner_counter = str(j)

        three_pointers_made = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(three_pointers_made)
        j = j + 1
        inner_counter = str(j)

        three_pointers_attempted = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(three_pointers_attempted)
        j = j + 1
        inner_counter = str(j)

        three_point_percentage = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(three_point_percentage)
        j = j + 1
        inner_counter = str(j)

        free_throws_made = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(free_throws_made)
        j = j + 1
        inner_counter = str(j)

        free_throws_attempted = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(free_throws_attempted)
        j = j + 1
        inner_counter = str(j)

        free_throws_percentage = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(free_throws_percentage)
        j = j + 1
        inner_counter = str(j)

        offensive_rebounds = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(offensive_rebounds)
        j = j + 1
        inner_counter = str(j)

        defensive_rebounds = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(defensive_rebounds)
        j = j + 1
        inner_counter = str(j)

        total_rebounds = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(total_rebounds)
        j = j + 1
        inner_counter = str(j)

        total_assists = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(total_assists)
        j = j + 1
        inner_counter = str(j)

        total_steals = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(total_steals)
        j = j + 1
        inner_counter = str(j)

        total_blocks = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(total_blocks)
        j = j + 1
        inner_counter = str(j)

        total_turnovers = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(total_turnovers)
        j = j + 1
        inner_counter = str(j)

        personal_fouls = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(personal_fouls)
        j = j + 1
        inner_counter = str(j)

        efficiency_rating = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(efficiency_rating)
        j = j + 1
        inner_counter = str(j)

        assists_to_turnovers = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(assists_to_turnovers)
        j = j + 1
        inner_counter = str(j)

        steals_to_turnovers = browser.find_element_by_xpath('//tr[' + outer_counter + ']/td[' + inner_counter + ']').text
        player.append(steals_to_turnovers)
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

# Write the player statistics to a CSV file
with open('player_stats.csv', 'w+') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter = ',')
    csvWriter.writerows(player_list)



