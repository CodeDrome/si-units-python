from types import MappingProxyType


class SIBaseUnit(object):

    """
    The SIBaseUnit class provides properties for
    representing values of the 7 SI base units,
    multiplier prefixes such as kilo and nano,
    methods for string representation,
    and arithmetic and comparison operators
    """

    quantities = MappingProxyType({
                    "time":
                        {"name": "time", "baseunit": "second", "symbol": "s"},

                    "length":
                        {"name": "length", "baseunit": "metre", "symbol": "m"},

                    "mass":
                        {"name": "mass", "baseunit": "gram", "symbol": "g"},

                    "electric current":
                        {"name": "electric current", "baseunit": "ampere", "symbol": "A"},

                    "thermodynamic temperature":
                        {"name": "thermodynamic temperature", "baseunit": "kelvin", "symbol": "K"},

                    "amount of substance":
                        {"name": "amount of substance", "baseunit": "mole", "symbol": "mol"},

                    "luminous intensity":
                        {"name": "luminous intensity", "baseunit": "candela", "symbol": "cd"}
                  })


    prefixes = MappingProxyType({
                    "yotta": {"name": "yotta", "power": 24, "symbol": "Y"},
                    "zetta": {"name": "zetta", "power": 21, "symbol": "Z"},
                    "exa": {"name": "exa", "power": 18, "symbol": "E"},
                    "peta": {"name": "peta", "power": 15, "symbol": "P"},
                    "tera": {"name": "tera", "power": 12, "symbol": "T"},
                    "giga": {"name": "giga", "power": 9, "symbol": "G"},
                    "mega": {"name": "mega", "power": 6, "symbol": "M"},
                    "kilo": {"name": "kilo", "power": 3, "symbol": "k"},
                    "hecto": {"name": "hecto", "power": 2, "symbol": "h"},
                    "deca": {"name": "deca", "power": 1, "symbol": "da"},

                    "none": {"name": "none", "power": 0, "symbol": ""},

                    "deci": {"name": "deci", "power": -1, "symbol": "d"},
                    "centi": {"name": "centi", "power": -2, "symbol": "c"},
                    "milli": {"name": "milli", "power": -3, "symbol": "m"},
                    "micro": {"name": "micro", "power": -6, "symbol": "μ"},
                    "nano": {"name": "nano", "power": -9, "symbol": "n"},
                    "pico": {"name": "pico", "power": -12, "symbol": "p"},
                    "femto": {"name": "femto", "power": -15, "symbol": "f"},
                    "atto": {"name": "atto", "power": -18, "symbol": "a"},
                    "zepto": {"name": "zepto", "power": -21, "symbol": "z"},
                    "yocto": {"name": "yocto", "power": -24, "symbol": "y"}
               })


    def __init__(self, quantity, prefix, value = 0):

        """
        quantity is one of the quantities values,
        eg SIBaseUnit.quantities["length"]

        prefix is one of the prefixes values,
        eg SIBaseUnit.prefixes["centi"]
        """

        self._quantity = quantity
        self._prefix = prefix
        self._value_base = self.prefixed_value_to_base(value, prefix)


    @property
    def value(self):
        return self.base_value_to_prefixed(self._value_base, self._prefix)
    @value.setter
    def value(self, value):
        self._value_base = self.prefixed_value_to_base(value, self._prefix)


    @property
    def prefix(self):
        return self._prefix


    def __repr__(self):
        return f'SIBaseUnit("{self._quantity}","{self._prefix}",{self.base_value_to_prefixed()})'


    def __str__(self):

        return self.string_short()


    def string_long(self):

        if self._prefix['name'] != "none":
            prefix = self._prefix['name']
        else:
            prefix = ""

        return f"{self.base_value_to_prefixed(self._value_base, self._prefix):g} {prefix}{self._quantity['baseunit']}"


    def string_short(self):

        if self._prefix['name'] != "none":
            symbol = self._prefix['symbol']
        else:
            symbol = ""

        return f"{self.base_value_to_prefixed(self._value_base, self._prefix ):g}{symbol}{self._quantity['symbol']}"


    # selection of arithmetic and comparison dunder methods


    def __add__(self, other):

        self.__check_quantities(other)

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_2 = self.prefixed_value_to_base(other.value, other.prefix)
        base_total = base_1 + base_2
        prefixed_total = self.base_value_to_prefixed(base_total, self.prefix)

        return SIBaseUnit(self._quantity, self._prefix, prefixed_total)


    def __sub__(self, other):

        self.__check_quantities(other)

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_2 = self.prefixed_value_to_base(other.value, other.prefix)
        base_difference = base_1 - base_2
        prefixed_difference = self.base_value_to_prefixed(base_difference, self.prefix)

        return SIBaseUnit(self._quantity, self._prefix, prefixed_difference)


    def __mul__(self, value):

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_product = base_1 * value
        prefixed_product = self.base_value_to_prefixed(base_product, self.prefix)

        return SIBaseUnit(self._quantity, self._prefix, prefixed_product)


    def __rmul__(self, value):

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_product = base_1 * value
        prefixed_product = self.base_value_to_prefixed(base_product, self.prefix)

        return SIBaseUnit(self._quantity, self._prefix, prefixed_product)


    def __truediv__(self, value):

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_quotient = base_1 / value
        prefixed_quotient = self.base_value_to_prefixed(base_quotient, self.prefix)

        return SIBaseUnit(self._quantity, self._prefix, prefixed_quotient)


    def __lt__(self, other):

        self.__check_quantities(other)

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_2 = self.prefixed_value_to_base(other.value, other.prefix)

        return base_1 < base_2


    def __le__(self, other):

        self.__check_quantities(other)

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_2 = self.prefixed_value_to_base(other.value, other.prefix)

        return base_1 <= base_2


    def __eq__(self, other):

        self.__check_quantities(other)

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_2 = self.prefixed_value_to_base(other.value, other.prefix)

        return base_1 == base_2


    def __gt__(self, other):

        self.__check_quantities(other)

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_2 = self.prefixed_value_to_base(other.value, other.prefix)

        return base_1 > base_2


    def __ge__(self, other):

        self.__check_quantities(other)

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_2 = self.prefixed_value_to_base(other.value, other.prefix)

        return base_1 >= base_2


    def __ne__(self, other):

        self.__check_quantities(other)

        base_1 = self.prefixed_value_to_base(self.value, self.prefix)
        base_2 = self.prefixed_value_to_base(other.value, other.prefix)

        return base_1 != base_2


    def __check_quantities(self, other):

        if self._quantity != other._quantity:
            raise TypeError('Both units must be of same quantity')


    def output(self):

        print(f"quantity:       {self._quantity['name']}")
        print(f"base unit:      {self._quantity['baseunit']}")
        print(f"prefix name:    {self._prefix['name']}")
        print(f"prefix power:   {self._prefix['power']}")
        print(f"value_base:     {self._value_base:f}")
        print(f"value prefixed: {self.base_value_to_prefixed(self._value_base, self._prefix):f}")


    @staticmethod
    def prefixed_value_to_base(value_prefixed, prefix):

        return value_prefixed * 10 ** prefix['power']


    @staticmethod
    def base_value_to_prefixed(value_base, prefix):

        return value_base / (10 ** prefix['power'])
