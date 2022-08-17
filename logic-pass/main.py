# The first question is remove given char
def remove_given_char(s, given_char):
    result = s.replace(given_char, "")
    return result


print(remove_given_char("hello from the other side", "s"))


# Q2/Write a program to find all prime numbers up to a given range of numbers?
def find_prime_number(first, last):
    for num in range(first, last):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            print(num)


print(find_prime_number(2, 30))


# Q3/write a function that count how many the given character repeated in a given string?
def count_repeated_char(char, sentence):
    count = 0
    for s in sentence:
        if s == char:
            count = count + 1
    return count


print(count_repeated_char("s", "hi mosul space"))