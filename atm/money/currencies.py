from enum import Enum


class StrEnum(str, Enum):
    def __str__(self):
        return self.value

    # The first argument to this function is documented to be the name of the
    # enum member, not `self`:
    # https://docs.python.org/3.6/library/enum.html#using-automatic-values
    # pylint: disable=no-self-argument
    def _generate_next_value_(name, *_):
        return name


allowed_banknotes = {
    'EUR': [5, 10, 20, 50, 100, 200, 500],
    'RUR': [50, 100, 200, 500, 1000, 2000, 5000],
    'USD': [1, 2, 5, 10, 20, 50, 100]
    }

# Does not work unless its a list
Currencies = StrEnum('Currencies', list(allowed_banknotes.keys()))
