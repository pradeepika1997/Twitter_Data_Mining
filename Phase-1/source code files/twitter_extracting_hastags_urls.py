import json
import re

# This functions takes .txt file as input
# and returns tweets as a list of json
def parse_tweets(tweet_files):

    twt_data = []
    for tweet_file in tweet_files:
    
        tweets_file = open(tweet_file, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                twt_data.append(tweet)
            except:
                continue

    print('\tSuccessfully parsed data into json format')
    return twt_data


# This function extracts hashtags and urls from tweets data
def extract_hashtags_urls(twt_data):

    # Extract hashtags and urls into separate files
    htfile = 'hashtags.txt'
    urlfile = 'urls.txt'

    htoutfile = open(htfile, 'w',encoding="utf-8")
    urloutfile = open(urlfile, 'w',encoding="utf-8")

    for i in range(len(twt_data)):

        # Extracting hashtags
        if re.match(r"401", str(twt_data[i])):
            continue
            
        ht = twt_data[i].get('entities').get('hashtags')
        for j in range(len(ht)):
            htoutfile.write(ht[j].get('text'))
            htoutfile.write('\n')

        # Extracting urls (expanded urls only)
        url = twt_data[i].get('entities').get('urls')
        for k in range(len(url)):
            urloutfile.write(url[k].get('expanded_url'))
            urloutfile.write(' ')

  
    print('\n...............Extraction is done................')


# Main Activity
if __name__ == '__main__':

    #Parsing the data
    print('\n...............Parsing data....................')
    tweet_files = ["tweets_tech.json", "tweets_tech-1.json", "tweets_tech-2.json"]
    tweets_data = parse_tweets(tweet_files)

    #Extracting hashtags and urls
    print('\n........Extracting hashtags and urls..........')
    extract_hashtags_urls(tweets_data)
