from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/<str:entry>", views.entry_detail, name="entry_detail"),
    path("encyclopedia/new/", views.new_entry, name="new_entry"),
    path("encyclopedia/edit/<str:title>/", views.edit_entry, name="edit_entry"),
    path("encyclopedia/update/<str:title>/", views.update_entry, name="update_entry"),
    path("encyclopedia/save/", views.save_entry, name="save_entry"),
    path("encyclopedia/random/", views.random_entry, name="random_entry"),
    path("encyclopedia/search/", views.search_entry, name="search_entry")
]
