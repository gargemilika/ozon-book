def capitalize(data):
    if data == "":
        return ""

    # head, *other = data
    # return head.upper() + "".join(other)

    return data[:1].upper() + data[1:]



