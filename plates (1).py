def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Plate may contain 2 to 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # First 2 characters letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    if s[0] not in letters or s[1] not in letters:
        return False

    # Check remaining characters
    number_started = False
    numbers = "0123456789"

    for i in range(2, len(s)):

        if s[i] in numbers:

            # The first number not 0
            if not number_started and s[i] == "0":
                return False

            number_started = True

        elif s[i] in letters:

            # Letters cannot appear after numbers
            if number_started:
                return False

        else:
            # No punctuation and spaces
            return False

    return True


main()
