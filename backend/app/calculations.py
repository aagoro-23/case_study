from app.models.outputs import Outputs
from decimal import Decimal


def calculate_x(
    x: Decimal, y: Decimal, z: Decimal, sigma: Decimal, delta_t: Decimal
) -> Decimal:
    return x + z * sigma * (y - x) * delta_t


def calculate_y(
    y: Decimal, x: Decimal, rho: Decimal, z: Decimal, delta_t: Decimal
) -> Decimal:
    return y + (x * (rho - z) - z * y) * delta_t


def calculate_z(
    z: Decimal, x: Decimal, y: Decimal, beta: Decimal, delta_t: Decimal
) -> Decimal:
    return z + (x * y - beta * z) * delta_t


def simulate_tdds(
    x: Decimal,
    y: Decimal,
    z: Decimal,
    sigma: Decimal,
    beta: Decimal,
    rho: Decimal,
    delta_t: Decimal,
) -> list[Outputs]:
    """Performs 20 steps of simulation for a discrete-time dynamical system following the equations
    for x_n, calculated by calculate_x; y_n calculated by calculate_y; an z_n calculated by calculate_z.
    where x, y, and z represent the position of a point in three dimensions at time n

    :param x: Coordinate value for point in three dimensional space
    :type x: Decimal
    :param y: Coordinate value for point in three dimensional space
    :type y: Decimal
    :param z: Coordinate value for point in three dimensional space
    :type z: Decimal
    :param sigma: Free user-defined parameter
    :type sigma: Decimal
    :param beta: Free user-defined parameter
    :type beta: Decimal
    :param rho: Free user-defined parameter
    :type rho: Decimal
    :param delta_t: Discrete timestep in discrete-time dynamical system
    :type delta_t: Decimal
    :return: List of 20 pydantic-typed steps of each simmulation, calculating the location of each coordinate (of X,Y,Z) per each simulation step at time N
    :rtype: list[Outputs]
    """
    response = list()
    for n in range(20):
        outputs = dict()
        x_n = calculate_x(x=x, y=y, z=z, sigma=sigma, delta_t=delta_t)
        y_n = calculate_y(y=y, x=x, rho=rho, z=z, delta_t=delta_t)
        z_n = calculate_z(z=z, x=x, y=y, beta=beta, delta_t=delta_t)
        outputs["N"] = n
        outputs["X"] = x_n
        outputs["Y"] = y_n
        outputs["Z"] = z_n
        response.append(Outputs(**outputs))
        x, y, z = x_n, y_n, z_n
    return response
