#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = '747482755315834880-B5WEowzhbKMyAV9wKqIeiRkGc0BSgDN'
access_token_secret = 'TXJt5957Wp81fXghNzSUpJoPcic7XcJLhvJrHIEZIUEF7'
consumer_key = 'OtVoYnJ1uYZR9v8EuygGlXNcM'
consumer_secret = '6kVYlRQpFX2vyHziIAowuifKlbhxmvDxvZTq5GtphsTxWFona2'


class StdOutListener(StreamListener):

    def on_data(self, data):
        with open("charity.json",'a') as f:
            f.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)



if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)


    #This line filter Twitter Streams to capture data by the keywords: donation charity
    stream.filter(languages = ["en"],track=['charity','donation','willing to donate'])
	   
