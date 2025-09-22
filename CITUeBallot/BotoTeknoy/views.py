from django.shortcuts import render, redirect
from .forms import VoterForm
from django.db.models import Count

def register_voter(request):
    if request.method == 'POST':
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voter_success')
    else:
        form = VoterForm()
    return render(request, 'register_voter.html', {'form': form})

def voter_success(request):
    return render(request, 'voter_success.html')


def results(request):
    candidates = Candidate.objects.annotate(total_votes=Count('vote'))
    return render(request, 'results.html', {'candidates': candidates})
