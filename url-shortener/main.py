from fastapi import (
    FastAPI,
    Request,
)

from api import router as api_router
from api.redirect_views import router as redirect_views

app = FastAPI(
    title="URL Shortener",
)
app.include_router(redirect_views)
app.include_router(api_router)


@app.get("/")
def read_root(
    request: Request,
    name: str = "World",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"Hello {name}",
        "docs": str(docs_url),
    }
