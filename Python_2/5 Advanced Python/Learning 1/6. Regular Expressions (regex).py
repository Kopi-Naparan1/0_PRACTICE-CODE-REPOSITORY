import re


def exercise_1():
    text = """Sure! Here's a 50-word text that includes some digits:In 2023,
     Emma ran 5 marathons across 3 countries. She trained 6 days a week,
      logging over 1000 miles. Her best time was 3:42:18.
       With 2 medals already won, she aims for 10 total by 2026.
        Her dedication inspires many—especially those under 30 seeking new challenges."""
    numbers = re.findall(r"\d+", text)

    print(numbers)


def exercise_2():
    emails = [
        "alice@example.com",
        "bob@example.com",
        "carol@example.com",
        "dave@example.com"
    ]

    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

    for email in emails:
        print(f"{email}: {bool(re.match(pattern, email))}")


def exercise_3():
    text = """My numbers are 09171234567 and 09281234567, but you can also try 09391234567,
     09451234567, 09561234567, or 09671234567. Some old ones include 09781234567,
      09891234567, and 09991234567. I also once used 09081234567, 09181234567,
       and 09291234567 for business. My friend's numbers are 09301234567 and 09411234567,
        while my office uses 09521234567, 09631234567, and 09741234567.
         Don't forget 09851234567 and 09961234567.
          For emergencies, try 09101234567, 09201234567, or 09311234567.
           You can also fax 09421234567 or call my assistant at 09531234567 
           and 09641234567."""

    pattern = r"09\d{9}"
    phone_numbers: list[int] = (re.findall(pattern, text))
    i = 1
    for number in phone_numbers:
        print(f"#{i}: {number}")
        i += 1


def exercise_4():
    text = "My email is test@exaaample.com, test@exaaample.com"
    match = re.search(r"\w+@\w+\.\w+", text)
    print(match.group())  # 'test@example.com'


def exercise_5():
    emails = re.findall(r"\w+@\w+\.\w+", "Send to a@b.com and x@y.org")
    print(emails)  # ['a@b.com', 'x@y.org']


def exercise_6():
    cleaned = re.sub(r"\d+", "[number]", "My phone is 123456")
    print(cleaned)  # 'My phone is [number]'


def exercise_7():
    valid = re.fullmatch(r"\d{3}-\d{2}-\d{4}", "123-45-6789")
    print(valid is not None)  # True


def main():
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    exercise_7()

if __name__ == "__main__":
    main()