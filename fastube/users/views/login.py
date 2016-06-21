from django.views.generic import View
from django.shortcuts import render


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "users/login.html",
            context={},
        )
