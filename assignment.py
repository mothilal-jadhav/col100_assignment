def digit_dominance(n: int) -> str:
    digit = str(n)
    list_of_num = list(digit)

    digit_count = 0
    even = 0
    odd = 0

    while digit_count < len(digit):
        if int(list_of_num[digit_count])%2 == 0:
            even += 1

        else:
            odd += 1

        digit_count += 1

    if even > odd:
        return 'MoreEven'

    elif even<odd:
        return 'MoreOdd'
    
    else:
        return "Equal"




def number_hill(n: int) -> str:
    rows = []
    #upperHalf
    for i in range(1, n + 1):
        row = ''

        for j in range(1, i + 1):
            row += str(j)

        for k in range(i - 1, 0, -1):
            row += str(k)

        rows.append(row)

    #lowerHalf

    for i in range(n-1,0,-1):
        row = ''

        for j in range(1, i + 1):
            row += str(j)

        for k in range(i - 1, 0, -1):
            row += str(k)

        rows.append(row)

    return '\n'.join(rows)



def first_repeated_digit(n: int) -> str:

    appeared = set()

    while n > 0:
        digit = n % 10

        if digit in appeared:
            return str(digit)

        appeared.add(digit)
        n //= 10

    return "No Repetition"


def hollow_right_triangle(n: int) -> str:
    stars = []

    for i in range(1, n + 1):
        if i == 1:
            stars.append("*")
        elif i == 2:
            stars.append("**")
        elif i == n:
            stars.append("*" * n)
        else:
            stars.append("*" + " " * (i - 2) + "*")

    return "\n".join(stars)


