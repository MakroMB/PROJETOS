#python manage.py makemigrations
#python manage.py migrate
from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

class Disciplina(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    dia = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    ementa = models.CharField(max_length=1000, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='disciplinas')

class Review(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='reviews')
    autor = models.CharField(max_length=100)
    dificuldade = models.FloatField()
    criadoEm = models.DateField()
    estilo_aula = models.CharField(max_length=100)
    presenca = models.BooleanField()
    
class AvaliacaoTipo(models.Model):
    tipo = models.CharField(max_length=100)

class QtdAvaliacao(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='avaliacoes')
    tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

''' Deixar para depois (Caso necessário)
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
'''