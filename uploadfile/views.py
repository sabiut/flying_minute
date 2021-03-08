from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from .forms import DocumentForm
from .models import BoardPaper


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('displayfile')
    else:
        form = DocumentForm()
    return render(request, 'upload_page.html', {
        'form': form
    })


def displayfile(request):
    in_group = User.objects.filter(groups__name="organizer")
    if request.user.is_authenticated:
        if request.user in in_group:
            document = BoardPaper.objects.all()
            return render(request, 'display_doc.html', locals())
        else:
            return render(request, 'no_access.html')


def view_file(request):
    document = BoardPaper.objects.all()
    return render(request, 'view_papers.html', locals())


@login_required(login_url='home')
def drop_paper(request, paper_id):
    delete_paper = BoardPaper.objects.get(id=paper_id)
    delete_paper.delete()
    return render(request, 'delete_paper_success.html')

