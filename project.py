from astral import moon
from datetime import date
import re

rules = ["Your password must be at least five characters",
         "Your password must include a number",
         "Your password must include an uppercase letter",
         "Your password must include a special character",
         "The digits in your password must add up to 25",
         "Your password must include a month of the year",
         "Your password must include a Roman numeral",
         "Your password must include the current phase of the moon as an emoji",
         "Your password must include a year that is divisible by 7",
         "Your password must include a palindrome word"]

def main():

    while True:
        password = input("Please enter a password: ")

        checks = [rule1(password), rule2(password), rule3(password),
                  rule4(password), rule5(password), rule6(password),
                  rule7(password), rule8(password), rule9(password),
                  rule10(password)]

        failed = []

        for i, passed in enumerate(checks):
            if not passed:
                failed.append(rules[i])

        if not failed:
            print("Congrats! You made a valid password!")
            break
        else:
            print()
            print(f"Your password failed these rules:\n")
            for f in failed:
                print(" -", f)

        print()
        print("Your most recent password attempt was: " + password)
        print("---------------------------")

def rule1(guess):
    if len(guess) >= 5:
        return True
    return False

def rule2(guess):
    if any(ch.isdigit() for ch in guess):
        return True
    return False

def rule3(guess):
    if any(ch.isupper() for ch in guess):
        return True
    return False

def rule4(guess):
    if not guess.isalnum():
        return True
    return False

def rule5(guess):
    result = 0

    for ch in guess:
        if ch.isdigit():
            num = int(ch)
            result += num

    if result == 25:
        return True
    return False

def rule6(guess):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for month in months:
        if month.lower() in guess.lower():
            return True
    return False

def rule7(guess):
    roman_chars = set("IVXLCDM")

    if any(ch in roman_chars for ch in guess):
        return True
    return False

def rule8(guess):
    today = date.today()
    phase = moon.phase(today)
    emoji = ""

    if phase == 0:
        emoji = "🌑"
    elif 0 < phase < 7:
        emoji = "🌒"
    elif phase == 7:
        emoji = "🌓"
    elif 7 < phase < 14:
        emoji = "🌔"
    elif phase == 14:
        emoji = "🌕"
    elif 14 < phase < 21:
        emoji = "🌖"
    elif phase == 21:
        emoji = "🌗"
    else:
        emoji = "🌘"

    if emoji in guess:
        return True
    return False

def rule9(guess):
    match = re.findall(r"\b\d{4}\b", guess)

    if not match:
        return False
    else:
        return True

def rule10(guess):
    guess = guess.lower()
    min_len = 2
    n = len(guess)
    palindromes = []

    for i in range(n):
        for j in range(i + min_len, n + 1):
            substring = guess[i:j]
            if substring == substring[::-1]:
                palindromes.append(substring)

    if not palindromes:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
