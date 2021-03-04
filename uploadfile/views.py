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
    document = BoardPaper.objects.all()
    return render(request, 'display_doc.html', locals())


def view_file(request):
    document = BoardPaper.objects.all()
    return render(request, 'view_papers.html', locals())
