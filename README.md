# Web Crawler

This application involves building a simple web crawler which fetches all public links from a given website

### Tech Stack
* DFS - depth first search

### Application Description
* This web application allows user to login(**username: xun, password: xun**)
* Allow user to choose 5 news sources from 134 news sources and display the top 10 articles
* Displayed news sources as tiles/links in web application and clicking on them will navigate to a screen which shows the top 10 articles.
* It allows the user to save articles and enabled a button which allows the user to look at the saved articles (Bonus-Points)
* The user must be able to choose 5 news sources from the 134 news sources (Bonus points).


## Run the application

### Installation and Running
1. check python3.6 is setup in your computer.
```
python --version
```
or
```
python3 --version
```
* [install python3](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)

2. Clone project
```
git clone https://github.com/XunPeng715/global-legaltech-corp.git
cd  global-legaltech-corp
```
3. Run application
if you want to go through up to 20 webpages
```
python spider.py https://www.tutorialspoint.com/index.htm 20
```
or if you want to fetch all links from website
```
python spider.py https://www.tutorialspoint.com/index.htm
```