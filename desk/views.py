from django.shortcuts import redirect, render
from .models import Desk
from django.contrib import messages
from mainapp.models import Stock, Team
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
    stock_list = Stock.objects.all()
    context_list = []
    for stock in stock_list:
        context_list.append({'stock_name' : stock.stock_name, 'stock_price' : stock.stock_price})
    context = {'stocks' : context_list} 

    #handling post request
    if request.method == 'POST':
        #getting the information sent through post request
        team_number = request.POST['team_number']
        stock_name = request.POST['stock_name']
        transaction_type = request.POST['transaction_type']
        quantity = int(request.POST['quantity'])

        #getting the stock and team info
        stock_price = float(Stock.objects.get(stock_name = stock_name).stock_price)
        team = Team.objects.get(team_number = team_number)
        team_balance = float(team.team_balance)
        portfolio = team.portfolio
        portfolio_short = team.portfolio_short

        print(team_number,stock_name,transaction_type,quantity)


        print(stock_price,team_balance, quantity)       
        print(type(stock_price), type(team_balance), type(quantity))

        #handling the transactions
        if transaction_type == 'buy':
            if quantity*stock_price > team_balance:
                messages.error(request, 'Your balance is only ' + str(team_balance))     
            else:
                team_balance = team_balance - quantity*stock_price
                team.team_balance = team_balance
                portfolio[stock_name] = str( int(portfolio[stock_name]) + quantity)
                team.portfolio = portfolio

                team.save()
        elif transaction_type == 'sell':
            if quantity > int(portfolio[stock_name]):
                messages.error(request, 'You only have ' + portfolio[stock_name] +' shares ' + 'of ' + stock_name)
            else:
                team_balance = team_balance + quantity*stock_price
                team.team_balance = team_balance
                portfolio[stock_name] = str( int(portfolio[stock_name]) - quantity)   
                team.save()
        elif transaction_type == 'short_sell':
            team_balance = team_balance + quantity*stock_price
            team.team_balance = team_balance
            portfolio_short[stock_name] = str( int(portfolio_short[stock_name]) + quantity)
            team.portfolio_short = portfolio_short
            team.save()
            
            
        else:
            print('seems like non of the transaction type matched.')

                
    return render(request, 'desk_dashboard.html',context)


def desk_stocklist(request):
    stock_list = Stock.objects.all()
    context = []
    for stock in stock_list:
        context.append({'stock_name' : stock.stock_name, 'stock_price' : stock.stock_price})

    return render(request, 'desk_stocklist.html', {'stocks' : context})