from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
# importamos la clase View
from django.views import View
from .models import *
from .forms import *
# Create your views here.
class MatriculaView(View):

    def get(self, request):
        queryset = request.GET.get("buscar")
        listMatricula = Matricula.objects.all()
        if queryset:
            listMatricula = Matricula.objects.filter(
                Q(codigoestudiante__nombre__icontains = queryset) |
                Q(codigoestudiante__apellido__icontains = queryset)
            ).distinct()
        formMatricula = Matriculaform()
        context = {
            'matriculas': listMatricula,
            'formMatricula': formMatricula
        }
        return render(request, 'index.html', context)
    
    def post(self, request):
        formMatricula = Matriculaform(request.POST)
        if formMatricula.is_valid():
            formMatricula.save()
            return redirect('/')
        
    def modificarMatricula(request, id):
        matriculas = get_object_or_404(Matricula, id=id)
        data = {
            'formu': Matriculaform(instance=matriculas)
        }
        if request.method == 'POST':
            formuMa = Matriculaform(data=request.POST, instance=matriculas, files=request.FILES)
            if formuMa.is_valid():
                formuMa.save()
                return redirect('/')
            data["formu"] = formuMa

        return render(request, 'editar_matricula.html', data)
