def convert(number: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    valid_subtractive = ["IV", "IX", "XL", "XC", "CD", "CM"]

    total = 0

    for i in range(len(number)):
        current_value = values[number[i]]

        if i + 1 < len(number) and current_value < values[number[i + 1]]:
            pair = number[i] + number[i + 1]

            if pair not in valid_subtractive:
                raise ValueError("Invalid Roman numeral")
            
            if i > 0 and number[i - 1] == number[i]:
                raise ValueError("Invalid Roman numeral")

            total -= current_value
        else:
            total += current_value

    return total