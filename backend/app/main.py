from fastapi import FastAPI, Depends
from app.models.inputs import Inputs
from app.models.outputs import Outputs
from app.calculations import simulate_tdds

app = FastAPI()


@app.get("/")
def index():
    return "Welcome to my application. To calculate the discrete-time dynamical system, GET /calculation."


@app.get("/calculation")
async def calculate(inputs: Inputs = Depends()) -> list[Outputs]:
    response = simulate_tdds(
        x=inputs.x0,
        y=inputs.y0,
        z=inputs.z0,
        sigma=inputs.sigma,
        beta=inputs.beta,
        rho=inputs.rho,
        delta_t=inputs.delta_t,
    )
    return response
