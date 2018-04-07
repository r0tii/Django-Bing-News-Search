from django.shortcuts import render
from .supportscripts.bing_search import run_query
from .models import SearchTerm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string


def home(request):

    query = request.POST.get('q')

    if request.method == 'POST':
        recent_searches = SearchTerm.objects.order_by('-time')[:10]

        if query:
            articles = run_query(query)
            term = SearchTerm(term=query)
            term.save()
            html = render_to_string('search_results.html', {'articles': articles, 'query': query, 'recent_searches': recent_searches}, request)

            return HttpResponse(html)
    else:
        return render(request, 'index.html', {'query': query,})