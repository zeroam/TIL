from functools import reduce
from pprint import pprint


def func_call(func):
    def wrapper(*args, **kwargs):
        print(f" {func.__name__} start ".center(50, "="))
        func(*args, **kwargs)
        print(f" {func.__name__} end ".center(50, "="))

    return wrapper


@func_call
def example_1():
    """count the number of occurences of even numbers"""
    values = [22, 4, 12, 43, 19, 71, 20]

    # using for loop
    print("using for loop: ", end="")
    count = 0
    for number in values:
        if not number % 2:
            count += 1
    print(count)

    # using reduce
    print("using reduce: ", end="")
    count = reduce(lambda acc, num: acc if num % 2 else acc + 1, values, 0)
    print(count)


@func_call
def example_2():
    """Creating a New dict Structure"""
    list_of_invitees = [
        {"email": "alex@example.com", "name": "Alex", "status": "attending"},
        {"email": "brian@example.com", "name": "Brian", "status": "declined"},
        {"email": "carol@example.com", "name": "Carol", "status": "pending"},
        {"email": "derek@example.com", "name": "Derek", "status": "attending"},
        {"email": "ellen@example.com", "name": "Ellen", "status": "attending"},
    ]

    def transform_data(acc, invitee):
        acc[invitee["email"]] = invitee["status"]
        return acc

    results = reduce(transform_data, list_of_invitees, {})
    pprint(results)


@func_call
def example_3_1(list_of_attendees: list):
    """Calculate the number of attendees who brought guests"""

    def derive_guest_count(acc, attendee):
        acc["total_guests"] += 1

        if attendee["brought_guests"]:
            acc["guest_who_brought_guests"] += 1
            acc["total_guests"] += len(attendee["guests"])

        return acc

    results = reduce(
        derive_guest_count,
        list_of_attendees,
        {"guest_who_brought_guests": 0, "total_guests": 0},
    )
    pprint(results)


@func_call
def example_3_2(list_of_attendees: list):
    def derive_vegan_info(acc, attendee):
        if attendee["vegan"]:
            acc["vegan"] += 1
        else:
            acc["non_vegan"] += 1

        if attendee.get("brought_guests"):
            for guest_brought in attendee["guests"]:
                # Check guests recursively
                acc = derive_vegan_info(acc, guest_brought)

        return acc

    results = reduce(derive_vegan_info, list_of_attendees, {"vegan": 0, "non_vegan": 0})
    pprint(results)


if __name__ == "__main__":
    example_1()
    example_2()

    list_of_attendees = [
        {
            "name": "Zeke",
            "vegan": True,
            "brought_guests": True,
            "guests": [
                {"name": "Amanda", "vegan": False},
                {"name": "Wayne", "vegan": True},
            ],
        },
        {"name": "Xavier", "vegan": True, "brought_guests": False},
        {
            "name": "Yohanna",
            "vegan": False,
            "brought_guests": True,
            "guests": [
                {"name": "Lily", "vegan": True},
                {"name": "Stefano", "vegan": True},
            ],
        },
        {"name": "Kael", "vegan": False, "brought_guests": False},
        {"name": "Landon", "vegan": True, "brought_guests": False},
    ]
    example_3_1(list_of_attendees)
    example_3_2(list_of_attendees)
