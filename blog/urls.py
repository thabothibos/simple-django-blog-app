from django.urls import path
from . views import HomeView, ArticleView, CategoryView, AddPostView, AddCategoryView, EditPostView, DeletePostView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    
    path('add-category/', AddCategoryView.as_view(), name='add_category'),
    
    
    path('article/edit/<int:pk>', EditPostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name="category"),
    
    path('like/<int:pk>', LikeView, name="like_post"),
]
