from pydantic import BaseModel
from decimal import Decimal


class Inputs(BaseModel):
    """
    Pydantic class that validates the request from the user.
    In case the user passes a wrong type, i.e., a string, the request will fail.
    """

    x0: Decimal
    y0: Decimal
    z0: Decimal
    sigma: Decimal
    rho: Decimal
    beta: Decimal
    delta_t: Decimal
