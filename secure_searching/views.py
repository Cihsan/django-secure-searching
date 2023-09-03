from django.shortcuts import render
from content.models import Content
from django.db.models import Q
from django.views.generic import ListView, DetailView
def home(request):
    contents = Content.objects.all()
    count = contents.count()
    context={'contents':contents,'count':count}
    return render(request, 'home.html',context)

# def search(request):
#     context={}
#     if 'keyword' in request.GET:
#         keyword = request.GET['keyword']
#         if keyword:
#             contents = Content.objects.order_by('-created_date').filter(Q(name__icontains=keyword))
#             count = contents.count()
#             context={'contents':contents,'count':count}
#     return render(request, 'search/home.html',context)

# def search(request):
#     keyword = request.GET.get('keyword', '')  # Default to an empty string if 'keyword' is not present

#     contents = []
#     count = 0

#     if keyword:
#         # Use the Q object to perform a case-insensitive search on the 'name' field
#         contents = Content.objects.filter(Q(name__icontains=keyword)).order_by('-created_date')
#         count = contents.count()

#     return render(request, 'content.html', {'contents': contents, 'count': count})

# def search(request):
#     # Check if the request is a post request.
#     if request.method == 'POST':
#         # Retrieve the search query entered by the user
#         search_query = request.POST['search_query']
#         # Filter your model by the search query
#         contents = Content.objects.filter(fieldName__contains=search_query)
#         count = contents.count()
#         return render(request, 'content.html', {'query':search_query, 'contents':contents,'count':count})
#     else:
#         return render(request, 'content.html',{})

# def search(request):
#     if request.method == 'POST':
#         search_query = request.POST['search_query']
#         contents = Content.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
#         count = contents.count()
#         return render(request, 'home.html', {'query':search_query, 'contents':contents, 'count':count} )
#     else:
#         return render(request, 'home.html',{})

# def search(request):
#     query=request.GET['query']
#     result=Content.objects.filter(name__icontains=query)
#     contents={'result':result}
#     return render(request,'home..html',contents)

class search(ListView):
    model = Content
    template_name = 'home.html'
    context_object_name = 'contents'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Content.objects.filter(name__icontains=query).order_by('-created_at')

class itemDetailView(DetailView):
    model = Content
    context_object_name = 'content'
    template_name = 'detail.html'