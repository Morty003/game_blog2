from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("category_slug")).select_related('category')


class ReviewView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class Search(ListView):
    """Поиск постов"""
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f"q={self.request.GET.get('q')}"
        return context



