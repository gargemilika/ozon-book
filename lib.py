def create_book(title, author, price, availability):
    return {
        'title': title,
        'author': author,
        'price': price,
        'available': availability
    }


def add_book(containter, book):
    containter.append(book)

def list_books(containter, page, page_size):
    # page_size = 50
    start = (page - 1) * page_size
    finish = start + page_size
    return containter [start:finish]

def search_books(container, search):
    search_lowercased = search.strip().lower()
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue

    return result