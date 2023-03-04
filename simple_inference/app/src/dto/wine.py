from pydantic import BaseModel


class Wine(BaseModel):
    fixed_acidity: float = 8.0
    volatile_acidity: float = 0.57
    citric_acid: float = 0.23
    residual_sugar: float = 3.2
    chlorides: float = 0.073
    free_sulfur_dioxide: float = 17.0
    total_sulfur_dioxide: float = 119.0
    density: float = 0.99675
    pH: float = 3.26
    sulphates: float = 0.57
    alcohol: float = 9.3
