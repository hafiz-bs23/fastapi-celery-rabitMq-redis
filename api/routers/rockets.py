from fastapi import APIRouter, Body, Query
from enum import Enum
from typing import Annotated
from models.request_models import BuildRocket

router = APIRouter(
    prefix="/rockets",
    tags=["rockets"],
    responses={404: {"description": "Not found"}}
)
# We also can add dependencies applicable to all path operations in the router.
# If you have multiple dependencies, the router dependency will execute first.

class RocketModel(str, Enum):
    type1 = "Falcon 9"
    type2 = "Falcon Heavy"
    type3 = "Starship"
    type4 = "New Glenn"
    type5 = "New Shepard"
    type6 = "Vulcan Centaur"


@router.get("/")
def default():
    return {"message": "All you want in life is rocket? You are in the right place"}


# Path parameter
# Used in path, Type validation is also possible.
 
@router.get("/get_info_by_id/{rocket_id}")
def rocket_info(rocket_id: int):
    return {
        "rocket_id": rocket_id
        }
# In case your path parameter can take predefined values, you can use Enum.

@router.get("/get_info_by_type/{rocket_type}")
def rocket_info_with_type(rocket_type: RocketModel):
    return {
        "rocket_type": rocket_type
        }
    
# Query parameter
# Function parameters that are not part of the path will be interpreted as query parameters.
# The query is the key-value pair that comes after the question mark in the URL.
# Type declared values are validated and converted to the declared type.
# You can also set default values for query parameters.
# You can also set optional query parameters by setting the default value to None.
# A bool type query parameter can be passed as true, false, 1, 0, on, off, yes, no.
# Any parameter with default value is optional.
# You can take multiple query parameters in the same method with same name. /q=123&q=456 is also excepted. But define q: list[str] this way.

@router.get("/get_details_by_id/{rocket_id}")
def rocket_details(rocket_id: int,description_type: str = "short", language: str | None = None):
    return {
        "rocket_id": rocket_id,
        "name": name
    }  

# Request body
# When you receive data from client, you receive it in the request body.
# POST, PUT, DELETE, PATCH methods can have request body.
# FastAPI use pydantic models to declare request body and also validate the data.

@router.post("/build_rocket/")
def build_rocket(build_rocket: BuildRocket):
    return {
        "rocket": build_rocket.rocket,
        "payload": build_rocket.payload,
        "budget": build_rocket.budget,
        "pre_pay_amount": build_rocket.pre_pay_amount,
        "deployment_date": build_rocket.deployment_date
    }
    
# You can also take data from body without pydantic model.
# For that you have to use Annotated type in the method parameter.
# For example I wat the know the current status of my rocket, and I will pass the rocket_id in the body.
# This scenario is useful when you have only one parameter in the body.
@router.post("/rocket_status/")
def rocket_status(rocket_id: Annotated[int, Body()]):
    return {
        "rocket_id": rocket_id
    }
    
# If you need to validate the Query params and the string, There are ways for that.
# You can check max length, min length, pattern, etc.
# In the previous example, we have seen how to validate the query param, say the length of the rocket it is 8.
# ... is used to specify that the query parameter is required.
# We can also add some more metadata to the query parameter. like title, description, alias, deprecated, hide_in_schema etc.
# Alias is used to change the name of the query parameter in the URL. By default, it is the same as the variable name. Alias name will be in the URL.
# Deprecated is used to mark the query parameter as deprecated. It will be shown in the documentation. You need to assign a boolean value to it.
# hide_in_schema is used to hide the query parameter in the documentation. You need to assign a boolean value to it.

@router.get("/rocket_status/")
def rocket_status(
    rocket_id: Annotated[
        int, 
        Query(
            title="Rocket ID",
            alias="rocket-id",
            description="This is the unique ID of the rocket",
            min_length=8,
            max_length=8
            )
        ] = ...
    ):
    return {
        "rocket_id": rocket_id
    }
