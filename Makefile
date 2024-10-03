migrate: migrations
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations

run:
	python3 manage.py runserver

dump: dump-category dump-product dump-blog

dump-category:
	 python3 -Xutf8 manage.py dumpdata catalog.category > catalog/fixtures/categories.json

dump-product:
	 python3 -Xutf8 manage.py dumpdata catalog.product > catalog/fixtures/products.json

dump-blog:
	 python3 -Xutf8 manage.py dumpdata blog.blog > blog/fixtures/blogs.json

populate: populate_catalog populate_blog

populate_catalog:
	python3 manage.py populate_catalog

populate_blog:
	python3 manage.py populate_blog

shell:
	python3 manage.py shell