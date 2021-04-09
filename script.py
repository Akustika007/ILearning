from sys import argv, stdout
from csv import writer, QUOTE_MINIMAL
from mimesis import Person, Address


def fakedata_writter (count, region):
    while (int(count) <= 0):
        print("First parameter must be more than 0, enter a different value:")
        count = int(input('> '))
    person = Person(region)
    address = Address(region)
    spamwriter = writer(stdout, delimiter=';', quotechar='"', quoting=QUOTE_MINIMAL)
    generate_field = ([person.full_name(), f"{address.country(allow_random=True)} {address.address()}", person.telephone()] for n in range(int(count)))
    for field in generate_field:
        spamwriter.writerow(field)


if __name__ == "__main__":
    fakedata_writter(argv[1], argv[2])
