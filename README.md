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

## API Endpoints

- POST /api/data/collect

    Collects the house price dataset from Kaggle and stores it in the MongoDB database.

- GET /api/analysis/trends

    Returns an image displaying the overall price trends over time.

- GET /api/analysis/price_vs_features

    Returns an image displaying the price distribution based on different features.

- GET /api/analysis/correlation_matrix

    Returns an image displaying the correlation matrix among the features and price.

- POST /api/analysis/predict

    Accepts a JSON object containing the house features and returns the predicted price.

- GET /api/health

    Returns the health status of the app

- GET /api/metrics
  
    Generate Prometheus metrics