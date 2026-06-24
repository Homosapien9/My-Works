def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    max_pal = None
    factors = []
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if max_pal is not None and product < max_pal:
                break  # everything smaller in this row is useless
            if is_palindrome(product):
                if max_pal is None or product > max_pal:
                    max_pal = product
                    factors = [(i, j)]
                elif product == max_pal:
                    factors.append((i, j))
    return (None, []) if max_pal is None else (max_pal, factors)

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    min_pal = None
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if min_pal is not None and product > min_pal:
                break  # no need to continue increasing j
            if is_palindrome(product):
                if min_pal is None or product < min_pal:
                    min_pal = product
                    factors = [(i, j)]
                elif product == min_pal:
                    factors.append((i, j))
    return (None, []) if min_pal is None else (min_pal, factors)