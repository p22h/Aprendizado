# url
# view
# template

from django.urls import path, include, reverse_lazy
from .views import Homepage, Homecursos, Detalhescursos, Pesquisacurso, Paginaperfil, Criarconta


from django.contrib.auth import views as auth_view

app_name = "Aprendizado"

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('cursos/', Homecursos.as_view(), name='homecursos'),
    path('cursos/<int:pk>', Detalhescursos.as_view(), name='detalhescursos'),
    path('pesquisa/', Pesquisacurso.as_view(), name='pesquisacurso'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name = 'editarperfil.html', success_url = reverse_lazy('Aprendizado:homecursos')), name='mudarsenha'),
    path('email/', include('enviaemail.urls'))

]
