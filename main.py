import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from Routers import User

app = FastAPI(
    title="pickup",
    version="v0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(User.router)


# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload='true')