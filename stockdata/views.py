from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import StockData
from .form import StockDataForm


# Create your views here.
def search_stock_view(request):
    query_dict = request.GET  # This is a dictionary
    query = query_dict.get('q')  # <input type='text' name='q'/>
    stockdata_obj = None
    if query is not None:
        stockdata_obj = StockData.objects.get(title=query)
    context = {
        'users': 'BaroN',
        'stockdata_obj': stockdata_obj
    }

    return render(request, 'stockdata/search.html', context)


@login_required
def create_stock_view(request):
    form = StockDataForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # stockdata_obj = StockData(title=title, content=content)  # Old form method
        stockdata_obj = form.save()  # Django form method
        context['form'] = StockDataForm()

        context['users'] = 'BaroN'
        context['stockdata_obj'] = stockdata_obj
        context['created'] = True

    return render(request, 'stockdata/create.html', context)


# def create_stock_view(request):
#     form = StockDataForm()
#     context = {
#         'form': form
#     }
#     if request.method == 'POST':
#         stockdata_obj = None
#         form = StockDataForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             if title and content is not None:
#                 stockdata_obj = StockData(title=title, content=content)
#                 stockdata_obj.save()
#
#             context['users'] = 'BaroN'
#             context['stockdata_obj'] = stockdata_obj,
#             context['created'] = 'TRUE'
#
#     return render(request, 'stockdata/create.html', context)


def detail_stock_view(request, stock_title=None):
    stockdata_obj = None
    if stock_title is not None:
        stockdata_obj = StockData.objects.get(title=stock_title)
    context = {
        'users': 'BaroN',
        'stockdata_obj': stockdata_obj
    }
    return render(request, 'stockdata/detail-stock-view.html', context)
