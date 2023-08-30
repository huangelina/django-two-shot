from django.shortcuts import render
from receipts.models import Receipt


# Create your views here.
def list_receipt_view(request):
    receipts = Receipt.objects.all()
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/home.html", context)
