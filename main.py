from pathlib import Path

from fastmcp import FastMCP
from fastmcp.server.providers import FileSystemProvider
from starlette.requests import Request
from starlette.responses import JSONResponse

from settings import settings

provider = FileSystemProvider(
    root=Path(__file__).parent / "tools",
    reload=bool(settings.DEBUG),
)

mcp = FastMCP("MCP-Server", providers=[provider])


@mcp.custom_route("/", methods=["GET"])
async def health_check(_request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


app = mcp.http_app()
