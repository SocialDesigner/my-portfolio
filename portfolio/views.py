from django.shortcuts import render

def post_list(request):
     return render(request, 'portfolio/post_list.html', {})
