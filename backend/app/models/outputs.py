from pydantic import BaseModel
from decimal import Decimal


class Outputs(BaseModel):
    """
    This is the schema built in pydantic for the response
    """

    N: Decimal
    X: Decimal
    Y: Decimal
    Z: Decimal
