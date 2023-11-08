# onecenter-vectara
## TO RUN:

``Install Python on your computer``
## RUN: 
`pip install -r requirements.txt`

## COPY 
``CONTENT OF .env.example to .env``

## CHANGE ONLY THE FOLLOWIG FIELDS WITH YOURS:
``DATABASE_URI``

``OPENAI_API_KEY``

``VECTARA_CUSTOMER_ID``

``VECTARA_APP_ID``

``VECTARA_APP_SECRET``

``VECTARA_API_KEY``

``VECTARA_BASE``

``VECTARA_AUTH_URL``

## RUN: 
`export FLASK_APP=main.py OR set FLASK_APP=main.py`
## RUN MIGRATION: 
`flask db upgrade`
## RUN: 
`flask run`
