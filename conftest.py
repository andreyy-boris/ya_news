import pytest

# Импортируем модель заметки, чтобы создать экземпляр.
from news.models import News

@pytest.fixture
def news(author):
    note = News.objects.create(  # Создаём объект заметки.
        title='Заголовок',
        text='Текст заметки',
        slug='note-slug',
        author=author,
    )
    return note