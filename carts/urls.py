from django.conf.urls import url

from .views import (
        cart_home, 
        cart_update, 
        checkout_home,
        checkout_done_view,
        checkout_handle_view
        )

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^response/$', checkout_handle_view, name='response'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
]

