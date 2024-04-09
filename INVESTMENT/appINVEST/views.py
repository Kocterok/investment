from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio
from .forms import AssetForm
from django.http import HttpResponse

@login_required
def portfolio(request):
    user_portfolio=Portfolio.objects.filter(investor=request.user)
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
