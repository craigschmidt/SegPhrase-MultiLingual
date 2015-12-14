# -*- coding: utf-8 -*-

import codecs
import sys
import unicodedata  # get the names of these unicode characters these are

# this file does some unicode normalization using this list of substitutions
# note that those characters are all different, despite their appearance

mapping = {u'０':u'0', u'１':u'1', u'２':u'2', u'３':u'3', u'４':u'4', u'５':u'5', u'６':u'6', u'７':u'7', u'８':u'8', u'９':u'9', \
           u'Ａ':u'A', u'Ｂ':u'B', u'Ｃ':u'C', u'Ｄ':u'D', u'Ｅ':u'E', u'Ｆ':u'F', u'Ｇ':u'G', u'Ｈ':u'H', u'Ｉ':u'I', u'Ｊ':u'J', \
           u'Ｋ':u'K', u'Ｌ':u'L', u'Ｍ':u'M', u'Ｎ':u'N', u'Ｏ':u'O', u'Ｐ':u'P', u'Ｑ':u'Q', u'Ｒ':u'R', u'Ｓ':u'S', u'Ｔ':u'T', \
           u'Ｕ':u'U', u'Ｖ':u'V', u'Ｗ':u'W', u'Ｘ':u'X', u'Ｙ':u'Y', u'Ｚ':u'Z', \
           u'ａ':u'a', u'ｂ':u'b', u'ｃ':u'c', u'ｄ':u'd', u'ｅ':u'e', u'ｆ':u'f', u'ｇ':u'g', u'ｈ':u'h', u'ｉ':u'i', u'ｊ':u'j', \
           u'ｋ':u'k', u'ｌ':u'l', u'ｍ':u'm', u'ｎ':u'n', u'ｏ':u'o', u'ｐ':u'p', u'ｑ':u'q', u'ｒ':u'r', u'ｓ':u's', u'ｔ':u't', \
           u'ｕ':u'u', u'ｖ':u'v', u'ｗ':u'w', u'ｘ':u'x', u'ｙ':u'y', u'ｚ':u'z', \
           u'（':u'(', u'）':u')', u'〔':u'[', u'〕':u']', u'【':u'[', u'】':u']', u'〖':u'[', u'〗':u']', u'｛':u'{', u'｝':u'}', \
           u'《':u'<', u'》':u'>', u'％':u'%', u'＋':u'+', u'—':u'-', u'－':u'-', u'～':u'-', u'：':u':', u'。':u'.', u'、':u',', \
           u'，':u',', u'、':u'.', u'；':u';', u'？':u'?', u'！':u'!', u'…':u'-', u'‖':u'|', u'”':u'"', u'‘':u'\'', u'｜':u'|', \
           u'〃':u'"', u'　':u' ', u'·':u',', u'「':u'"', u'」':u'"', u'”':u'"', u'“':u'"'}

# see that these are different characters: i.e. FULLWIDTH on left, and regular letters on right
def printkey():
    for k in sorted(mapping):
        print k + ", " + mapping[k] + u", " + unicodedata.name(k) + u", " + unicodedata.name(unicode(mapping[k]))

