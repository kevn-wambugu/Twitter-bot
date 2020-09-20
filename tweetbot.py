import tweepy
import time

'''
   The first function serches for a certain keyword and likes the tweets with that keyword.
   The second function follows 50 users of a given account
   The third function unfollows users who dont follow back.
   the three functions are enclosed in a while loop,each function is envoked after 2 hours.
   The access token and authentication handler you get them from your twitter developer account.
   Take care not to violate twitter laws.'''


auth = tweepy.OAuthHandler('First secret key','Second secret key')
auth.set_access_token('First secret key','second secret key')
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()

#a variable that hold something you might want to searc on twitter.
search = 'Curfew in Kenya'
def Like_tweet():
    for tweet in tweepy.Cursor(api.search,search).items(5):
        try:
            tweet.favorite()
            time.sleep(5)
            print("TWEET LIKED!")         
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def follow():
    try:
        for follower in tweepy.Cursor(api.followers,screen_name='username',count=5).items():
            follower.follow()
    except tweepy.TweepError as e:
        print(e.reason)

    
def unfollow_users():
    try:
        people = api.followers_ids()
        friends = api.friends_ids()
        for f in friends:
            if f not in people:
                api.destroy_friendship(f)
    except tweepy.TweepError as e:
        print(e.reason)

while(True):
    Like_tweet()
    time.sleep(7200)
    follow()
    time.sleep(7200)
    unfollow_users()
    break
