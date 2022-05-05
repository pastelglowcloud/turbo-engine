def format_address(address_string):
    street_name = ""
    parts = address_string.split(" ")
    house_number = parts[0]
    parts = parts[1:]
    for part in parts:
        street_name += str(part)
        if parts.index(part) != len(parts)-1:
            street_name += " "
    return "house number {} on street named {}".format(house_number, street_name)