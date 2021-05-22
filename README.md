# prediction-api-service-concept
building and recording a process about development a prediction API service.

Note:
    if you don't have pipenv, just run command without `pipenv run`


## Setup Develop mode

```
~$ pipenv run python setup.py develop --user
```

## Train Model

```
~$ pipenv run python scripts/train.py
```

## Generate Model List

```
~$ pipenv run python scripts/list_model.py
```

## Setup API service

```
~$ pipenv run python app.py
```

## Pytest

```
~$ pipenv run pytest
```

## API Example


### Browser

```
http://localhost:8080/predict/category/iris?sepal_length=5.1&sepal_width=3.4&petal_length=7.5&petal_width=2.1
```


### Curl

```
curl --location --request GET 'http://localhost:8080/predict/category/iris?sepal_length=5.1&sepal_width=3.4&petal_length=7.5&petal_width=2.1'
```

### Python - Requests

```
import requests

url = "http://localhost:8080/predict/category/iris?sepal_length=5.1&sepal_width=3.4&petal_length=7.5&petal_width=2.1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```