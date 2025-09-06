
def data_giver() ->list:
    list_emails = [
    " Kopi@gmail.com ", "", "NRyo@Yahoo.com", "invalid@", "hello@world",
    " pipoy@email.com", "not-an-email", "walter@crypto.ai", "   "
    ]

    return list_emails


def clean_email(emails: list[str], lowercase=False, sort=False, domain_filter=None) -> list[str]:
    # Step 1: Strip whitespace
    emails = list(map(str.strip, emails))

    # Step 2: Filter valid emails
    valid_emails = list(filter(lambda e: '@' in e and '.' in e and e != '', emails))

    # Step 3: Optional domain filtering
    if domain_filter:
        valid_emails = list(filter(lambda e: domain_filter in e, valid_emails))

    # Step 4: Optional lowercase
    if lowercase:
        valid_emails = [email.lower() for email in valid_emails]

    # Step 5: Optional sort
    if sort:
        valid_emails = sorted(valid_emails)

    return valid_emails


def main():
    list_emails = data_giver()
    valid_emails = clean_email(list_emails, True,True, "@Yahoo")
    print(valid_emails)


if __name__ == "__main__":
    main()
