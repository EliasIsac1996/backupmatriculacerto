from django.contrib import admin
from core.models import Matricula,agendamento_de_aula,deletarAgendamento

# Register your models here.

admin.site.register(Matricula)
admin.site.register(agendamento_de_aula)
admin.site.register(deletarAgendamento)
