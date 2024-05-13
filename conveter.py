class NumeralConverter:
    def to_decimal(self, input_value):
        raise NotImplementedError("to_decimal method must be implemented in subclass")

    def from_decimal(self, input_value):
        raise NotImplementedError("from_decimal method must be implemented in subclass")


class RomanNumeralConverter(NumeralConverter):
    _instance = None
    ROMAN_NUMERALS = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def to_decimal(self, roman):
        decimal = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.ROMAN_NUMERALS[char]
            decimal += value if value >= prev_value else -value
            prev_value = value
        return decimal

    def from_decimal(self, decimal):
        if not 0 < decimal < 4000:
            raise ValueError("Input must be between 1 and 3999")

        roman = ''
        for numeral, value in sorted(self.ROMAN_NUMERALS.items(), reverse=True, key=lambda x: x[1]):
            while decimal >= value:
                roman += numeral
                decimal -= value
        return roman


class DecimalConverter(NumeralConverter):
    def to_roman(self, decimal):
        roman = RomanNumeralConverter().from_decimal(decimal)
        return roman

    def from_roman(self, roman):
        decimal = RomanNumeralConverter().to_decimal(roman)
        return decimal


class ConverterFactory:
    @staticmethod
    def create_converter(choice):
        if choice == '1':
            return RomanNumeralConverter()
        elif choice == '2':
            return DecimalConverter()
        else:
            raise ValueError("Invalid converter type")


class UserInterface:
    def __init__(self, converter):
        self.converter = converter

    def roman_to_decimal(self, roman_numeral):
        try:
            decimal_number = self.converter.from_roman(roman_numeral)
            print(f"Decimal representation of {roman_numeral} is {decimal_number}")
        except ValueError as e:
            print(e)

    def decimal_to_roman(self, decimal_number):
        try:
            roman_numeral = self.converter.to_roman(decimal_number)
            print(f"Roman representation of {decimal_number} is {roman_numeral}")
        except ValueError as e:
            print(e)


def main():
    while True:
        choice = input("Choose conversion type (1 for Roman to Decimal, 2 for Decimal to Roman, 0 to exit): ")

        if choice in ('1', '2'):
            converter = ConverterFactory.create_converter(choice)
            ui = UserInterface(converter)
            if choice == '1':
                roman_numeral = input("Enter Roman numeral: ")
                ui.roman_to_decimal(roman_numeral)
            else:
                decimal_number = int(input("Enter Decimal number: "))
                ui.decimal_to_roman(decimal_number)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
