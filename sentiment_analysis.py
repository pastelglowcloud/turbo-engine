punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
positive_words = []
negative_words = []
twitter_data = []

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
fileconnection = open("project_twitter_data.csv", 'r')
lines = fileconnection.readlines()
for row in lines[1:]:
    twitter_data.append(row.strip().split(','))
            
def strip_punctuation(word:str):
    for item in punctuation_chars:
        word = word.replace(item, "")
    return word
    
def get_pos(tweet):
    pfreq = 0
    for word in tweet:
        word = strip_punctuation(word)
        if word in positive_words:
            pfreq = pfreq + 1
    return pfreq

def get_neg(tweet):
    nfreq = 0
    for word in tweet:
        word = strip_punctuation(word)
        if word in negative_words:
            nfreq = nfreq + 1
    return nfreq

outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

for datum in twitter_data:
    tweet = datum[0]
    tweet = tweet.lower()
    tweet = tweet.split(" ")
    neg_score = get_neg(tweet)
    pos_score = get_pos(tweet)
    net_score = pos_score-neg_score
    row_string = '{}, {}, {}, {}, {}'.format(datum[1], datum[2], pos_score, neg_score, net_score)
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()