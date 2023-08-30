from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from receipts.models import Receipt

@login_required
def list_receipt_view(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/home.html", context)
