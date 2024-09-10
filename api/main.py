from fastapi import FastAPI
from routers import rockets, users
from fastapi_versioning import VersionedFastAPI

app = FastAPI()
app.include_router(rockets.router)
app.include_router(users.router)

# You can also include the routers directly in the FastAPI instance with prefix, tags, dependencies, and responses.
# You also can include same router with multiple prefixes.

@app.get("/")
def read_root():
    return {"message": "Hello world! Welcome to Socket Science. Here we build, load and lunch exciting rocket. You also can build your custom rocket."}

# Path Operation
# Path is the also called as endpoint, it is the URL of the API. Example: /items/1
# Operation is the HTTP method used to access the endpoint. Example: GET, POST, PUT, DELETE
# You can return dict, list, and singular value as string or int. You can also return Pydantic models.
# In path operation order matters. You can not redefine a path operation with same path and same HTTP method. The first one will be used.



app = VersionedFastAPI(app, version_format='{major}', prefix_format='/v{major}')




