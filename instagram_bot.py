from instapy import InstaPy
from instapy import smart_run

my_username = '11.7khg_sample'
my_password = 'Lot05usetoabmf'

session = InstaPy(username = my_username, 
	password = my_password,
	headless_browser = False)

with smart_run(session):
	session.set_relationship_bounds(enabled=True,
		delimit_by_numbers=True,
		max_followers=500,
		min_followers=30,
		min_following=50)

	session.set_do_follow(True, percentage=100)
	session.set_dont_like(['cars', 'kia', 'ford'])

	session.like_by_tags(['fallootd', 'petitestyle'], amount=10)
