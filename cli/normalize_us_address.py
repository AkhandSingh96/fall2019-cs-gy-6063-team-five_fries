import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from external.googleapi import normalize_us_address  # noqa: E402

usage = """
What it does:
    Normalize an address to the standard form. It handles upper/lowercase letter and a partial address, etc.

usage:
    python normalize_us_address.py "6 metrotech"

output:
    Address(street='6 MetroTech Center', zipcode='11201', city='Brooklyn', state='NY', latitude=40.6942793, longitude=-73.98649809999999)
    6 MetroTech Center, Brooklyn, NY, 11201
"""


def main():
    if len(sys.argv) < 2:
        print(usage)
        return

    addr = sys.argv[1]
    data = normalize_us_address(addr)
    print(data)
    print(data.full_address)


if __name__ == "__main__":
    main()
