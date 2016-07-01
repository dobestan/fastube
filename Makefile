migrate:
	- python fastube/manage.py makemigrations users posts tags notifications
	- python fastube/manage.py migrate


test:
	- pep8 . -v
	- python fastube/manage.py test users posts tags -v2