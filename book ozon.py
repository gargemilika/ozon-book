from lib import create_book, add_book, list_books, search_books


# TODO: tags - война, любовь
# TODO: tags - поезд, любовь
# TODO: 1. Как хранить (тип данных)
# TODO: 2. Как искать  (полное совпадение???)
# TODO: 3. Написать функцию поиска по тегам
# TODO: 4.(advanced) искать по тегам #name

books = []

war_and_piece = create_book(
    'Война и мир',
    'Толстой',
    1000,
    True
)

anna_karenina = create_book(
    'Анна Каренина',
    'Толстой',
    500,
    False
)

add_book(books, war_and_piece)
add_book(books, anna_karenina)

# print(list_books(books, 1, 1))
# print(list_books(books, 2, 1))


print(search_books(books, 'каре'))
print(search_books(books, 'толстой'))
print(search_books(books, 'стругацкие'))
