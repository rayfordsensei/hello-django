from django.http import Http404, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")


texts = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Pellentesque sit amet nunc aliquet, tincidunt sem eget, commodo mauris.",
    "Suspendisse imperdiet justo sed facilisis suscipit.",
]


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])

    raise Http404("No such section")
