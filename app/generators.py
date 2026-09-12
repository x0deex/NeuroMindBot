import httpx
from openai import AsyncOpenAI
from config import AITOKEN, BASE_URL, PROXY


client = AsyncOpenAI(
    api_key= AITOKEN,
    base_url= BASE_URL,
    http_client=httpx.AsyncOpenAI(
        proxie=PROXY,
        transport=httpx.HTTPTransport(
        local_address="0.0.0.0"))
)


async def gpt_text(request, model) -> None:
    response = await client.responses.create(
        input=request,
        model=model
    )
    return response.output_text