# nba-statistics-scraper

A Python3 program that uses Selenium to scrape statistics from "https://stats.nba.com/." Currently, the program is limited to basic individual player statistics with plans to add team statistics.

Link to scraper: [player_stats_scraper.py](https://github.com/ichishtie/nba-statistics-scraper/blob/master/nba_statistics_scraper_pkg/player_stats_scraper.py)

### Instructions

1. There are two ways to download the Python bindings for Selenium. If you have [pip](https://pypi.org/project/pip/) on your system, you can download and install Selenium with the following command:

   ```
   pip install selenium
   ``` 
   Otherwise, you can download directly from the [PyPI page](https://pypi.org/project/selenium/).   

2. You must install a driver for Selenium to be able to interface with the chosen browser. [nba-statistics-scraper](https://github.com/ichishtie/nba-statistics-scraper/) uses Chrome, which has [its own specific driver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure that the driver executable is on your system's *PATH*.

3. Run the program. 

   Note: The program will take several minutes to complete and will create a CSV file in the directory you ran the program from.   

### Built With

* [Selenium](https://www.seleniumhq.org/) - The software-testing web application framework used

### Author

* **[Iyad Chishtie](https://github.com/ichishtie)**

### License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.