#import tweepy
# http://tweepy.readthedocs.io/en/v3.5.0/api.html


#auth = tweepy.OAuthHandler('EjIwJyRJGmZ0LkBRrjtWdniPQ', #’dEDe973gTlFuezq15OIBmCZtDu2aPF4tk60qzFCLnYydD3PZbx')
#auth.set_access_token("736454557866295296-#CzqATNPebPknavk9Wfe5DBBuuvWW5Oo","7R7DvZKY1VqHWsDeRWCpbyYVBTOSmaczXdU2qKDoyqHDc")

#api = tweepy.API(auth)

#public_tweets = api.home_timeline()

#print timeline

##for tweet in public_tweets:
##    print tweet.text

#updates status

## api.update_status('Hello world')


##     Status update with media

##     API.update_with_media(filename[, status][, in_reply_to_status_id][, lat][, long][, source][, place_id][, file])


#api.destroy_status(1)

#user = api.get_user("StartsubTr")

#print user


# Returns an array containing the IDs of users following the specified user.
# API.followers_ids(id/screen_name/user_id)

# Returns an array containing the IDs of users being followed by the specified user.
# API.friends_ids(id/screen_name/user_id[, cursor])


# Checks if a friendship exists between two users. Will return True if user_a follows user_b, otherwise False.# API.friends_ids(id/screen_name/user_id[, cursor])
# API.exists_friendship(user_a, user_b)


# Sends a new direct message to the specified user from the authenticating user.
# API.send_direct_message(user/screen_name/user_id, text)

# Returns a specific direct message.
# API.get_direct_message([id][, full_text])
