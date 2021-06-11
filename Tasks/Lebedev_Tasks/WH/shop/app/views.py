from app.forms import AddElement
from django.shortcuts import render, redirect
from .models import Element
from django.contrib.auth.decorators import permission_required
from .forms import AddElement


# Create your views here.

def home(request):
    return render(request, "home.html")

def catalog(request):
    Elements = Element.objects.all()[::-1]
    return render(request, "catalog.html", {'title':'Каталог', 'Elements': Elements})

def post(request, post_id):

    el = Element.objects.get(id=post_id)

    return render(request, 'post.html', {'el': el, 'title': f'Post {el.id}'})

@permission_required('app.add_post')
def add_post(request):

    form = AddElement()

    if request.method == "POST":
        form = AddElement(request.POST, request.FILES)

        if form.is_valid():

            post_entry = Element()
            post_entry.title = form.cleaned_data['title']
            post_entry.color = form.cleaned_data['color']
            post_entry.Producer_Name = form.cleaned_data['Producer_Name']
            post_entry.size = form.cleaned_data['size']
            post_entry.structure = form.cleaned_data['structure']
            post_entry.price = form.cleaned_data['price']
            post_entry.image = form.cleaned_data['image']



            post_entry.save()

            return redirect('catalog')

    return render(request, 'add_post.html', {'form': form})



