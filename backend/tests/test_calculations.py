from app.calculations import calculate_x, calculate_y, calculate_z, simulate_tdds
import pytest


@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        pytest.param(
            {"x": 1, "y": 1, "z": 1, "sigma": 1, "delta_t": 1},
            1,
            id="simple_calculation_of_x",
        ),
        pytest.param(
            {"x": 2, "y": 4, "z": 0.5, "sigma": 3, "delta_t": 2},
            8,
            id="complex_calculation_of_x",
        ),
    ],
)
def test_calculate_x(input_values, expected_output):
    assert calculate_x(**input_values) == expected_output


@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        pytest.param(
            {"y": 1, "x": 1, "rho": 1, "z": 1, "delta_t": 1},
            0,
            id="simple_calculation_of_y",
        ),
        pytest.param(
            {"y": 2, "x": 4, "rho": 0.5, "z": 3, "delta_t": 2},
            -30,
            id="complex_calculation_of_y",
        ),
    ],
)
def test_calculate_y(input_values, expected_output):
    assert calculate_y(**input_values) == expected_output


@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        pytest.param(
            {"z": 1, "x": 1, "y": 1, "beta": 1, "delta_t": 1},
            1,
            id="simple_calculation_of_z",
        ),
        pytest.param(
            {"z": 2, "x": 4, "y": 0.5, "beta": 3, "delta_t": 2},
            -6,
            id="complex_calculation_of_z",
        ),
    ],
)
def test_calculate_z(input_values, expected_output):
    assert calculate_z(**input_values) == expected_output


def test_simmulate_tdds(simple_simmulation_results):
    given = {"x": 1, "y": 1, "z": 1, "sigma": 1, "rho": 1, "beta": 1, "delta_t": 1}
    assert simulate_tdds(**given) == simple_simmulation_results
