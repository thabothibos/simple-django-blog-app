from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
	else:
		post.likes.add(request.user)
		liked = True
		
	return HttpResponseRedirect(reverse('article', args=[str(pk)]))

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
	cat_menu = Category.objects.all()             # so as to render the category nav-link on the page
	context = {'cats':cats.title().replace('-',' '), 'category_posts':category_posts, 'cat_menu':cat_menu}
	return render(request, 'categories.html', context)
	

class ArticleView(DetailView):
	model = Post
	template_name = 'detail_view.html'
	
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleView, self).get_context_data(*args, **kwargs)
		
		item = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes =  item.total_likes()
		
		liked = False
		if item.likes.filter(id=self.request.user.id).exists():
			liked = True
			
		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	success_url = reverse_lazy('home')
	
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
	
class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	#fields = '__all__'
	template_name = "add_comment.html"

	def form_valid(self, form): 
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)
	success_url = reverse_lazy('home')
