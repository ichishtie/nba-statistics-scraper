# nba-statistics-scraper

A Python3 program that uses Selenium to scrape statistics from [stats.nba.com](stats.nba.com) Currently, the program is limited to basic individual player statistics with plans to add team statistics.

### Instructions

1. This program requires Selenium. If you have pip, install using:
   ```
   pip3 install selenium
   ```
   
   Otherwise, download and install Selenium from [here](https://pypi.org/project/selenium/).
   
2. To allow the program to interface with the Chrome browser, you must download [chomedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your PATH. Save the executable file in your C Drive and make sure that it is saved under the name "chromedriver.exe", otherwise you will have to change the code on line 8 to match the destination of the chromedriver executable.

3. Open your command line or Terminal and navigate to the directory you would like to clone the repository.

4. Clone the repository.
   ```
   git clone https://github.com/ichishtie/nba-statistics-scraper
   ```

5. Navigate to the local repository.
   ```
   cd nba-statistics-scraper
   ```

6. Navigate to the directory where you cloned the repository and then go to the folder labeled "scraper".
   ```
   cd scraper
   ```
7. Run the program.
   
   Windows:
   ```
   py player_stats_scrape.py
   ```
   macOS:
   If you have both Python2 and Python3 installed, run the program using:
   ```
   python3 player_stats_scrape.py
   ```
   Otherwise, run the program using:
   ```
   player_stats_scrape.py
   ```  
   
Note: A CSV file will be created in the "scraper" folder. This file will contain the statistics gathered by the program.

### Built With

* [Selenium](https://www.seleniumhq.org/) - The software-testing web application framework used

### Author

* **[Iyad Chishtie](https://github.com/ichishtie)**

### License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.
