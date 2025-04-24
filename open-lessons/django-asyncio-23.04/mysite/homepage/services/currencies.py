from decimal import Decimal

import httpx

CURRENCIES_API_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currency}.json"


async def get_exchange_rates(currency: str) -> dict[str, Decimal]:
    currency = currency.lower()
    url = CURRENCIES_API_URL.format(currency=currency)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    data = response.json(parse_float=Decimal)
    return data[currency]


async def get_currency_exchange_rates(
    currency: str,
    *to_currencies: str,
) -> dict[str, Decimal]:
    rates = await get_exchange_rates(currency)
    res = {}
    for to_currency in to_currencies:
        to = to_currency.lower()
        res[to] = rates[to]
    return res
