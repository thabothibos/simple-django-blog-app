from django.urls import path
#from . import views
from . views import HomeView, ArticleView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]
