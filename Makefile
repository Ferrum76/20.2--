migrate: migrations
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations

run:
	python3 manage.py runserver

dumpdata:
	 python3 -Xutf8 manage.py dumpdata catalog > fixtures/catalog_data.json

populate:
	python3 manage.py populate_catalog

shell:
	python3 manage.py shell