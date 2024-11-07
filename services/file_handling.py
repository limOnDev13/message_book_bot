import os


# BOOK_PATH = 'books\\Bredberi_Marsianskie-hroniki.txt'
BOOK_PATH = os.path.join(".", "books", "Bredberi_Marsianskie-hroniki.txt")
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str,
                   start: int,
                   page_size: int) -> tuple[str, int]:
    punctuation_marks = '.,?!:;'

    result_page_size: int
    result_text: str = text[start:start + page_size]

    if page_size <= len(text[start:start + page_size]):
        result_page_size = page_size

        for letter in result_text[::-1]:
            if (letter in punctuation_marks) and \
                    (text[start + result_page_size] not in punctuation_marks):
                break
            else:
                result_page_size -= 1
        result_text = text[start:start + result_page_size]
    else:
        result_page_size = len(text[start:start + page_size])

    return result_text, result_page_size


def prepare_book(path: str) -> None:
    with open(path, encoding="utf-8") as book_text:
        local_book = book_text.read()

        page_number: int = 1
        while local_book:
            page, page_size = _get_part_text(local_book, 0, PAGE_SIZE)
            page = page.lstrip(' \n\t')
            book[page_number] = page
            page_number += 1
            local_book = local_book[page_size:]


prepare_book(BOOK_PATH)
