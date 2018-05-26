"""flight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from MonitorFlight import views as FlightViews

urlpatterns = [
    url(r'^index/', FlightViews.index, name='index'),
    url(r'^$', FlightViews.index, name='index'),
    url(r'^video/$', FlightViews.video, name='video'),
    url(r'^video1/$', FlightViews.video1, name='video1'),
    url(r'^video2/$', FlightViews.video2, name='video2'),
    url(r'^LoadPoints/$', FlightViews.LoadPoints, name='LoadPoints'),
    url(r'^LoadHeight/$', FlightViews.LoadHeight, name='LoadHeight'),
    url(r'^LoadHeightLow/$', FlightViews.LoadHeightLow, name='LoadHeightLow'),
    url(r'^LoadHeightMid/$', FlightViews.LoadHeightMid, name='LoadHeightMid'),
    url(r'^LoadHeightHig/$', FlightViews.LoadHeightHig, name='LoadHeightHig'),
]
