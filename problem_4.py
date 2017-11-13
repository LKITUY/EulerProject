"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

#palindrome
#num to string
# palindrome if reverse(string) == string


#naive algorithm
def largest_pal_num():
    pal_prod = 0
    for n1 in range(100, 1000):
        for n2 in range(100, 1000):
            product = n1*n2
            str_product = str(product)
            if str_product == str_product[::-1] and pal_prod < product:
                    pal_prod = product
    return pal_prod


print(largest_pal_num()) #906609


