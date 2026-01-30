from typing import Iterable, Optional

from django.db import transaction
from django.db.models import QuerySet

from db.models import Movie


def get_movies(title: Optional[str] = None) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if title is not None:
        queryset = queryset.filter(title__icontains=title)

    return queryset


@transaction.atomic
def create_movie(
    *,
    title: str,
    description: str,
    duration: int,
    genres: Iterable[int],
    actors: Iterable[int],
) -> Movie:
    movie = Movie.objects.create(
        title=title,
        description=description,
        duration=duration,
    )
    movie.genres.set(genres)
    movie.actors.set(actors)
    return movie
