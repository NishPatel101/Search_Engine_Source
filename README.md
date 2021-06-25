# CS172 - Final Project (IR System)

## Member Information
Spring 2021  
Team member 1 - Bryant Chang  
Team member 2 - Nish Patel
  
## Collaboration Details
Bryant created the foundational crawler code.  
Nish added features to the crawler to extract the html code into a data.json file. He made the scripts to run the crawler and indexer.
  
## Part 1 - Crawler
### --Overview--
####	Architecture:
The system uses queues to keep track of visited URLS. From the initial starting (seed) URL, the crawl() function is called.  
crawl() adds the current URL to the visited queue, extracts html info to the data.json file, and searches for links in the page.  
crawl() is called on these linked pages that have not already been crawled on. There is a delay for politeness.  
The first URL is taken from a seedURl.txt file, and only num_pgs pages are crawled.  
####	Crawling Strategy:
Begin from seed URL. Extract information from the html source code. Look for links in <a> tags and crawl the pages if not already visited.  
Due to race conditions, we removed the multithreading and the crawler no longer works in parallel.  
Due to issues with certain non-normalized URLS, we removed much of the duplicate-checking code. Many duplicates are handled but not all.  
####	Data Structures:
The crawler uses a PGS_CRAWLED array to store visited URLs. There are other arrays (all_links and LINK_QUEUE), but these were used for testing.  
For URL handling, the crawler uses BeautifulSoup objects.  
### --Limitations--
The crawler does not perfectly handle duplicates, so some previously visited website links that are not normalized are left undetected.  
### --Instructions--
Run code: ./crawler.py <seedUrl file> <number of pages to crawl>  
  Since we use Windows Terminal, we ran with "py ./crawler seedURL.txt 590"  
  Because the crawler is mainly used for extracting the information to a data.json file, we just used a python script.  
  After the data.json file is created, we use that for the IR.  

## Part 2 - Indexer
### -- Instructions--
Created a bash script that takes in a query word, bulk-loads the index, and outputs the query results to an output file specified by the user.  
  Run code: ./index.sh <query-word> <output file name>  
  Since we use Windows, we ran with "bash index.sh uci output.txt"  

## Part 3 - Extension
  We attempted the website extension to display queries to the user.


# P.S. Thank you for the kindness and teachings, Professor Salloum and Ms. Chen! This project was a struggle, but it was worth the lessons learned. --Nish :)
