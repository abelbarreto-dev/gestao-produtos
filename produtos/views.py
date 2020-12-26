from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
@login_required
def produto_list(request):
    """
        método base para a listagem de produtos
        abelbcarvalho
    """
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

@login_required
def produto_new(request):
    """
        método base para o registro de protudos
        saveProduto
        abelbcarvalho
    """
    form = ProdutoForm(request.POST or None, request.FILES or None)
    # is it valid?
    if form.is_valid():
        form.save()
        return redirect('')
    # else...
    return render(request, 'produtos_form.html', {'form': form})

@login_required
def produto_update(request, id):
    """
        método básico para a atualização de um produto já registrado.
        updateProduto
        abelbcarvalho
    """
    # tentar recuperar objeto
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, 'produto_form.html', {'form': form})

@login_required
def produto_delete(request, id):
    """
        método básico para a exclusão de um produto já registrado.
        deleteProduto
        abelbcarvalho
    """
    # tentar recuperar objeto
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, 'produto_delete_auth.html', {'produto': produto})
