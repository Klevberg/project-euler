"""
Project Euler - Problem 17

Name: Number letter counts

Description:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

number_to_name_dict = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred', 1000: 'thousand'
}


def get_name(num):

    name = ''

    for i, n in enumerate(str(num)):
        digits = len(str(num)[i:])

        # THOUSAND
        if digits == 4:
            name += number_to_name_dict[int(n)] + ' ' + number_to_name_dict[1000]
            name += ' ' if int(str(num)[-3:]) else ''
        
        # HUNDRED
        elif digits == 3:
            name += number_to_name_dict[int(n)] + ' ' + number_to_name_dict[100] if int(n) else ''
            name += ' and ' if int(str(num)[-2:]) else ''

        # TEN
        elif digits == 2:
            if int(n) in range(2, 9 + 1):
                name += number_to_name_dict[int(n)*10]
                name += '-' if int(str(num)[-1:]) else ''
            elif int(n) == 1:
                name += number_to_name_dict[int(str(num)[-2:])]
                break

        # ONE
        else:
            name += number_to_name_dict[int(n)]

    return name


def get_length_of_names_up_to(num):

    names = ''.join(get_name(n) for n in range(1, num + 1))
    
    return len(names.translate(str.maketrans('', '', ' -')))


print(get_length_of_names_up_to(1000))