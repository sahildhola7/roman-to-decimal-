
Coursework Report: Roman Numeral Converter Application
1. Introduction
a. What is your application?
This coursework presents a Python application for converting between Roman numerals and decimal numbers. It offers functionality to convert Roman numerals to decimal numbers and vice versa.

b. How to run the program?
To run the program, ensure you have Python installed on your system. Then, execute the main() function in the provided Python script.

c. How to use the program?
Upon running the program, the user is prompted to choose the conversion type:

Enter '1' for Roman to Decimal conversion.
Enter '2' for Decimal to Roman conversion.
Enter '0' to exit the program.
Based on the chosen option, the user is further prompted to input the Roman numeral or decimal number they want to convert.

2. Body/Analysis
a. Explain how the program covers functional requirements
The program utilizes a class structure with inheritance to implement the functionality.

The NumeralConverter abstract base class defines methods to_decimal() and from_decimal().
The RomanNumeralConverter subclass implements these methods to convert Roman numerals to decimal and vice versa.
The DecimalConverter subclass acts as a bridge to convert decimal numbers to Roman numerals using the RomanNumeralConverter.
3. Results and Summary
The implementation successfully meets the functional requirements by providing accurate conversions between Roman numerals and decimal numbers.
Challenges faced during implementation included ensuring the correctness of the conversion algorithms, especially for edge cases and error handling.
4. Conclusions
The coursework has achieved its objective of creating a functional Roman Numeral Converter application. Future prospects include:

Adding more robust error handling and validation.
Extending the application to support additional numeral systems.
Enhancing the user interface for better usability and feedback.
