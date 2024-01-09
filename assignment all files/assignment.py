names = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
    40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
    80: "eighty", 90: "ninety", 100: "hundred"
}
def number_to_words(num):
    if 0 <= num <= 19:
        return names[num]
    elif 20 <= num <= 99:
        tens = num // 10 * 10
        ones = num % 10
        return names[tens] + (names[ones] if ones else '')
    elif 100 <= num <= 999:
        hundreds = num // 100
        remainder = num % 100
        if remainder:
            return names[hundreds] + " hundred and " + number_to_words(remainder)
        else:
            return names[hundreds] + " hundred"
num = int(input('Enter a number: '))
result = number_to_words(num)
print(f"{num} in words: {result}")
