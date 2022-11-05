from django import template
from django.db.models import Count

from blog.models import Category, Post, Comment

register = template.Library()


def get_all_categories():
    return Category.objects.all()


@register.simple_tag()
def get_list_category():
    """Вывод всех категорий"""
    return get_all_categories()


# @register.inclusion_tag('blog/include/tags/top_menu.html')
# def get_categories():
#     category = get_all_categories()
#     return {"list_category": category}

@register.simple_tag()
def get_last_posts():
    posts = Post.objects.select_related("category").order_by("-id")[:5]
    return posts


@register.simple_tag()
def get_last_comments():
    comments = Comment.objects.select_related("post").order_by("-id")[:5]
    return comments

@register.simple_tag()
def get_top_of_week():
    top_of_week = Post.objects.select_related('category').annotate(comments_count=Count('comment')).order_by('-comments_count')[:5]
    return top_of_week
