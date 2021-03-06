"""only_company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from city_person import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.show_persons, name='home'),
    path('cities/', views.show_cities, name='cities'),
    path('biggest/', views.show_biggest, name='biggest'),
    path('events/', views.event_list, name='events'),
    path('selcity/', views.select_city, name='selcity'),
]

if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
