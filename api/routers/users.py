from fastapi import APIRouter
from fastapi_versioning import version

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
@version(1)
def read_root():
    return {"message": "Users are managed in here."}

@router.get("/")
@version(2)
def read_root():
    return {"message": "Users are managed in here. Version 2"}
