from django.urls import path
from . import views
from .views import UserEditView, PasswordsChangeView

urlpatterns = [
    #path('url/', call function in views, name for referencing)
    path('jobs/', views.jobs, name="jobs"),
    path('edit_account/', UserEditView.as_view(), name="edit_account"),
    path('about/', views.about, name="about"),
    #path('edit_account/password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('edit_account/password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    #path('', views.base, name="base"),

]
