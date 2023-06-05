import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import os
import base64
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from utils.database import get_db


def build_linear_regression_model():
    df = load_house_listing_data()

    X = df[["bedrooms", "bathrooms", "size", "lot_size", "zipcode"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()

    # fit the model to the training data
    model.fit(X_train, y_train)

    # evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R2 Score: {r2}")

    directory_path = 'data/model/'
    file_name = 'linear_regression_model.pkl'

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, file_name)
    with open(file_path, 'wb') as file:
        pickle.dump(model, file)

    print("Linear regression model built and saved.")


def load_house_listing_data():
    db = get_db()
    collection = db["raw_data"]

    data = list(collection.find())

    df = pd.DataFrame(data)

    return df


def predict_price(features):
    with open("data/model/linear_regression_model.pkl", "rb") as file:
        model = pickle.load(file)

    X = np.array(
        [
            features["bedrooms"],
            features["bathrooms"],
            features["size"],
            features["lot_size"],
            features["zipcode"],
        ]
    ).reshape(1, -1)

    # make the prediction using the trained model
    price_prediction = model.predict(X)

    return price_prediction[0]


def generate_data_analysis():
    try:
        db = get_db()["raw_data"]

        listings = list(db.find())

        # extract the necessary columns for analysis
        prices = [listing["price"] for listing in listings]
        bedrooms = [listing["bedrooms"] for listing in listings]
        bathrooms = [listing["bathrooms"] for listing in listings]
        size = [listing["size"] for listing in listings]
        lot_size = [listing["lot_size"] for listing in listings]

        # generate the three graphs
        price_trend_img = generate_price_trend(prices)
        price_vs_features_img = generate_price_vs_features(
            prices, bedrooms, bathrooms, size, lot_size
        )
        correlation_matrix_img = generate_correlation_matrix(listings)

        return {
            "price_trend": price_trend_img,
            "price_vs_features": price_vs_features_img,
            "correlation_matrix": correlation_matrix_img,
        }
    except Exception as e:
        raise Exception(f"Data analysis failed: {str(e)}")


def generate_price_trend(prices):
    plt.plot(prices)
    plt.xlabel("House")
    plt.ylabel("Price")
    plt.title("Overall Price Trends")

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close()

    img_str = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
    return img_str


def generate_price_vs_features(prices, bedrooms, bathrooms, size, lot_size):
    plt.figure(figsize=(10, 6))
    plt.scatter(bedrooms, prices, label="Bedrooms")
    plt.scatter(bathrooms, prices, label="Bathrooms")
    plt.scatter(size, prices, label="Size")
    plt.scatter(lot_size, prices, label="Lot Size")
    plt.xlabel("Features")
    plt.ylabel("Price")
    plt.title("Price vs Features")
    plt.legend()

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close()

    img_str = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
    return img_str


def generate_correlation_matrix(listings):
    df = pd.DataFrame(listings)

    selected_columns = ["price", "bedrooms", "bathrooms", "size", "lot_size"]
    df_selected = df[selected_columns]

    corr_matrix = df_selected.corr()

    # generate the correlation matrix heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")

    # convert the plot to an image
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close()

    img_str = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
    return img_str
