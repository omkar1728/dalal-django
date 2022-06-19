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