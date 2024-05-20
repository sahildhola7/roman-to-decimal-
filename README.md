### Brief Report on the Numeral Conversion Program

#### Overview

The program is designed to convert between Roman numerals and decimal numbers. It includes several classes that encapsulate the conversion logic and a user interface for interaction. The main components are:

1. **NumeralConverter**: An abstract base class defining the interface for numeral conversion.
2. **RomanNumeralConverter**: A singleton class for converting between Roman numerals and decimal numbers.
3. **DecimalConverter**: A class utilizing RomanNumeralConverter to facilitate conversions.
4. **ConverterFactory**: A factory class to create converter instances based on user choice.
5. **UserInterface**: A class handling user interactions for conversion processes.

#### Classes and Their Responsibilities

1. **NumeralConverter**:
    - Defines two methods, `to_decimal` and `from_decimal`, which must be implemented by subclasses.

2. **RomanNumeralConverter**:
    - Implements `to_decimal` to convert Roman numerals to decimal.
    - Implements `from_decimal` to convert decimal numbers to Roman numerals.
    - Uses a dictionary, `ROMAN_NUMERALS`, for Roman numeral values.
    - Ensures it is a singleton to avoid multiple instances.

3. **DecimalConverter**:
    - Uses RomanNumeralConverter for conversion purposes.
    - Provides `to_roman` to convert decimal numbers to Roman numerals.
    - Provides `from_roman` to convert Roman numerals to decimal numbers.

4. **ConverterFactory**:
    - Contains a static method `create_converter` that returns an instance of RomanNumeralConverter or DecimalConverter based on the user's choice.

5. **UserInterface**:
    - Handles user input and output.
    - Contains methods `roman_to_decimal` and `decimal_to_roman` for performing and displaying conversions.

#### Program Workflow

1. The program starts by prompting the user to choose a conversion type or exit.
2. Based on the user's choice, ConverterFactory creates an appropriate converter instance.
3. UserInterface uses the converter to perform the desired conversion.
4. The user can continue making conversions or exit the program.

#### User Interaction

- **Choice Input**: The user selects between Roman to Decimal conversion (`1`), Decimal to Roman conversion (`2`), or exit (`0`).
- **Roman to Decimal**: The user inputs a Roman numeral, and the program outputs the corresponding decimal number.
- **Decimal to Roman**: The user inputs a decimal number, and the program outputs the corresponding Roman numeral.
- **Exit**: The user can exit the program by choosing `0`.

#### Example Usage

1. **Roman to Decimal Conversion**:
    - User inputs `1` to choose Roman to Decimal conversion.
    - User inputs `XIV` as the Roman numeral.
    - Program outputs `Decimal representation of XIV is 14`.

2. **Decimal to Roman Conversion**:
    - User inputs `2` to choose Decimal to Roman conversion.
    - User inputs `28` as the decimal number.
    - Program outputs `Roman representation of 28 is XXVIII`.

#### Error Handling

- If the user inputs an invalid choice, the program prompts them to choose again.
- If the input value for conversion is out of the valid range or incorrectly formatted, the program raises and catches a ValueError, displaying an appropriate message.

#### Conclusion

This program effectively demonstrates object-oriented principles, such as inheritance, polymorphism, and the singleton pattern, while providing a practical utility for converting between Roman numerals and decimal numbers. The user-friendly interface ensures ease of use, and the robust design handles various input scenarios gracefully.
