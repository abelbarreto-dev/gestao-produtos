from django.forms import ModelForm
from .models import Produto


class ProdutoForm(ModelForm):
    """
        Classe base de formulário
        abelbcarvalho
    """
    class Meta:
        model = Produto
        # campos a serem preenchidos
        fields = ['nome', 'descricao', 'numero', 'preco']