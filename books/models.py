# books/models.py
# This file defines the Book model for the bookstore application.
from django.db import models

# Book  model genre and type choices
# These lists are shown as dropdowns to the user.
genre_choices = (
('classic', 'Classic'),
('romantic', 'Romantic'),
('comic', 'Comic'),
('fantasy', 'Fantasy'),
('horror', 'Horror'),
('educational', 'Educational'),
)

book_type_choices=(
('hardcover','Hard cover'),
('ebook', 'E-Book'),
('audiobook', 'Audiobook')
)

# Book model
class Book(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    author = models.CharField(max_length=128, null=False, blank=False)
    genre = models.CharField(max_length=16, choices=genre_choices, default='classic', null=False, blank=False)
    book_type = models.CharField(max_length=16, choices=book_type_choices, default='hardcover', null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='in US dollars $')   # Allows to add a tooltip

    def __str__(self):
        return self.title
