DATA_FILE = "day_05.txt"


def parse_orders(orders: str) -> list[list[int]]:
    return [list(map(int, line.split("|"))) for line in orders.splitlines()]


def parse_lists(lists: str) -> list[list[int]]:
    return [list(map(int, pages.split(","))) for pages in lists.splitlines()]


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
    print(parsed_orders)
    print(parsed_lists)


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
