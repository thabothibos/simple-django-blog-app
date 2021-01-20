from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']
	#ordering = ['-id']

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-',' '))
	context = {'cats':cats.title().replace('-',' '), 'category_posts':category_posts}
	return render(request, 'categories.html', context)

class ArticleView(DetailView):
	model = Post
	template_name = 'detail_view.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	
class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'

class EditPostView(UpdateView):
	model = Post
	form_class = EditForm			#fields are specified in the form
	template_name = 'update_post.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')
