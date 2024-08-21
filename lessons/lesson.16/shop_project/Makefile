test:
	python manage.py test

coverage:
	coverage run --source='.' manage.py test
	coverage report --omit=shop_project/asgi.py,shop_project/wsgi.py,manage.py --fail-under=77
	coverage html --omit=shop_project/asgi.py,shop_project/wsgi.py,manage.py
