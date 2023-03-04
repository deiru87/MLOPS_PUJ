from pydantic import BaseModel


class House(BaseModel):
    bedrooms: float = 8.0
    bathrooms: float = 0.57
    sqft_living: float = 0.23
    sqft_lot: float = 3.2
    floors: float = 0.073
    waterfront: float = 17.0
    view: float = 119.0
    condition: float = 0.99675
    sqft_above: float = 3.26
    sqft_basement: float = 0.57
    yr_built: float = 9.3
    yr_renovated: float = 9.3
