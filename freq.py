def frequency(elements):
    freq = {}
    # for element in elements:
    #     if element not in freq:
    #         freq[element] = 1
    #     else:
    #         freq[element] = freq[element] + 1
    uniq = set(elements)
    for u in uniq:
        freq[u] = elements.count(u)


    return freq


print(frequency([1, 2, 1, 3]))
