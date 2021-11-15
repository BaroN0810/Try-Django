"""
To render HTML webpages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string

from stockdata.models import StockData


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return a response)
    """
    stock_list = StockData.objects.all()

    CONTEXT = {
        'users': 'BaroN',
        'stock_list': stock_list,
    }

    ## NO TEMPLATE
    # HTML_STRING = """
    #     <h1> Hello {users}!</h1>
    #     <p> Stock name:{title}  price:{content} </p>
    #     """.format(**CONTEXT)

    ## DJANGO TEMPLATE
    HTML_STRING = render_to_string('home-view.html', context=CONTEXT)

    return HttpResponse(HTML_STRING)
