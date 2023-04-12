from django.shortcuts import render, get_object_or_404, redirect
from .models import Santa, SantaGroup
from .forms import SantaGroupForm
from django.contrib.auth.decorators import login_required


def santa_group_list(request):
    groups = SantaGroup.objects.filter(joinable=True).order_by('distribution_date')
    return render(request, 'secretsanta/santa_group_list.html', {'santa_groups': groups})


def santa_group_detail(request, pk):
    group = get_object_or_404(SantaGroup, pk=pk)
    return render(request, 'secretsanta/santa_group_detail.html', {'group': group})


@login_required
def santa_group_new(request):
    if request.method == "POST":
        form = SantaGroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.generate_code()
            group.save()
            santa = Santa(user=request.user, santa_group=group)
            return redirect('santa_group_detail', pk=group.pk)
    else:
        form = SantaGroupForm()
    return render(request, 'secretsanta/santa_group_edit.html', {'form': form})

@login_required
def santa_group_edit(request, pk):
    group = get_object_or_404(SantaGroup, pk=pk)
    if request.method == "POST":
        form = SantaGroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.generate_code()
            group.save()
            santa = Santa(user=request.user, santa_group=group)
            return redirect('santa_group_detail', pk=group.pk)
    else:
        form = SantaGroupForm(instance=group)
    return render(request, 'secretsanta/santa_group_edit.html', {'form': form})
