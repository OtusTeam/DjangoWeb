import asyncio

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from homepage.models import Profile
from homepage.services.currencies import get_currency_exchange_rates
from homepage.services.jokes import get_joke


class HomeView(TemplateView):
    template_name = "homepage/home.html"


@login_required()
async def dashboard(request: HttpRequest) -> HttpResponse:
    user = request.user
    async with asyncio.TaskGroup() as tg:
        profile = tg.create_task(
            Profile.objects.select_related("user").aget(user=user),
        )
        currency_rates = tg.create_task(
            get_currency_exchange_rates(
                "rub",
                "JPY",
                "BTC",
            )
        )
        joke = tg.create_task(get_joke())

    context = dict(
        profile=profile.result(),
        currencies=currency_rates.result(),
        joke=joke.result(),
    )
    return render(
        request=request,
        template_name="homepage/dashboard.html",
        context=context,
    )
