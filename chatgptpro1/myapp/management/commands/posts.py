from django.core.management.base import BaseCommand
from myapp.models import Post, Category
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Create dummy Data for Post'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='No.of products to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        categories = Category.objects.all()

        if not categories:
            self.stdout.write(self.style.ERROR('No categories present add something before use run the code '))
            return

        for i in range(count):
            title = f'Title{i+1}'
            author = f'Author{i+1}'
            title_tag = f'Title_tag{i+1}'
            category = random.choice(categories)
            description = fake.text(max_nb_chars=200)
            Post.objects.create(
                title=title,
                author=author,
                title_tag = title_tag,
                category = category,
                description=description
            )
            self.stdout.write(self.style.SUCCESS(f'successfully created Post {title}'))