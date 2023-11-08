from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ("EDUCACAO", "Educação"),
    ("SAUDE", "Saúde"),
    ("ADMINSTRACAO", "Adminstração"),
    ("INFORMÁTICA", "Informática"),
    ("OUTROS", "Outros"),
)


# criar categoria e cursos
class Aprendizado(models.Model):
    Categoria_dos_Cursos = models.CharField(max_length=50, choices=LISTA_CATEGORIAS)
    Descrição_da_Categoria = models.TextField(max_length=500)
    Imagem_da_Categoria = models.ImageField(upload_to='img_categoria')
    Nome_do_Curso = models.CharField(max_length=40,  default='Nome a definir')
    Descrição_do_Curso = models.TextField(max_length=500)
    Imagem_do_Curso = models.ImageField(upload_to='img_curso')
    Prazo_do_Curso = models.IntegerField(default=0)
    Quantidade_de_Vizualizações = models.IntegerField(default=0)
    Data_de_Criação = models.DateTimeField(default=timezone.now)
    Data_de_Finalização = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Nome_do_Curso

#criara episodios
class Episodio(models.Model):
    filme = models.ForeignKey("Aprendizado", related_name ="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.titulo


class Usuario(AbstractUser):
    cursos_vistos = models.ManyToManyField("Aprendizado")



