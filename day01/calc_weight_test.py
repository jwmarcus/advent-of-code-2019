def calc_fuel(mass):
    return int(mass / 3) - 2


def enhanced_calc_fuel(mass):
    initial_fuel = calc_fuel(mass)
    tot_additional_fuel = 0
    fractional_fuel = initial_fuel

    while True:
        fractional_fuel = calc_fuel(fractional_fuel)
        if fractional_fuel > 0:
            tot_additional_fuel += fractional_fuel
        else:
            break

    return initial_fuel + tot_additional_fuel


def test_part_one():
    assert 2 == calc_fuel(12)
    assert 2 == calc_fuel(14)
    assert 654 == calc_fuel(1969)
    assert 33583 == calc_fuel(100756)


def test_part_two():
    assert 2 == enhanced_calc_fuel(14)
    assert 966 == enhanced_calc_fuel(1969)
    assert 50346 == enhanced_calc_fuel(100756)


def part_one():
    tot_fuel = 0

    with open("masses.txt") as f:
        for mass in f:
            tot_fuel += calc_fuel(int(mass))

    return tot_fuel


def part_two():
    tot_fuel = 0

    with open("masses.txt") as f:
        for mass in f:
            tot_fuel += enhanced_calc_fuel(int(mass))

    return tot_fuel

    return enhanced_calc_fuel(part_one())


if __name__ == "__main__":
    print(part_one())
    print(part_two())
