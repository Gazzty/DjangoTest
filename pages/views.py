from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PageForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

# Mixin
class StaffRequiredMixin(object):
    # Este mixin revisa si el usuario es staff
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # Esto es reemplazado por el decorador arriba
        """ if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login')) """
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PageListView(ListView):
    model = Page
    template_name = "pages/pages.html"
    context_object_name = "pages"

class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page.html"

class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')