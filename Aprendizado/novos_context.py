from .models import Aprendizado

def lista_cursos_recentes (request):
    lista_cursos = Aprendizado.objects.all().order_by('-Data_de_Criação')[0:5]
    if lista_cursos:
        destaque = lista_cursos[0]
    else:
        destaque = None
    return {"lista_cursos_recentes": lista_cursos, "destaque": destaque}

def lista_cursos_top (request):
    lista_cursos = Aprendizado.objects.all().order_by('-Quantidade_de_Vizualizações')[0:5]
    return {"lista_cursos_top": lista_cursos}


