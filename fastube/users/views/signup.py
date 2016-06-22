from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "users/signup.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        phonenumber = request.POST.get("phonenumber")

        # TODO: validations ( username )

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            phonenumber=phonenumber,
        )

        messages.add_message(
            request,
            messages.SUCCESS,
            settings.SIGNUP_SUCCESS_MESSAGE,
        )

        return redirect(reverse("users:login"))
