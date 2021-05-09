from django.shortcuts import render


def index(request):
    """ helper method to get the version information into the top-view """
    content = dict(
    )
    return render(request, 'index.html', context=content)
