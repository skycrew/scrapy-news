Scrapy-News
===========
**Description**

 1. This crawler will crawl bbc.com/news website and store the details in mongodb hosted using compose.io
 2. WebServices is included and hosted using amazon ec2

**Usage**

To crawl

    scrapy crawl bbcspider

List all news

    curl http://ec2-52-221-187-243.ap-southeast-1.compute.amazonaws.com/news

Search specific news

    curl http://ec2-52-221-187-243.ap-southeast-1.compute.amazonaws.com/news/<keyword>

**TODO**

 1. Unit tests
 2. Add more fields
 3. Automate crawler by cron

**Limitation**

Time!
