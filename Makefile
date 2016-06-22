migrate:
	- python fastube/manage.py makemigrations users posts
	- python fastube/manage.py migrate


test:
	- pep8 . -v
	- python fastube/manage.py test users posts -v2