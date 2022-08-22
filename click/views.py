from django.http import HttpResponse
from django.template import loader
from .models import Accounts

def index(request):
    accounts = Accounts.objects.all().values()
    output = "<table>"
    for account in accounts:
        print(account)
        output += "<tr>"
        output += f"<th>{account['nickname']}</th>"
        output += "</tr>"
    output += "</table>"
    template = loader.get_template('index.html')
    return HttpResponse(output)