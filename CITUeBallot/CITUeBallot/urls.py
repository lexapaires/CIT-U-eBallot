"""
URL configuration for CITUeBallot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_voter, name='register_voter'),
    path('success/', views.voter_success, name='voter_success'),
]

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


def vote(request):
    candidates = Candidate.objects.all()
    if request.method == 'POST':
        voter_id = request.POST['voter_id']
        candidate_id = request.POST['candidate_id']
        voter = Voter.objects.get(id=voter_id)
        candidate = Candidate.objects.get(id=candidate_id)
        Vote.objects.create(voter=voter, candidate=candidate)
        return redirect('vote_success')
    return render(request, 'vote.html', {'candidates': candidates})

def vote_success(request):
    return render(request, 'vote_success.html')

urlpatterns += [
    path('vote/', views.vote, name='vote'),
    path('vote/success/', views.vote_success, name='vote_success'),
    path('results/', views.results, name='results'),
]
