from django.contrib import messages
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            "성공적으로 로그아웃 되었습니다",
        )
        return redirect(reverse("login"))
