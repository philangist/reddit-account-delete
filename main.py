import utils
import json
from reddit import (
	RedditAPIClient,
	RedditUser,
)

AUTH_ERROR_MESSAGE = """Your account could not be authenticated. Please ensure
that your provided credentials are correct and that Reddit's API is not being
a complete bitch."""

if __name__ == '__main__':
	auth_info = utils.get_auth_info()
	username, password = auth_info['username'], auth_info['password']
	reddit_user = RedditUser(username, password)
	if reddit_user.login():
		reddit_user.download_self()
		print 'Submitted Posts: \n %s \n Comments: \n %s' % (
			str(reddit_user._posts),
			str(reddit_user._comments),
		)

	else:
		print AUTH_ERROR_MESSAGE
