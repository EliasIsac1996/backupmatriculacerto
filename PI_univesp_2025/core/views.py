from agenda import urls
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from core.models import agendamento_de_aula
from core.models import Matricula



#render tela inicial
@login_required
def tela_principal(request):
    return render(request, 'tela_principal.html', {'agendamentos': agendamento_de_aula})

def matriculasubmit(request) :
    if request.POST:
      nome_completo = request.POST.get('nome_completo')
      idade  = request.POST.get('idade')
      instrumento = request.POST.get('instrumento')
      email = request.POST.get('email')
      telefone= request.POST.get('telefone')
      observacao =  request.POST.get('observacoes')
      instrutor = request.user
      Matricula.objects.create(nome_completo= nome_completo ,idade = idade ,instrumento = instrumento, email = email, telefone = telefone,observacao = observacao, instrutor = instrutor)
    return redirect('tela_principal/')


     
