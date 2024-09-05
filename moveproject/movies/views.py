from django.shortcuts import get_object_or_404, redirect, render
from .models import Movie

from .forms import MovieForm


# Create your views here.

from django.shortcuts import redirect, render
from .models import Movie

# View to render the form for entering only the movie name


    


def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('view_movies')

    else:
        form = MovieForm()
        return render(request,'movies/create_movie.html', {'form': form})
    
def view_movie(request):
    movies=Movie.objects.all()
    return render(request, 'movies/view_movie.html', {'movies': movies})


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)  # Fetch the movie object by its primary key (pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)  # Bind the POST data to the existing movie instance
        if form.is_valid():
            form.save()  # Save the updated movie data
            return redirect('view_movies')  # Redirect after saving
    else:
        form = MovieForm(instance=movie)  # Pre-fill the form with the movie's current data for GET requests
    return render(request, 'movies/edit_movie.html', {'form': form})  # Render the form for editing


def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)  # Fetch the movie object by its primary key (pk)
    movie.delete()  # Delete the movie from the database
    return redirect('view_movies')  # Redirect back to the list of movies after deletion


