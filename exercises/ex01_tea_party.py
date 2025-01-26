"""__author__ = "Alexander Knudsen"
__PID__ = "730761985"""

__author__ = "730761985"


"""Program to plan a tea party"""


def main_planner(guests: int) -> None:
    """This function is the main function of the program and creates the output that allows users to
    see what they need in order to plan their party accordingly."""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${round(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)), 2)}"
    )


def tea_bags(people: int) -> int:
    """Function that will calculate the number of tea bags needed
    for a party assuming each person needs 2.
    """
    return people * 2


def treats(people: int) -> int:
    """This function is made to calculate the amount of treats needed for the tea party."""
    return int(tea_bags(people=people) * 1.5 + 0.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function calculates the cost of the tea party using the combined cost of tea
    and treats."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
