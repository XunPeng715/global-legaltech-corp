# Web Crawler

This application involves building a simple web crawler which fetches all public links from a given website

### Tech Stack
* DFS - depth first search
* Set - remove duplicate

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
* if you want to fetch all links from website
```
python spider.py https://www.tutorialspoint.com/index.htm
```
* if you want to go through up to 20 webpages
```
python spider.py https://www.tutorialspoint.com/index.htm 20
```
