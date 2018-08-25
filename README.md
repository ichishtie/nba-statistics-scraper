# nba-statistics-scraper

A Python3 program that uses Selenium to scrape statistics from [stats.nba.com](stats.nba.com) Currently, the program is limited to basic individual player statistics with plans to add team statistics.

### Instructions

1. This program requires Selenium. If you have pip, install using:
   ```
   pip install selenium
   ```
   Otherwise, download and install Selenium from [here](https://pypi.org/project/selenium/).
   
2. To allow the program to interface with the Chrome browser, you must download [chromedriver]     (https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your PATH.

3. Open your command line or Terminal and navigate to the directory you would like to clone the repository.

4. Clone the repository
   ```
   git clone https://github.com/ichishtie/nba-statistics-scraper
   ```
5. Navigate to the directory where you cloned the repository and then go to the folder labeled "scraper".
   ```
   cd scraper
   ```
6. Run the program.
   
   Windows:
   ```
   python player_stats_scrape.py
   ```
   macOS:
   ```
   python3 player_stats_scrape.py
   ```
   
Note: A CSV file will be created in the "scraper" folder. This file will contain the statistics gathered by the program.

### Built With

* [Selenium](https://www.seleniumhq.org/) - The software-testing web application framework used

### Author

* **[Iyad Chishtie](https://github.com/ichishtie)**

### License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.
