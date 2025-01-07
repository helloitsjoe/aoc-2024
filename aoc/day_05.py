DATA_FILE = "day_05.txt"


def parse_orders(orders: str) -> list[list[int]]:
    return [list(map(int, line.split("|"))) for line in orders.splitlines()]


def parse_lists(lists: str) -> list[list[int]]:
    return [list(map(int, pages.split(","))) for pages in lists.splitlines()]


def get_middle_page(pages: list[int], parsed_orders: list[list[int]]):
    for num in pages:
        for order in parsed_orders:
            a, b = order
            if (
                a in pages
                and b in pages
                and a == num
                and pages.index(b) < pages.index(a)
            ):
                return 0
    return pages[int(len(pages) / 2)]


def run(data: str):
    """
    Data has two sections: ordering rules and ordered pages.
    Ordering rules specify which pages should come before others
    Task is to figure out which lists of ordered pages are correct,
    and then add up the middle digits of those lists
    """
    orders, lists = data.strip().split("\n\n")
    parsed_orders = parse_orders(orders)
    parsed_lists = parse_lists(lists)

    total = 0
    for pages in parsed_lists:
        total += get_middle_page(pages, parsed_orders)

    return total


TEST_DATA = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
