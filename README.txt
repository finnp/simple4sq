This is a ultralightweight foursquare API wrapper - which is a little bit different.

If you're looking for something more serious I recommend https://github.com/mLewisLogic/foursquare.

Usage:
import simple4sq
simple4sq.cred = ('CLIENT_ID', 'CLIENT_SECRET', 'REDIRECT_URI')
# Redirect user to
print simple4sq.oauth_url()
# Insert the response code into
simple4sq.download_token(code)
# Start requesting
user = simple4sq.request('user/self')
print user['response']['user']['firstName']

