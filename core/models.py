from django.db import models

# faremos o cadastro das nossas series e personagem

class GeneroJogo(models.Model):
    genero = models.CharField(max_length=20, verbose_name="Genero")

    def __str__(self):
        return self.genero


class Jogo(models.Model):
    nomeJogo = models.CharField(max_length=20, verbose_name="Nome")
    person = models.CharField(max_length=20, verbose_name="Personagem")
    ano = models.CharField(max_length=4, verbose_name="Ano")
    generoJogo = models.ForeignKey(GeneroJogo, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nomeJogo 