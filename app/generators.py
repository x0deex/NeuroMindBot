from openai import AsyncOpenAI
from config import AITOKEN, BASE_URL

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key= AITOKEN,
    base_url= BASE_URL
)


async def gpt_text(request, model) -> None:
    response = await client.responses.create(
        input=request,
        model=model
    )
    return response.output_text