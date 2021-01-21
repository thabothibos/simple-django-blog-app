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
	
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context['cat_menu'] = cat_menu
		return context
	   
def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-',' ')).order_by('-post_date')
	cat_menu = Category.objects.all()             # so as to render the category nav-link in this page
	context = {'cats':cats.title().replace('-',' '), 'category_posts':category_posts, 'cat_menu':cat_menu}
	return render(request, 'categories.html', context)
	

class ArticleView(DetailView):
	model = Post
	template_name = 'detail_view.html'
	
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

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
	
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(EditPostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')
	
	
