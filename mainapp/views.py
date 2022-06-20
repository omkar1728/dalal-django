from django.shortcuts import render
from .models import Team,Stock
# Create your views here.
def create_team(request):
    #creates team with default portfolio and balance mentioned in models.py of mainapp
    if request.method == 'POST':
        number_of_teams = int(request.POST['number_of_teams'])
        stocks = Stock.objects.all()
        default_portfolio  = {}
        for stock in stocks:
            stock = str(stock.stock_name)
            default_portfolio[stock] = "0"
        for team_number in range(number_of_teams,0,-1):
            team = Team(team_number = team_number, portfolio = default_portfolio, portfolio_short = default_portfolio )
            team.save()
    return render(request, "mainapp_create_team.html")

def dividend(request):
    stocks = Stock.objects.all()
    teams = Team.objects.all()
    stocklist = []
    for stock in stocks:
        stocklist.append({'stock_name' : stock.stock_name})

    if request.method == 'POST':
        stock_name = request.POST['stock_name']
        dividend_amount = int(request.POST['dividend_amount'])
        for team in teams:
            portfolio = team.portfolio
            team_balance = team.team_balance
            number_of_stocks_held = int(portfolio[stock_name])
            dividend_to_be_given = dividend_amount * number_of_stocks_held
            team_balance = team_balance + dividend_to_be_given
            team.team_balance = team_balance
            team.save()

        
    return render(request, "mainapp_dividend.html", {'stocks' : stocklist}) 