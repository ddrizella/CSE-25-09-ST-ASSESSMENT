from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SongForm
from .models import Song


# Create your views here.


def upload_song(request):
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Song uploaded successfully!")
            return redirect('upload_song')
    else:
        form = SongForm()  

    songs = Song.objects.all().order_by('-id')

    return render(request, "upload_song.html", {
        "form": form,    
        "songs": songs,
    })
