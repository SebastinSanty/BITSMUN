"""bitsmun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views as homeviews
from userpanel import views as userpanelviews
import registration

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homeviews.home, name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^dashboard/', userpanelviews.dashboard),
    url(r'^profile/', userpanelviews.SeeProfile, name = 'profile'),
    url(r'^executive_board/', userpanelviews.executive_board, name = 'executive_board'),
    url(r'^executive_board_reg/', userpanelviews.executive_board_reg, name = 'executive_board_reg'),
    url(r'^delegates/', userpanelviews.delegates),
    url(r'^press_members/', userpanelviews.press_members),
    url(r'^updateprofile/', userpanelviews.FillProfile, name = 'fillprofile'),
]
