class TextToBraille:
    def __init__(self, text, convex="*", smooth=" "):
        self.text = text.lower().replace("\n", " ").replace("\t", " ")
        self.convex = str(convex)
        self.smooth = str(smooth)

    def update_text(self, text):
        self.text = text.lower().replace("\n", " ").replace("\t", " ")

    def update_signs(self, convex="*", smooth=" "):
        self.convex = str(convex)
        self.smooth = str(smooth)

    def to_braille_terminal(self):
        c = self.convex
        s = self.smooth
        txt_to_braille = {'а': [c + s, s + s, s + s], 'б': [c + s, c + s, s + s], 'в': [s + c, c + c, s + c],
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
        x = ''
        y = ''
        z = ''
        for i in self.text:
            x += str(txt_to_braille[i][0]) + ' '
            y += str(txt_to_braille[i][1]) + ' '
            z += str(txt_to_braille[i][2]) + ' '
        return x + '\n' + y + '\n' + z

    def to_braille_unicode(self):
        txt_to_braille = {'а': '⠁', 'б': '⠃', 'в': '⠺',
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
        x = ''
        for i in self.text:
            x += txt_to_braille[i]
        return x

    def to_braille_array(self):
        c = self.convex
        s = self.smooth
        txt_to_braille = {'а': [[c, s], [s, s], [s, s]], 'б': [[c, s], [c, s], [s, s]], 'в': [[s, c], [c, c], [s, c]],
                          'г': [[c, c], [c, c], [s, s]], 'д': [[c, c], [s, c], [s, s]], 'е': [[c, s], [s, c], [s, s]],
                          'ё': [[c, s], [s, s], [s, c]], 'ж': [[s, c], [c, c], [s, s]], 'з': [[c, s], [s, c], [c, c]],
                          'и': [[s, c], [c, s], [s, s]], 'й': [[c, c], [c, s], [c, c]], 'к': [[c, s], [s, s], [c, s]],
                          'л': [[c, s], [c, s], [s, c]], 'м': [[c, c], [s, s], [c, s]], 'н': [[c, c], [s, c], [c, s]],
                          'о': [[c, s], [s, c], [c, s]], 'п': [[c, c], [c, s], [c, s]], 'р': [[c, s], [c, c], [c, s]],
                          'с': [[s, c], [c, s], [c, s]], 'т': [[s, c], [c, c], [c, s]], 'у': [[c, s], [s, s], [c, c]],
                          'ф': [[c, c], [c, s], [s, s]], 'х': [[c, s], [c, c], [s, s]], 'ц': [[c, c], [s, s], [s, s]],
                          'ч': [[c, c], [c, c], [c, s]], 'ш': [[c, s], [s, c], [s, c]], 'щ': [[c, c], [s, s], [c, c]],
                          'ъ': [[c, s], [c, c], [c, c]], 'ы': [[s, c], [c, s], [c, c]], 'ь': [[s, c], [c, c], [c, c]],
                          'э': [[s, c], [c, s], [s, c]], 'ю': [[c, s], [c, c], [s, c]], 'я': [[c, c], [c, s], [s, c]],
                          '.': [[s, s], [c, c], [s, c]], '!': [[s, s], [c, c], [c, s]], '-': [[s, s], [s, s], [c, c]],
                          '«': [[s, s], [c, s], [c, c]], '»': [[s, s], [s, c], [c, c]], '(': [[c, s], [c, s], [s, c]],
                          ')': [[s, c], [s, c], [c, s]], ',': [[s, s], [c, s], [s, s]], '?': [[s, s], [c, s], [s, c]],
                          ' ': [[s, s], [s, s], [s, s]]}
        x, y, z = [], [], []
        for i in self.text:
            x += txt_to_braille[i][0]
            y += txt_to_braille[i][1]
            z += txt_to_braille[i][2]
        return [x, y, z]
