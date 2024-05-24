from django.shortcuts import render

def post_list(request):
    return render(request, 'base/post_list.html', {})

