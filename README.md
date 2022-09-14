
```shell
 docker-compose up -d --build
```


```shell
docker-compose exec web python manage.py migrate --noinput

```


```shell
docker-compose exec web python manage.py createsuperuser 

```


###CREATE TEST

```shell
docker-compose exec web_1 python manage.py test

```




### Run all the tests
```shell
python manage.py test 
```

### Run all the tests found within the 'tests' package
```shell
python manage.py test tests
```

### Run all the tests in the tests.test_view_index module
```shell
python manage.py test tests.test_view_index
```

### Run just one test case
```shell
python manage.py test tests.test_view_index.PostIndexView
```


### Run just one test method
```shell
python manage.py test tests.test_view_index.PostIndexView.test_no_post
```

