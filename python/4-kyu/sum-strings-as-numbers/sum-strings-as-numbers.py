​
def sum_strings(x, y):
​
    if x == "" or y == "":
        return (x or y) or "0"
​
    else:
        import sys
        sys.set_int_max_str_digits(0)
        i = int(x)
        j = int(y)
        return str(i + j)
​