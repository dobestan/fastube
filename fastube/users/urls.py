from django.conf.urls import url

from users.views import *


urlpatterns = [
    url(r'^signup/', SignupView.as_view(), name="signup"),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
]
