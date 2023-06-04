import csv
import kaggle
from models.listing import Listing
from utils.database import get_db


def collect_data():
    try:
        db = get_db()["raw_data"]

        download_dataset()

        csv_path = "data/raw/train.csv"

        with open(csv_path, "r") as file:
            reader = csv.reader(file)

            # clear the existing collection
            db.delete_many({})

            # match the indices of the required columns
            beds_index = 0
            baths_index = 1
            size_index = 2
            size_units_index = 3
            lot_size_index = 4
            lot_size_units_index = 5
            zip_code_index = 6
            price_index = 7

            # Skip the header row
            next(reader)

            # iterate over each row in the CSV data
            for row in reader:
                listing = Listing(
                    id=reader.line_num,
                    price=float(row[price_index]),
                    bedrooms=int(row[beds_index]),
                    bathrooms=float(row[baths_index]),
                    size=float(row[size_index]),
                    size_units=str(row[size_units_index]),
                    lot_size=float(row[lot_size_index]) if row[lot_size_index] != '' else 0.0,
                    lot_size_units=str(row[lot_size_units_index]) if row[lot_size_units_index] != None else '',
                    zipcode=int(row[zip_code_index]),
                )

                db.insert_one(listing.to_dict())

        print("Data collection completed.")
        return
    except Exception as e:
        raise Exception(f"Data collection failed: {str(e)}")


def download_dataset():
    dataset_name = "samuelcortinhas/house-price-prediction-seattle"
    destination_folder = "data/raw/"
    kaggle.api.dataset_download_files(dataset_name, path=destination_folder, unzip=True)
    print("Dataset downloaded successfully.")
