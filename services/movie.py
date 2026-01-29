from typing import Optional

from django.db import transaction

from db.models import Movie


def get_movies(title: Optional[str] = None):
    queryset = Movie.objects.all()

    if title is not None:
        queryset = queryset.filter(title__icontains=title)

    return queryset


@transaction.atomic
def create_movie(*, title: str, description: str, duration: int, genres, actors) -> Movie:
    movie = Movie.objects.create(
        title=title,
        description=description,
        duration=duration,
    )
    movie.genres.set(genres)
    movie.actors.set(actors)
    return movie
