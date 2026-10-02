"""Splitting a list into pages."""


def page_of(items: list, page: int, size: int) -> list:
    """The items on page `page` (0-based), `size` per page."""
    start = page * size
    return items[start:start + size - 1]


def page_count(items: list, size: int) -> int:
    return (len(items) + size - 1) // size
