import sys
import os 
import tweepy
import json
import pandas as pd

consumer_secret = 'dFcbmYl0O9yfNgmyM9h6pbjhVgY18lyMsFQXU2aCfNwqiEyXJl' 
consumer_key = 'qid1fBtd1UtI1nSP2rlws7wGa'

#consumer_secret = 'hhuf6ZVJWVGHux9GHz8nWEBpNfQNsuKo7LT9O92GTHgJH8UGjJ'
#consumer_key = '8zdNwxAj6rTMgjvz5sKJmeVZ6'

used_ids = [1339835893,89781370,11388132,15824288]
dem_ids = [216776631,2746932876]
gop_ids = [113047940,1180379185,1347285918,1074480192,65691824,3021632183,432895323,15416505,17078632,18020081,2865560724,216881337,15745368,25073877,58379000]
ids = dem_ids+gop_ids

used_cand = ['Lincoln Chafee','Hillary Rodham Clinton','Lawrence Lessig',"Martin O'Malley"]
candidates = ['Bernie Sanders','Jim Webb','Jeb Bush','Ben Carson','Chris Christie','Ted Cruz','Carly Fiorina','Jim Gilmore','Lindsey Graham','Mike Huckabee','Bobby Jindal','John Kasich','George Pataki','Rand Paul','Marco Rubio','Rick Santorum','Donald J. Trump']

dems = candidates[0:2]
gop = candidates[2:]
rev_mapper = {}
for dem_id in range(len(dems)):
	rev_mapper[dem_ids[dem_id]] = dems[dem_id]
for gop_id in range(len(gop)):
	rev_mapper[gop_ids[gop_id]] = gop[gop_id]

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

#status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need

def process(a,id_):
	df = {'date_time':[],'text':[],'name':[],'location':[]}
	for tweet in a:
		new_tweet = json.loads(tweet.json)
		df['date_time'].append(new_tweet['created_at'])
		df['location'].append(new_tweet['user']['location'])
		df['text'].append(new_tweet['text'])
		df['name'].append(rev_mapper[id_])
	answer = pd.DataFrame(df)
	return answer

if __name__ == "__main__":
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		api = tweepy.API(auth)
		for id_ in ids:
			print(rev_mapper[id_])
			a = tweepy.Cursor(api.user_timeline,id=id_).items()
			result = process(a,id_)
			result.to_csv('{0}.csv'.format(rev_mapper[id_]),encoding='utf-8')
	except tweepy.error.TweepError:
		print(id_)
		
			