# output:
# ·, ,, MIDDLE DOT, COMMA
# —, -, EM DASH, HYPHEN-MINUS
# ‖, |, DOUBLE VERTICAL LINE, VERTICAL LINE
# ‘, ', LEFT SINGLE QUOTATION MARK, APOSTROPHE
# “, ", LEFT DOUBLE QUOTATION MARK, QUOTATION MARK
# ”, ", RIGHT DOUBLE QUOTATION MARK, QUOTATION MARK
# …, -, HORIZONTAL ELLIPSIS, HYPHEN-MINUS
# 　,  , IDEOGRAPHIC SPACE, SPACE
# 、, ., IDEOGRAPHIC COMMA, FULL STOP
# 。, ., IDEOGRAPHIC FULL STOP, FULL STOP
# 〃, ", DITTO MARK, QUOTATION MARK
# 《, <, LEFT DOUBLE ANGLE BRACKET, LESS-THAN SIGN
# 》, >, RIGHT DOUBLE ANGLE BRACKET, GREATER-THAN SIGN
# 「, ", LEFT CORNER BRACKET, QUOTATION MARK
# 」, ", RIGHT CORNER BRACKET, QUOTATION MARK
# 【, [, LEFT BLACK LENTICULAR BRACKET, LEFT SQUARE BRACKET
# 】, ], RIGHT BLACK LENTICULAR BRACKET, RIGHT SQUARE BRACKET
# 〔, [, LEFT TORTOISE SHELL BRACKET, LEFT SQUARE BRACKET
# 〕, ], RIGHT TORTOISE SHELL BRACKET, RIGHT SQUARE BRACKET
# 〖, [, LEFT WHITE LENTICULAR BRACKET, LEFT SQUARE BRACKET
# 〗, ], RIGHT WHITE LENTICULAR BRACKET, RIGHT SQUARE BRACKET
# ！, !, FULLWIDTH EXCLAMATION MARK, EXCLAMATION MARK
# ％, %, FULLWIDTH PERCENT SIGN, PERCENT SIGN
# （, (, FULLWIDTH LEFT PARENTHESIS, LEFT PARENTHESIS
# ）, ), FULLWIDTH RIGHT PARENTHESIS, RIGHT PARENTHESIS
# ＋, +, FULLWIDTH PLUS SIGN, PLUS SIGN
# ，, ,, FULLWIDTH COMMA, COMMA
# －, -, FULLWIDTH HYPHEN-MINUS, HYPHEN-MINUS
# ０, 0, FULLWIDTH DIGIT ZERO, DIGIT ZERO
# １, 1, FULLWIDTH DIGIT ONE, DIGIT ONE
# ２, 2, FULLWIDTH DIGIT TWO, DIGIT TWO
# ３, 3, FULLWIDTH DIGIT THREE, DIGIT THREE
# ４, 4, FULLWIDTH DIGIT FOUR, DIGIT FOUR
# ５, 5, FULLWIDTH DIGIT FIVE, DIGIT FIVE
# ６, 6, FULLWIDTH DIGIT SIX, DIGIT SIX
# ７, 7, FULLWIDTH DIGIT SEVEN, DIGIT SEVEN
# ８, 8, FULLWIDTH DIGIT EIGHT, DIGIT EIGHT
# ９, 9, FULLWIDTH DIGIT NINE, DIGIT NINE
# ：, :, FULLWIDTH COLON, COLON
# ；, ;, FULLWIDTH SEMICOLON, SEMICOLON
# ？, ?, FULLWIDTH QUESTION MARK, QUESTION MARK
# Ａ, A, FULLWIDTH LATIN CAPITAL LETTER A, LATIN CAPITAL LETTER A
# Ｂ, B, FULLWIDTH LATIN CAPITAL LETTER B, LATIN CAPITAL LETTER B
# Ｃ, C, FULLWIDTH LATIN CAPITAL LETTER C, LATIN CAPITAL LETTER C
# Ｄ, D, FULLWIDTH LATIN CAPITAL LETTER D, LATIN CAPITAL LETTER D
# Ｅ, E, FULLWIDTH LATIN CAPITAL LETTER E, LATIN CAPITAL LETTER E
# Ｆ, F, FULLWIDTH LATIN CAPITAL LETTER F, LATIN CAPITAL LETTER F
# Ｇ, G, FULLWIDTH LATIN CAPITAL LETTER G, LATIN CAPITAL LETTER G
# Ｈ, H, FULLWIDTH LATIN CAPITAL LETTER H, LATIN CAPITAL LETTER H
# Ｉ, I, FULLWIDTH LATIN CAPITAL LETTER I, LATIN CAPITAL LETTER I
# Ｊ, J, FULLWIDTH LATIN CAPITAL LETTER J, LATIN CAPITAL LETTER J
# Ｋ, K, FULLWIDTH LATIN CAPITAL LETTER K, LATIN CAPITAL LETTER K
# Ｌ, L, FULLWIDTH LATIN CAPITAL LETTER L, LATIN CAPITAL LETTER L
# Ｍ, M, FULLWIDTH LATIN CAPITAL LETTER M, LATIN CAPITAL LETTER M
# Ｎ, N, FULLWIDTH LATIN CAPITAL LETTER N, LATIN CAPITAL LETTER N
# Ｏ, O, FULLWIDTH LATIN CAPITAL LETTER O, LATIN CAPITAL LETTER O
# Ｐ, P, FULLWIDTH LATIN CAPITAL LETTER P, LATIN CAPITAL LETTER P
# Ｑ, Q, FULLWIDTH LATIN CAPITAL LETTER Q, LATIN CAPITAL LETTER Q
# Ｒ, R, FULLWIDTH LATIN CAPITAL LETTER R, LATIN CAPITAL LETTER R
# Ｓ, S, FULLWIDTH LATIN CAPITAL LETTER S, LATIN CAPITAL LETTER S
# Ｔ, T, FULLWIDTH LATIN CAPITAL LETTER T, LATIN CAPITAL LETTER T
# Ｕ, U, FULLWIDTH LATIN CAPITAL LETTER U, LATIN CAPITAL LETTER U
# Ｖ, V, FULLWIDTH LATIN CAPITAL LETTER V, LATIN CAPITAL LETTER V
# Ｗ, W, FULLWIDTH LATIN CAPITAL LETTER W, LATIN CAPITAL LETTER W
# Ｘ, X, FULLWIDTH LATIN CAPITAL LETTER X, LATIN CAPITAL LETTER X
# Ｙ, Y, FULLWIDTH LATIN CAPITAL LETTER Y, LATIN CAPITAL LETTER Y
# Ｚ, Z, FULLWIDTH LATIN CAPITAL LETTER Z, LATIN CAPITAL LETTER Z
# ａ, a, FULLWIDTH LATIN SMALL LETTER A, LATIN SMALL LETTER A
# ｂ, b, FULLWIDTH LATIN SMALL LETTER B, LATIN SMALL LETTER B
# ｃ, c, FULLWIDTH LATIN SMALL LETTER C, LATIN SMALL LETTER C
# ｄ, d, FULLWIDTH LATIN SMALL LETTER D, LATIN SMALL LETTER D
# ｅ, e, FULLWIDTH LATIN SMALL LETTER E, LATIN SMALL LETTER E
# ｆ, f, FULLWIDTH LATIN SMALL LETTER F, LATIN SMALL LETTER F
# ｇ, g, FULLWIDTH LATIN SMALL LETTER G, LATIN SMALL LETTER G
# ｈ, h, FULLWIDTH LATIN SMALL LETTER H, LATIN SMALL LETTER H
# ｉ, i, FULLWIDTH LATIN SMALL LETTER I, LATIN SMALL LETTER I
# ｊ, j, FULLWIDTH LATIN SMALL LETTER J, LATIN SMALL LETTER J
# ｋ, k, FULLWIDTH LATIN SMALL LETTER K, LATIN SMALL LETTER K
# ｌ, l, FULLWIDTH LATIN SMALL LETTER L, LATIN SMALL LETTER L
# ｍ, m, FULLWIDTH LATIN SMALL LETTER M, LATIN SMALL LETTER M
# ｎ, n, FULLWIDTH LATIN SMALL LETTER N, LATIN SMALL LETTER N
# ｏ, o, FULLWIDTH LATIN SMALL LETTER O, LATIN SMALL LETTER O
# ｐ, p, FULLWIDTH LATIN SMALL LETTER P, LATIN SMALL LETTER P
# ｑ, q, FULLWIDTH LATIN SMALL LETTER Q, LATIN SMALL LETTER Q
# ｒ, r, FULLWIDTH LATIN SMALL LETTER R, LATIN SMALL LETTER R
# ｓ, s, FULLWIDTH LATIN SMALL LETTER S, LATIN SMALL LETTER S
# ｔ, t, FULLWIDTH LATIN SMALL LETTER T, LATIN SMALL LETTER T
# ｕ, u, FULLWIDTH LATIN SMALL LETTER U, LATIN SMALL LETTER U
# ｖ, v, FULLWIDTH LATIN SMALL LETTER V, LATIN SMALL LETTER V
# ｗ, w, FULLWIDTH LATIN SMALL LETTER W, LATIN SMALL LETTER W
# ｘ, x, FULLWIDTH LATIN SMALL LETTER X, LATIN SMALL LETTER X
# ｙ, y, FULLWIDTH LATIN SMALL LETTER Y, LATIN SMALL LETTER Y
# ｚ, z, FULLWIDTH LATIN SMALL LETTER Z, LATIN SMALL LETTER Z
# ｛, {, FULLWIDTH LEFT CURLY BRACKET, LEFT CURLY BRACKET
# ｜, |, FULLWIDTH VERTICAL LINE, VERTICAL LINE
# ｝, }, FULLWIDTH RIGHT CURLY BRACKET, RIGHT CURLY BRACKET
# ～, -, FULLWIDTH TILDE, HYPHEN-MINUS

# do the substitutions on unicode string ustr
def q2b(ustr):
    return ''.join([c if c not in mapping else mapping[c] for c in ustr])

def main(argv):
    rawTextInput = 'rawText.txt'
    argc = len(argv)
    for i in xrange(argc):
        if argv[i] == "-i" and i + 1 < argc:
            rawTextInput = argv[i + 1]
        elif argv[i] == "-o" and i + 1 < argc:
            segmentedFile = argv[i + 1]
    with codecs.open(segmentedFile, mode='w') as output:
        for line in codecs.open(rawTextInput, encoding='utf-8', mode='r'):
            line = q2b(line)
            output.write(line.encode('utf8'))

if __name__ == "__main__":

    if len(sys.argv) == 1:
        printkey()
    else:
        main(sys.argv[1 : ])