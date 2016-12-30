from django.conf.urls import url
from django.contrib import admin

from views import BookView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', BookView.as_view())
]
