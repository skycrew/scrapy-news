Scrapy-News
===========
**Description**

 1. This crawler will crawl bbc.com/news website and store the details in mongodb hosted using compose.io
 2. WebServices is included and hosted using amazon ec2

**Usage**
To crawl

    scrapy crawl bbcspider

List all news

    curl http://54.179.134.54/news

Search specific news

    curl http://54.179.134.54/news/<keyword>

**TODO**

 1. Unit tests
 2. Add more fields

**Limitation**
Time!
