from fastapi import FastAPI

from prisma import Prisma

app = FastAPI()

prisma = Prisma(auto_register=True)


@app.get("/")
async def root() -> None:
    """GET API Request with no path."""
    return {"message": "Your app is working!"}


@app.on_event("startup")
async def startup() -> None:
    """Items to be executed before the application starts up."""
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """Items to be executed when the application is to shut down."""
    if prisma.is_connected():
        await prisma.disconnect()


# https://fastapi.tiangolo.com/tutorial/testing/?h=testing#testing
