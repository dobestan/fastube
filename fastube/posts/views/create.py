from django.views.generic import View
from django.shortcuts import render


class PostCreateFormView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "posts/new.html",
            context={},
        )


class PostCreateConfirmView(View):
    pass
