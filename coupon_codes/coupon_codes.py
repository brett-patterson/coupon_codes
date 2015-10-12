""" A Python implementation of the Algorithm::CouponCode algorithm.
See:
1. http://search.cpan.org/dist/Algorithm-CouponCode/lib/Algorithm/CouponCode.pm
2. https://github.com/chilts/node-coupon-code/blob/master/coupon-code.js

Author: Brett Patterson <bmp2@rice.edu>
"""

import codecs
import random

BAD_WORDS = map(lambda w: codecs.decode(w, 'rot13'), [
    'SHPX', 'PHAG', 'JNAX', 'JNAT', 'CVFF', 'PBPX', 'FUVG', 'GJNG', 'GVGF',
    'SNEG', 'URYY', 'ZHSS', 'QVPX', 'XABO', 'NEFR', 'FUNT', 'GBFF', 'FYHG',
    'GHEQ', 'FYNT', 'PENC', 'CBBC', 'OHGG', 'SRPX', 'OBBO', 'WVFZ', 'WVMM',
    'CUNG'
])

SYMBOLS = list('0123456789ABCDEFGHJKLMNPQRTUVWXY')

SYMBOLS_MAP = {s: i for i, s in enumerate(SYMBOLS)}

PART_SEP = '-'

REPLACEMENTS = [
    (r'[^0-9A-Z]+', ''),
    (r'O', '0'),
    (r'I', '1'),
    (r'Z', '2'),
    (r'S', '5')
]


def has_bad_word(code):
    """ Check if a given code contains a bad word.
    """
    for word in BAD_WORDS:
        if word in code:
            return True
    return False


def check_digit(data, n):
    """ Generate the check digit for a code part.
    """
    for c in data:
        n = n * 19 + SYMBOLS_MAP[c]
    return SYMBOLS[n % (len(SYMBOLS) - 1)]


def cc_generate(plaintext=None, n_parts=3, part_len=4):
    """ Generate a coupon code.

    Parameters:
    -----------
    plaintext : str
        A plaintext to generate the code from.

    n_parts : int
        The number of parts for the code.

    part_len : int
        The number of symbols in each part.

    Returns:
    --------
    A coupon code string.
    """
    parts = []

    if plaintext is not None:
        raise NotImplementedError(
            'Generating a code from plaintext is not yet implemented'
        )

    while len(parts) == 0 or has_bad_word(''.join(parts)):
        for i in range(n_parts):
            part = ''
            for j in range(part_len - 1):
                part += random.choice(SYMBOLS)
            part += check_digit(part, i+1)
            parts.append(part)

    return PART_SEP.join(parts)


def cc_validate(code, n_parts=3, part_len=4):
    """ Validate a given code.

    Parameters:
    -----------
    code : str
        The code to validate.

    n_parts : int
        The number of parts for the code.

    part_len : int
        The number of symbols in each part.

    Returns:
    --------
    A cleaned code if the code is valid, otherwise an empty string.
    """
    code = code.upper()
    for replacement in REPLACEMENTS:
        code = code.replace(*replacement)

    parts = code.split(PART_SEP)
    if len(parts) != n_parts:
        return ''

    for i, part in enumerate(parts):
        if len(part) != part_len:
            return ''

        data = part[0:-1]
        check = part[-1]

        if check != check_digit(data, i+1):
            return ''

    return code
