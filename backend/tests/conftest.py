from app.models.outputs import Outputs
from tests.constants import SIMPLE_SIMULATION
import pytest


@pytest.fixture
def request_inputs():
    return "?x0=1&y0=2&z0=3&sigma=4&rho=5&beta=1&delta_t=2"


@pytest.fixture
def simple_simmulation_results():
    simple_simulation = list()
    for result in SIMPLE_SIMULATION:
        simple_simulation.append(Outputs(**result))
    return simple_simulation
