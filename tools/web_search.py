import json

import aiohttp
from fastmcp.tools import tool
from pydantic import BaseModel, Field
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from settings import settings
from utils.logger import get_logger, log_before_retrying

logger = get_logger()


class SearchResult(BaseModel):
    """Serper api response schema"""

    title: str = Field(..., description="Title of the search result")
    link: str = Field(..., description="Link of the search result")
    snippet: str = Field(..., description="Snippet of the search result")
    position: int = Field(..., description="Position of the search result")
    date: str | None = Field(default=None, description="Date of the search result")


@tool(name="web_search", description="Search the web for the given query")
@retry(
    reraise=True,
    stop=stop_after_attempt(settings.MAX_RETRIES),
    wait=wait_exponential(),
    before_sleep=log_before_retrying,
)
async def get_serper_organic_search_results(query: str) -> list[SearchResult]:

    if not query or not query.strip():
        raise ValueError("Query cannot be empty")

    payload = json.dumps(
        {
            "q": query,
            "gl": "us",
            "hl": "en",
            "num": 10,
            "type": "search",
        }
    )
    headers = {"X-API-KEY": settings.SERPER_API_KEY, "Content-Type": "application/json"}
    logger.info("Serper API called", extra={"query": query})
    async with aiohttp.ClientSession(trust_env=True) as client:
        timeout = aiohttp.ClientTimeout(total=30.0)
        async with client.post(
            "https://google.serper.dev/search",
            data=payload,
            headers=headers,
            timeout=timeout,
        ) as response:
            response.raise_for_status()
            data = await response.json()
            organic_results = data.get("organic", [])
            return [SearchResult(**result) for result in organic_results]
