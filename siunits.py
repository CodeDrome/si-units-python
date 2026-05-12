import sibaseunit as sibu


def main():

    print("----------------------")
    print("| codedrome.com      |")
    print("| SI Units in Python |")
    print("| Part 1: Base Units |")
    print("----------------------\n")


    quantities()

    # add_and_subtract()

    # add_error()

    # multiply_and_divide()

    # comparison_operators()


def quantities():

    """
    Create and output samples of each base type
    """

    print("time\n====")

    time = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["time"],
                           prefix = sibu.SIBaseUnit.prefixes["nano"],
                           value = 2800000000)

    print(f"string_long:  {time.string_long()}")
    print(f"string_short: {time.string_short()}")

    print("output:")
    time.output()


    print("\nlength\n======")

    length = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["length"],
                             prefix = sibu.SIBaseUnit.prefixes["kilo"],
                             value = 1)

    print(f"string_long:  {length.string_long()}")
    print(f"string_short: {length.string_short()}")

    print("\noutput:")
    length.output()


    print("\nmass\n====")

    mass = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["mass"],
                           prefix = sibu.SIBaseUnit.prefixes["milli"],
                           value = 500)

    print(f"string_long:  {mass.string_long()}")
    print(f"string_short: {mass.string_short()}")

    print("\noutput:")
    mass.output()


    print("\nelectric current\n================")

    current = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["electric current"],
                              prefix = sibu.SIBaseUnit.prefixes["none"],
                              value = 13)

    print(f"string_long:  {current.string_long()}")
    print(f"string_short: {current.string_short()}")

    print("\noutput:")
    current.output()


    print("\nthermodynamic temperature\n=========================")

    temperature = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["thermodynamic temperature"],
                              prefix = sibu.SIBaseUnit.prefixes["none"],
                              value = 273.15)

    print(f"string_long:  {temperature.string_long()}")
    print(f"string_short: {temperature.string_short()}")

    print("\noutput:")
    temperature.output()


    print("\namount of substance\n===================")

    amount = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["amount of substance"],
                              prefix = sibu.SIBaseUnit.prefixes["none"],
                              value = 25)

    print(f"string_long:  {amount.string_long()}")
    print(f"string_short: {amount.string_short()}")

    print("\noutput:")
    amount.output()


    print("\nluminous intensity\n===================")

    luminousintensity = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["luminous intensity"],
                              prefix = sibu.SIBaseUnit.prefixes["none"],
                              value = 135)

    print(f"string_long:  {luminousintensity.string_long()}")
    print(f"string_short: {luminousintensity.string_short()}")

    print("\noutput:")
    luminousintensity.output()


def add_and_subtract():

    """
    Demo adding and subtracting lengths.
    Note that the mix of centimetres and millimetres works fine.
    """

    length_1 = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["length"],
                          prefix = sibu.SIBaseUnit.prefixes["centi"],
                          value = 12)

    length_2 = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["length"],
                          prefix = sibu.SIBaseUnit.prefixes["milli"],
                          value = 30)

    total = length_1 + length_2

    print(f"length_1:       {length_1}")
    print(f"length_2:       {length_2}")
    print(f"length_1 + length_2: {total}")

    difference = length_1 - length_2

    print(f"length_1 - length_2: {difference}")


def add_error():

    """
    Try to add a length and a mass to show that an exception is raised
    """

    length = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["length"],
                          prefix = sibu.SIBaseUnit.prefixes["centi"],
                          value = 30)

    mass = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["mass"],
                          prefix = sibu.SIBaseUnit.prefixes["kilo"],
                          value = 2)

    print(f"length:        {length}")
    print(f"mass:          {mass}")

    # this will raise an error as we are
    # trying to add a mass to a length
    try:
        total = length + mass
        print(f"length + mass: {total}")
    except TypeError as e:
        print(e)


def multiply_and_divide():

    """
    Demonstrate multiplying and dividing a length
    """

    length_1 = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["length"],
                          prefix = sibu.SIBaseUnit.prefixes["centi"],
                          value = 16)

    print(f"length_1:     {length_1}")

    product = length_1 * 4
    print(f"length_1 * 4: {product}")

    product = 6 * length_1
    print(f"6 * length_1: {product}")

    quotient = length_1 / 4
    print(f"length_1 / 4: {quotient}")


def comparison_operators():

    """
    Demonstrate <. <=. != etc.
    Note that we can mix prefixes, centimetres and millimetres etc.
    """

    length_1 = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["length"],
                          prefix = sibu.SIBaseUnit.prefixes["centi"],
                          value = 12)

    length_2 = sibu.SIBaseUnit(quantity = sibu.SIBaseUnit.quantities["length"],
                          prefix = sibu.SIBaseUnit.prefixes["milli"],
                          value = 30)

    print(f"{length_1.string_short()} < {length_2.string_short()}    {length_1 < length_2}")
    print(f"{length_1.string_short()} <= {length_2.string_short()}   {length_1 <= length_2}")
    print(f"{length_1.string_short()} == {length_2.string_short()}   {length_1 == length_2}")
    print(f"{length_1.string_short()} > {length_2.string_short()}    {length_1 > length_2}")
    print(f"{length_1.string_short()} >= {length_2.string_short()}   {length_1 >= length_2}")
    print(f"{length_1.string_short()} != {length_2.string_short()}   {length_1 != length_2}")


if __name__ == "__main__":

    main()