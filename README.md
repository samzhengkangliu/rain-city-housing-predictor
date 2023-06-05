# rain-city-housing-predictor
Final project for Applications of Software Architecture for Big Data

## Prerequisites
- Python 3.7 or higher
- Node 
- MongoDB
- Kaggle API credentials (for dataset download)

## Getting Started
1. It's recommended to use `venv` so you don't mess up with your local python environment
```
python3 -m venv venv && source venv/bin/activate
```

2. Install required packages through `pip`
```
pip install -r requirements.txt
```

3. After successful instanlation, simply use `flask run` or `gunicorn app:app` to start the app in your local.

4. You can navigate to http://localhost:5000 (or `8000` if you use `gunicorn`). Use `curl` or Postman to query the APIs

## List of APIs you can use
You can navigate to http://localhsot:5000/swagger for a list of APIs. (In progress work and sorry you can't directly interact with the swagger UI yet)
