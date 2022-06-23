# API pour les fev22cde

## Installation

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Lancement

```shell
python3 -m uvicorn main:api --host=0.0.0.0 --reload
```

## Tests

```shell
# in one terminal
python3 -m uvicorn main:api

# in another terminal
python3 -m pytest tests.py
```
