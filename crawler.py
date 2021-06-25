import sys
import requests
import time
from bs4 import BeautifulSoup

all_links = []
PGS_CRAWLED = []
LINK_QUEUE = []
data = open('data.json', 'w')


def crawl(url):
    global PGS_CRAWLED
    PGS_CRAWLED.append(url)
    print("URL being crawled: " + url)
    try:
        code = requests.get(url)
    except:
        print("Error found at URL: " + url + "\nproceding to next URL")
        return
    content = code.text
    soup = BeautifulSoup(content, "html.parser")
    #print(str(soup))
    data.write("{\"index\":{}}\n")
    data.write("{\"html\": \"" + str(soup).replace("\"", "").replace("\'", "").replace("\t", " ").replace("\r", " ").replace("\n", " ") + "\"}\n")
    for a in soup.find_all('a', href=True):
        if a.get('href'):
            #print(a.get('href'))
            if a.get('href')[0] == '/':                                
                if ((url + a.get('href').strip()) not in PGS_CRAWLED and (url + a.get('href').strip()).replace("www.", "") not in PGS_CRAWLED and ((url + a.get('href')[1:].strip()) not in PGS_CRAWLED)):
                    #print("Full:", url + a.get('href').strip()); #print("From 1:", url + a.get('href')[1:].strip());
                    if url[-1] != '/':
                        all_links.append(url + a.get('href').strip())
                        LINK_QUEUE.append(url + a.get('href').strip())
                    else:
                        all_links.append(url + a.get('href')[1:].strip())
                        LINK_QUEUE.append(url + a.get('href')[1:].strip())
            elif a.get('href')[0:4].lower() == "http":
                if (a.get('href') not in  PGS_CRAWLED and (a.get('href').strip() not in PGS_CRAWLED) and a.get('href').strip().replace("www.", "") not in PGS_CRAWLED):
                    all_links.append(a.get('href').strip())
                    LINK_QUEUE.append(a.get('href').strip())
                
def readWriteFiles(urlFile, num_pgs):
    f = open(urlFile, 'r')
    lines = f.readlines()
    for line in lines:
        url = line.rstrip()
        LINK_QUEUE.append(url)
    f.close()

    for pg in range(num_pgs):
        print(pg)
        crawl(LINK_QUEUE.pop(0))
        time.sleep(3.5)
        # print(PGS_CRAWLED)
        # print(LINK_QUEUE)
        # print(all_links)
 
    # f = open(outFile, "a")
    # for l in all_links:
    #     f.write(l + " \n")
    # f.close()

    # f = open("pgs_crawled.txt", "a")
    # for l in PGS_CRAWLED:
    #     f.write(l + " \n")
    # f.close()

    data.write("\n")
    data.close()

if len(sys.argv) != 3:
    print('Error: Command line argument invalid. USAGE: ./crawler.py <seedUrl file> <number of pages>')
else:
    readWriteFiles(sys.argv[1], int(sys.argv[2]))
    print("\n\nScraping complete")
    print("Results in data.json")