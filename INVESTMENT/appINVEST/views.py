from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Asset
from .forms import AssetForm
from django.http import HttpResponse

@login_required
def portfolio(request):
    user_portfolio = Portfolio.objects.filter(investor=request.user)
    total_value = sum(item.total_value() for item in user_portfolio)
    context={'portfolio':user_portfolio,'total_value':total_value}
    return render(request, 'appINVEST/portfolio.html',context)

@login_required
def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.investor = request.user
            asset.save()
            return redirect('portfolio')
    else:
        form = AssetForm()
    return render(request, 'appINVEST/add_asset.html', {'form': form})

@login_required
def delete_asset(request, asset_id):
    asset = Portfolio.objects.get(id=asset_id)
    asset.delete()
    return redirect('portfolio')
    
def index(request):
    return render(request,'appINVEST/index.html')
def abaut(request):
    return render(request,'appINVEST/about.html')




# def portfolio_view(request):
#     user=request.user
#     portfolio=Portfolio.objects.get_or_create(user=user)
#     assets=portfolio[0].assets.all()

#     total_value = sum(asset.price * asset.quantity for asset in assets)
#     return render(request, 'portfolio.html', {'assets': assets, 'total_value': total_value})

# def add_asset(request):
#     if request.method == 'POST':
#         user = request.user
#         asset_ticker = request.POST.get('ticker')
#         asset_quantity = int(request.POST.get('quantity'))
#         price = float(request.POST.get('price'))
        
#         asset, created = Asset.objects.get_or_create(ticker=asset_ticker, defaults={'name': asset_ticker})
#         asset.quantity += asset_quantity
#         asset.price = price
#         asset.save()
        
#         portfolio = Portfolio.objects.get_or_create(user=user)
#         portfolio.assets.add(asset)
        
#         return redirect('portfolio_view')

#     return render(request, 'add_asset.html')

# def remove_asset(request, asset_id):
#     user = request.user
#     portfolio = Portfolio.objects.get(user=user)
#     asset = Asset.objects.get(pk=asset_id)
#     portfolio.assets.remove(asset)
    
#     return redirect('portfolio_view')