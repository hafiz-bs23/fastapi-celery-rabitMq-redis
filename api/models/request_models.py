from pydantic import BaseModel


class RocketBase(BaseModel):
    rocket_Id: int
    rocket_name: str
    rocket_type: str
    has_payload: bool

class PayloadBase(BaseModel):
    payload_Id: int
    payload_name: str
    payload_type: str
    payload_weight: float


class BuildRocket(BaseModel):
    rocket: RocketBase
    payload: PayloadBase
    budget: float
    pre_pay_amount: float | None = None
    deployment_date: str | None = None