from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadModelForm


def lead_list(request):
    leads = Lead.objects.all()

    context = {
        'leads': leads
    }
    return render(request, "lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.filter(pk=pk)

    context = {
        'lead': lead
    }
    return render(request, "lead.html", context)


def lead_create(request):

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/lead/list")
    context = {
        'form': LeadModelForm()
    }
    return render(request, "lead_create.html", context)
