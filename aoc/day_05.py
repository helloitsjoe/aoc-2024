DATA_FILE = "day_05.txt"


def parse_orders(orders: str) -> list[list[int]]:
    return [list(map(int, line.split("|"))) for line in orders.splitlines()]


def parse_lists(lists: str) -> list[list[int]]:
    return [list(map(int, pages.split(","))) for pages in lists.splitlines()]


def get_middle_page_correct(pages: list[int], parsed_orders: list[list[int]]):
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


def get_middle_page_incorrect(pages: list[int], full_order: list[int]):
    corrected = []
    print(full_order)
    for val in full_order:
        if val in pages:
            corrected.append(val)

    return corrected[int(len(corrected) / 2)]


def get_full_order(orders: list[list[int]]) -> list[int]:
    print("ORDERS", orders)
    if len(orders) == 3:
        a_counts: dict[int, int] = {}
        b_counts: dict[int, int] = {}
        first = None
        last = None
        mid = None
        for a, b in orders:
            if a in a_counts:
                first = a
                a_counts[a] += 1
            else:
                a_counts[a] = 1
            if b in b_counts:
                last = b
                b_counts[b] += 1
            else:
                b_counts[b] = 1

        for a, b in orders:
            if a_counts[a] == 1:
                mid = a

        if first is None or mid is None or last is None:
            raise RuntimeError("fuck")

        return [first, mid, last]

    new_orders: list[list[int]] = []

    # find first by looking for a that doesn't exist as b
    # find last by looking for b that doesn't exist as a
    # put first and last
    # remove all pairs that include each of those numbers
    # repeat
    first = None
    last = None
    seen_a = {}
    seen_b = {}

    for a, b in orders:
        seen_a[a] = True
        seen_b[b] = True

    print("A", sorted(list(seen_a)))
    print("B", sorted(list(seen_b)))

    if sorted(list(seen_a)) == sorted(list(seen_b)):
        raise RuntimeError("wut")

    for a, b in orders:
        if a not in seen_b:
            first = a
        if b not in seen_a:
            last = b
        if a in seen_b and b in seen_a:
            new_orders.append([a, b])

    print(first, last)
    print(new_orders)

    if first is None or last is None:
        return []

    return [first, *get_full_order(new_orders), last]


def run(data: str, should_be_correct: bool | None = True):
    """
    Data has two sections: ordering rules and ordered pages.
    Ordering rules specify which pages should come before others
    Task is to figure out which lists of ordered pages are correct,
    and then add up the middle digits of those lists
    """
    orders, lists = data.strip().split("\n\n")
    parsed_orders = parse_orders(orders)
    parsed_lists = parse_lists(lists)
    full_order = get_full_order(parsed_orders)

    correct_sum = 0
    incorrect_sum = 0
    for pages in parsed_lists:
        middle_page_correct = get_middle_page_correct(pages, parsed_orders)
        if middle_page_correct > 0:
            correct_sum += middle_page_correct
        else:
            incorrect_sum += get_middle_page_incorrect(pages, full_order)

    return correct_sum if should_be_correct else incorrect_sum


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
