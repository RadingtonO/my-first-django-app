from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import *
from .models import *

categories = Categories.objects.all()


def main_list(request):
    articles = Articles.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/index.html', {'articles': articles, 'categories': categories})


def detail_articles(request, category_id):
    articles = Categories.objects.filter(id=category_id)[0].articles_set.all()
    category = Categories.objects.filter(id=category_id)[0].title
    return render(request, 'articles/detail.html', {'articles': articles, 'categories': categories,
                                                    'category': category})


def results_articles(request, article_id):
    article = Articles.objects.filter(id=article_id)
    return render(request, 'articles/results.html', {'article': article[0], 'categories': categories})


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = 'articles/index.html'
    template_name = 'articles/register.html'

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


class LoginView(TemplateView):
    template_name = 'articles/login.html'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)
