
import json   #allows python to "speak" or convert to json
import os   #allows python visibility into our file system

class Business:
    """
    represents a single local business
    Every business we create will have a the same or very similar shape
    """
    def __init__(self, name, address, category, rating):
        self.name     = name
        self.address  = address 
        self.category = category
        self.rating   = rating 

    def __str__(self):
        """
        This is called automatically when we print() a Business
        This is for humans
        """
        return f"{self.name}. | {self.category} | {self.address} |  {self.rating} STARS"
    
    def __repr__(self):
        """
        Called by repr() - this is for developers (more technical humans)
        By convention this looks like the call that would recreate the object.
        """
        return f"Business(name={self.name}, category={self.category})"
    
    def to_dict(self):
        """
        Convert this Business instance to a plain dictionary
        we need to do this to convert to json.
        json.dump()  only understands plain dictionaries
        """
        return {
            "name": self.name,   
            "address": self.address,
            "category": self.category,
            "rating": self.rating,
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Build a Business object FROM a dictionary
        this is gonna do the opposite of what to_dict does

        @classmethod means we call it on the CLASS, not an instance:

        'cls' is the class itself - like 'self' but one level up.
        """
        return cls(
            name = data["name"],
            address = data["address"],
            category = data["category"],
            rating = data["rating"],
        )
    

DATA_FILE = "data/businesses.json"

def save_businesses(businesses):
    """
    save a alist of Businesss OBJECTS to our JSON file
    we need to convert each business to a dict first... JSON is a litte picky about how this is formatted.
    """
    os.makedirs("data", exist_ok=True)    # creates a folder if one doesn't yet exist

    data = [b.to_dict() for b in businesses]

    with open(DATA_FILE, "w") as f:
        json.dump(data,f, indent=2)

    print(f"   SAVED {len(businesses)} businessses")

def load_businesses():
    """
    load businesses from our JSON file
    if there are no business we want this to return an empty list
    """

    if not os.path.exists(DATA_FILE):
        print(" no data file found --- start fresh")
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return [Business.from_dict(item) for item in data]

loaded_businesses = load_business()
for b in load_businesses:
    print(b)
  
