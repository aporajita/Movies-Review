from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.movies, name="movies"),
    path('snippet/<id>', views.Snippet, name="snippet"),
    path('category/<id>', views.categoryList, name="category"),   
    path('registered/', views.signupPage, name="signup"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),


]
