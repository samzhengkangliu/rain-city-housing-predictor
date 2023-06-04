from utils.database import get_db

collection = get_db()["raw_data"]

# Define the document model
class Listing:
    def __init__(
        self,
        id,
        price,
        bedrooms,
        bathrooms,
        size,
        size_units,
        lot_size,
        lot_size_units,
        zipcode,
    ):
        self.id = id
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.size = size
        self.size_units = size_units
        self.lot_size = lot_size
        self.lot_size_units = lot_size_units
        self.zipcode = zipcode

    @staticmethod
    def from_dict(data):
        return Listing(**data)

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "size": self.size,
            "size_units": self.size_units,
            "lot_size": self.lot_size,
            "lot_size_units": self.lot_size_units,
            "zipcode": self.zipcode,
        }

    def save(self):
        collection.insert_one(self.to_dict())

    @staticmethod
    def save_all(documents):
        data = [doc.to_dict() for doc in documents]
        collection.insert_many(data)

    @staticmethod
    def find_all():
        cursor = collection.find()
        return [Listing.from_dict(data) for data in cursor]

    @staticmethod
    def find_by_id(id):
        data = collection.find_one({"id": id})
        if data:
            return Listing.from_dict(data)
        return None
