from django.shortcuts import render, redirect, HttpResponse
from .models import investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


def investimentos(request):
    dados ={
        'dados':investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html',context=dados)

def detalhe(request, id_investimento):
    dados ={
        'dados': investimento.objects.get(pk=id_investimento)
    }
    return render(request,'investimentos/detalhe.html', context=dados)

@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos') 
    else:   
        investimento_form = InvestimentoForm()
        formulario = {
        'formulario': investimento_form
        }

        return render(request, 'investimentos/novo_investimento.html',context=formulario)
    
@login_required    
def editar(request, id_investimento):
    Investimento = investimento.objects.get(pk=id_investimento)    
    # novo_investimento/1 --> GET

    if request.method == 'GET':
        formulario = InvestimentoForm(instance=Investimento)
        return render(request,'investimentos/novo_investimento.html',{'formulario':formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=Investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')  
      
@login_required    
def excluir(request, id_investimento):
    Investimento = investimento.objects.get(pk=id_investimento)

    if request.method == 'POST':
        Investimento.delete()
        return redirect('investimentos')
    
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': Investimento})

         
         