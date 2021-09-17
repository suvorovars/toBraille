class TextToBraille:
    def __init__(self, convex="*", smooth=" ", toUnicode=False):
        c = str(convex)
        s = str(smooth)
        self.toUnicode = toUnicode
        if toUnicode:
            self.txt_to_braille = {'а': '⠁', 'б': '⠃', 'в': '⠺',
                                   'г': '⠛', 'д': '⠙', 'е': '⠑',
                                   'ё': '⠡', 'ж': '⠚', 'з': '⠵',
                                   'и': '⠊', 'й': '⠯', 'к': '⠅',
                                   'л': '⠇', 'м': '⠍', 'н': '⠝',
                                   'о': '⠕', 'п': '⠏', 'р': '⠗',
                                   'с': '⠎', 'т': '⠞', 'у': '⠥',
                                   'ф': '⠋', 'х': '⠓', 'ц': '⠉',
                                   'ч': '⠟', 'ш': '⠱', 'щ': '⠭',
                                   'ъ': '⠷', 'ы': '⠮', 'ь': '⠾',
                                   'э': '⠪', 'ю': '⠳', 'я': '⠫',
                                   '.': '⠲', '!': '⠖', '-': '⠤',
                                   '«': '⠦', '»': '⠴', '(': '⠣',
                                   ')': '⠜', ',': '⠂', '?': '⠢',
                                   ' ': ' '}
        else:
            self.txt_to_braille = {'а': [c + s, s + s, s + s], 'б': [c + s, c + s, s + s], 'в': [s + c, c + c, s + c],
                                   'г': [c + c, c + c, s + s], 'д': [c + c, s + c, s + s], 'е': [c + s, s + c, s + s],
                                   'ё': [c + s, s + s, s + c], 'ж': [s + c, c + c, s + s], 'з': [c + s, s + c, c + c],
                                   'и': [s + c, c + s, s + s], 'й': [c + c, c + s, c + c], 'к': [c + s, s + s, c + s],
                                   'л': [c + s, c + s, c + s], 'м': [c + c, s + s, c + s], 'н': [c + c, s + c, c + s],
                                   'о': [c + s, s + c, c + s], 'п': [c + c, c + s, c + s], 'р': [c + s, c + c, c + s],
                                   'с': [s + c, c + s, c + s], 'т': [s + c, c + c, c + s], 'у': [c + s, s + s, c + c],
                                   'ф': [c + c, c + s, s + s], 'х': [c + s, c + c, s + s], 'ц': [c + c, s + s, s + s],
                                   'ч': [c + c, c + c, c + s], 'ш': [c + s, s + c, s + c], 'щ': [c + c, s + s, c + c],
                                   'ъ': [c + s, c + c, c + c], 'ы': [s + c, c + s, c + c], 'ь': [s + c, c + c, c + c],
                                   'э': [s + c, c + s, s + c], 'ю': [c + s, c + c, s + c], 'я': [c + c, c + s, s + c],
                                   '.': [s + s, c + c, s + c], '!': [s + s, c + c, c + s], '-': [s + s, s + s, c + c],
                                   '«': [s + s, c + s, c + c], '»': [s + s, s + c, c + c], '(': [c + s, c + s, s + c],
                                   ')': [s + c, s + c, c + s], ',': [s + s, c + s, s + s], '?': [s + s, c + s, s + c],
                                   ' ': ['  ', '  ', '  ']}

    def to_braille(self, txt):
        txt = txt.lower().replace("\n", " ").replace("\t", " ")
        if self.toUnicode:
            x = ''
            for i in txt:
                x += self.txt_to_braille[i]
            return x
        else:
            x = ''
            y = ''
            z = ''
            for i in txt:
                x += str(self.txt_to_braille[i][0]) + ' '
                y += str(self.txt_to_braille[i][1]) + ' '
                z += str(self.txt_to_braille[i][2]) + ' '
            return x + '\n' + y + '\n' + z


a = TextToBraille('1', 0)
b = TextToBraille(toUnicode=True)
print(b.to_braille("привет мир!!!"))

print(a.to_braille("привет мир!!!"))
