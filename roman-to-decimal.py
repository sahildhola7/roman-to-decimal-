class NumeralConverter:
    def to_decimal(self, input_value):
        raise NotImplementedError("to_decimal method must be implemented in subclass")

    def from_decimal(self, input_value):
        raise NotImplementedError("from_decimal method must be implemented in subclass")


class RomanNumeralConverter(NumeralConverter):
    _instance = None
    ROMAN_NUMERALS = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def to_decimal(self, roman):
        decimal = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in self.ROMAN_NUMERALS:
                decimal += self.ROMAN_NUMERALS[roman[i:i+2]]
                i += 2
            else:
                decimal += self.ROMAN_NUMERALS[roman[i]]
                i += 1
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
    def to_decimal(self, input_value):
        return int(input_value)

    def from_decimal(self, input_value):
        return str(input_value)


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
            decimal_number = self.converter.to_decimal(roman_numeral)
            print(f"Decimal representation of {roman_numeral} is {decimal_number}")
        except ValueError as e:
            print(e)

    def decimal_to_roman(self, decimal_number):
        try:
            decimal_number = int(decimal_number)
            roman_numeral = self.converter.from_decimal(decimal_number)
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
                decimal_number = input("Enter Decimal number: ")
                ui.decimal_to_roman(decimal_number)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
