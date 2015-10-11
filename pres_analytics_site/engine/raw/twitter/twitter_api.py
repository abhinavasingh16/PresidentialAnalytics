import sys
import os 
from twython import Twython

snaq_secret = 'dFcbmYl0O9yfNgmyM9h6pbjhVgY18lyMsFQXU2aCfNwqiEyXJl' 
snaq_key = 'qid1fBtd1UtI1nSP2rlws7wGa'


if __name__ == "__main__":
	twitter = Twython(APP_KEY, APP_SECRET)
	auth = twitter.get_authentication_tokens(callback_url='http://andrewhollenbach.com')
	OAUTH_TOKEN = auth['oauth_token']
	OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
	auth['auth_url']

