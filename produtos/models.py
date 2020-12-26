from django.db import models

# Create your models here.
class Produto(models.Model):
    """
    Essa é a classe modelo do projeto
    abelbcarvalho
    """
    # product name
    nome = models.CharField(max_length=50)
    # product description
    descricao = models.CharField(max_length=100)
    # product serial number
    numero = models.CharField(max_length=25)
    # product price
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

