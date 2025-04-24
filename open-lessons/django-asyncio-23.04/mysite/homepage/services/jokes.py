import httpx

JOKES_API_URL = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"


async def get_joke() -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(JOKES_API_URL)
    data = response.json()
    return data["joke"]


if __name__ == "__main__":
    print(get_joke())
