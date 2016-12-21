from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models.evento import Evento
from .models.categoria import Categoria
from .models.registro import Registro
from .forms import EventoForm, RegistroForm

# Create your views here.


from django.core.urlresolvers import reverse_lazy


# seccion de creacion views de  registro

class MainRegistroPanelView(TemplateView):

    template_name = 'events/registro/registro.html'

    def get_context_data(self, **kwargs):
        context = super(MainRegistroPanelView, self).get_context_data(**kwargs)
        context['asistentes'] = Registro.objects.all()
        return context


class CrearRegistro(CreateView):

    form_class = RegistroForm
    template_name = 'events/registro/crear_registro.html'
    success_url = reverse_lazy('events_app:registropanel')

    def form_valid(self, form):

        return super(CrearRegistro, self).form_valid(form)


# Seccion de creacion de views de Evento

class IndexView(TemplateView):

    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['events'] = Evento.objects.all()
        context['categorias'] = Categoria.objects.all()
        return context


class MainPanelView(TemplateView):

    template_name = 'events/panel/panel.html'

    def get_context_data(self, **kwargs):
        context = super(MainPanelView, self).get_context_data(**kwargs)
        context['events'] = Evento.objects.all()
        context['cantidad'] = context['events'].count()
        return context


class EventDetail(DetailView):

    template_name = 'events/panel/detalle_evento.html'
    model = Evento


class CreateEvent(CreateView):

    form_class = EventoForm
    template_name = 'events/panel/crear_evento.html'
    success_url = reverse_lazy('events_app:panel')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(CreateEvent, self).form_valid(form)


class EventEdit(UpdateView):

    template_name = 'events/panel/editar_evento.html'
    success_url = reverse_lazy('events_app:panel')
    model = Evento
    form_class = EventoForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(EventEdit, self).form_valid(form)


class EventDelete(DeleteView):

    template_name = 'events/panel/eliminar_evento.html'
    model = Evento
    success_url = reverse_lazy('events_app:panel')
    context_object_name = 'event'
