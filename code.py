from typing import List, Optional, Iterator


class Film:
    def __init__(self, title: str, genre: str, year: int, rating: float):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def __repr__(self):
        return f"{self.title} ({self.year}) - {self.rating}/10"


class CinemaCollection:
    def __init__(self):
        self.films = {}

    def add_film(self, film: Film) -> None:
        self.films[film.title] = film

    def remove_film(self, title: str) -> None:
        self.films.pop(title, None)

    def search_by(self, **kwargs) -> List[Film]:
        result = []
        for film in self.films.values():
            match = True
            for key, value in kwargs.items():
                if getattr(film, key) != value:
                    match = False
                    break
            if match:
                result.append(film)
        return result

    def __iter__(self) -> Iterator:
        return iter(self.films.values())
