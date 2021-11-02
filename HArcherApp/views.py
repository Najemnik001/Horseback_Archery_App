from django.shortcuts import render, get_object_or_404, redirect
from .models import Training
from .forms import TrainingForm
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.utils import timezone

@login_required
def all_results(request):
    all_trainings = Training.objects.all()
    return render(request, 'treningi.html', {'all_trainings': all_trainings})

@login_required
def plots(request):
    daty = Training.objects.values_list('date')
    wyniki = instance
    plt.plot(daty, wyniki, '-bo')
    plt.ylabel('Wynik')
    plt.xlabel('Data')
    plt.xticks(rotation=30)
    plt.title('Wyniki')
    plt.grid()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png', bbox_inches = 'tight')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'wykresy.html', {'data': uri})

@login_required
def new_training(request):
    form = TrainingForm(request.POST or None, request.FILES or None,auto_id=False)
    if form.is_valid():
        form.save()
        return redirect(all_results)

    return render(request, 'training_form.html', {'form': form, 'nowy': True})

@login_required
def edit_training(request, id):
    training = get_object_or_404(Training, pk=id)

    form = TrainingForm(request.POST or None, request.FILES or None, instance=training, auto_id=False)
    if form.is_valid():
        form.save()
        return redirect(all_results)

    return render(request, 'training_form.html', {'form': form, 'nowy': True})

@login_required
def delete_training(request, id):
    training = get_object_or_404(Training, pk=id)

    if request.method == "POST":
        training.delete()
        return redirect(all_results)

    return render(request, 'potwierdz.html', {'training': training, 'nowy': True})

@login_required
def all_statistics(request, id):
    all_statistics = get_object_or_404(Training, pk=id)

    form = TrainingForm(request.POST or None, request.FILES or None, instance=all_statistics)
    if form.is_valid():
        form.save()
        return redirect(all_results)

    return render(request, 'statystyki.html', {'all_statistics': all_statistics, 'nowy': True})

