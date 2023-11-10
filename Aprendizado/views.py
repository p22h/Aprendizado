from django.shortcuts import render , redirect, reverse
from .models import Aprendizado, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#def homepage(request):
    #return render(request, "homepage.html")

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage


    def get(self, request,*args, **kwargs):
        if request.user.is_authenticated: #usuario autenticado
            #redireciona para homecursos
            return redirect('Aprendizado:homecursos')
        else:
            return super().get(request, *args, **kwargs) #redireciona homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('Aprendizado:login')
        else:
            return reverse('Aprendizado:criarconta')

# precisa criar para cada pagina: url - view (essa é um view) - html
#def homecursos(request):
    #context = {}
    #lista_filmes = Aprendizado.objects.all()
    #context['lista_filmes'] = lista_filmes
    #return render(request, "homecursos.html", context)

class Homecursos(LoginRequiredMixin, ListView):
    template_name = "homecursos.html"
    model = Aprendizado

class Detalhescursos(LoginRequiredMixin, DetailView):
    template_name = "detalhescursos.html"
    model = Aprendizado

    def get(self, request,*args, **kwargs):
        #qual o filme que esta acessando
        filme = self.get_object()
        filme.Quantidade_de_Vizualizações +=1
        filme.save()
        usuario = request.user
        usuario.cursos_vistos.add(filme)
#redireciona o usuario para  final
        return super().get(request, *args, **kwargs )

    def get_context_data(self, **kwargs):
        context = super(Detalhescursos, self).get_context_data(**kwargs)
        filmes_relacionados = Aprendizado.objects.filter(Categoria_dos_Cursos=self.get_object().Categoria_dos_Cursos)[0:3]
        context ["filmes_relacionados"] = filmes_relacionados
        return context

class Pesquisacurso(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Aprendizado

    #editando object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(Nome_do_Curso__icontains = termo_pesquisa)
            return object_list
        else:
            return None

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields =[ 'first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('Aprendizado:homecursos')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('Aprendizado:login')

