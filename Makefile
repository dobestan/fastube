migrate:
	- python fastube/manage.py makemigrations users posts
	- python fastube/manage.py migrate