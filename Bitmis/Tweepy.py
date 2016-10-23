import tweepy
# http://tweepy.readthedocs.io/en/v3.5.0/api.html


auth = tweepy.OAuthHandler('EjIwJyRJGmZ0LkBRrjtWdniPQ', 'dEDe973gTlFuezq15OIBmCZtDu2aPF4tk60qzFCLnYydD3PZbx')
auth.set_access_token("736454557866295296-CzqATNPebPknavk9Wfe5DBBuuvWW5Oo","7R7DvZKY1VqHWsDeRWCpbyYVBTOSmaczXdU2qKDoyqHDc")

api = tweepy.API(auth)

public_tweets = api.home_timeline()

#print timeline

##for tweet in public_tweets:
##    print tweet.text

#updates status

## api.update_status('Hello world')


##     Status update with media
##     API.update_with_media(filename[, status][, in_reply_to_status_id][, lat][, long][, source][, place_id][, file])


#api.destroy_status('777570628392091648')

#user = api.get_user("StartsubTr")

#print user


##a = api.followers_ids("wom_works")
##
##count = 0
##while count < len(a):
##
##    print a[count]
##    
##    count = count + 1
##    

m = api.get_user(2497871310)

print m.name
    

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


'''
Attributes

dict_proxy({'__module__': 'tweepy.models',
'timeline': <function timeline at 0x1053c8ed8>,
'unfollow': <function unfollow at 0x1053c9140>,
'lists_memberships': <function lists_memberships at 0x1053c91b8>,
'parse_list': <classmethod object at 0x1053c41a0>,
'lists': <function lists at 0x1053c92a8>,
'parse': <classmethod object at 0x1053c4168>,
'followers': <function followers at 0x1053c9050>,
'follow': <function follow at 0x1053c90c8>,
'followers_ids': <function followers_ids at 0x1053c9320>,
'friends': <function friends at 0x1053c8f50>, '__doc__':
None, 'lists_subscriptions': <function lists_subscriptions at 0x1053c9230>}) '''
