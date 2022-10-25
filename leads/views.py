from django.shortcuts import redirect, render, reverse
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import LeadModelForm
from .models import Lead


class HomeView(TemplateView):
    template_name = "home.html"


def home(request):
    return render(request, 'home.html')


class LeadListView(ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def lead_list(request):
    leads = Lead.objects.all()

    context = {
        'leads': leads
    }
    return render(request, "lead_list.html", context)


class LeadDetailView(DetailView):
    template_name = "lead.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_detail(request, pk):
    lead = Lead.objects.filter(pk=pk).first()

    context = {
        'lead': lead
    }
    return render(request, "lead.html", context)


class LeadCreateView(CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("lead-list")


def lead_create(request):
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            send_mail(
                subject='test',
                message='test uchun',
                from_email='abdulbosit.go@gmail.com',
                recipient_list=['abdulbositformg@gmail.com']
            )
            form.save()
            return redirect("/lead/list")
    context = {
        'form': LeadModelForm()
    }
    return render(request, "lead_create.html", context)


class LeadUpdateView(UpdateView):
    template_name = "lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("lead-list")


def lead_update(request, pk):
    lead = Lead.objects.filter(pk=pk).first()
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/lead/list")
    context = {
        'form': form,
        'lead': lead
    }
    return render(request, "lead_update.html", context)


class LeadDeleteView(DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("lead-list")


def lead_delete(request, pk):
    lead = Lead.objects.filter(pk=pk).first()
    if lead is not None:
        lead.delete()

    return redirect("lead-list")
