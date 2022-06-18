from django.shortcuts import redirect, render
from .models import Desk
from django.contrib import messages
from mainapp.models import Stock
# Create your views here.
def home(request):
    if request.method == 'POST':
        print('post request detected ')
        desk_number = request.POST['desk_number']
        desk_password = request.POST['desk_password']
        print(desk_number)
        print(desk_password)
        desk_object = 'not changed'
        try:
            desk_object = Desk.objects.get(desk_number = desk_number)
            if desk_object.desk_password == desk_password:
                    return redirect(dashboard)
            else:
                if desk_object.desk_password != desk_password:
                    messages.error(request, "desk number and password does not match")
                    
        except Desk.DoesNotExist:
            if desk_object == None:
                messages.error(request, "wrong desk number")
                   

        
    return render(request, 'desk_homepage.html')


def dashboard(request):
    return render(request, 'desk_dashboard.html')


def desk_stocklist(request):
    stock_list = Stock.objects.all()
    context = []
    for stock in stock_list:
        context.append({'stock_name' : stock.stock_name, 'stock_price' : stock.stock_price})
        
    return render(request, 'desk_stocklist.html', {'stocks' : context})