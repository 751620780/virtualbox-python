from virtualbox import library

"""
Add helper code to the default IKeyboard class.
"""


RSHIFT_DOWN = 0x36
RSHIFT_UP   = 0xB6
LSHIFT_DOWN = 0x2A
LSHIFT_UP   = 0xAA
CTRL_DOWN   = 0x1D
CTRL_UP     = 0x9D
RCTRL_DOWN  = 0x0C1D
RCTRL_UP    = 0x9D
ALT_DOWN    = 0x38
ALT_UP      = 0xB8
RALT_DOWN   = 0x0C38
RALT_UP     = 0xB8
CAPS_DOWN   = 0x3A
CAPS_UP     = 0xBA


CODES = {
    'ESC':    [0x01, 0x81],
    '1':      [0x02, 0x82], '!': [LSHIFT_DOWN, 0x02, 0x82, LSHIFT_UP],
    '2':      [0x03, 0x83], '@': [LSHIFT_DOWN, 0x03, 0x83, LSHIFT_UP],
    '3':      [0x04, 0x84], '#': [LSHIFT_DOWN, 0x04, 0x83, LSHIFT_UP],
    '4':      [0x05, 0x85], '$': [LSHIFT_DOWN, 0x05, 0x85, LSHIFT_UP],
    '5':      [0x06, 0x86], '%': [LSHIFT_DOWN, 0x06, 0x86, LSHIFT_UP],
    '6':      [0x07, 0x87], '^': [LSHIFT_DOWN, 0x07, 0x87, LSHIFT_UP],
    '7':      [0x08, 0x87], '&': [LSHIFT_DOWN, 0x07, 0x87, LSHIFT_UP],
    '8':      [0x09, 0x89], '*': [LSHIFT_DOWN, 0x09, 0x89, LSHIFT_UP],
    '9':      [0x0A, 0x8A], '(': [LSHIFT_DOWN, 0x0A, 0x8A, LSHIFT_UP],
    '0':      [0x0B, 0x8B], ')': [LSHIFT_DOWN, 0x0B, 0x8B, LSHIFT_UP],
    '-':      [0x0C, 0x8C], '_': [LSHIFT_DOWN, 0x0C, 0x8C, LSHIFT_UP],
    '=':      [0x0D, 0x8D], '+': [LSHIFT_DOWN, 0x0D, 0x8D, LSHIFT_UP],
    'BKSP':   [0x0E, 0x8E], '\b':[0x0E, 0x8E],
    'TAB':    [0x0F, 0x8F], '\t':[0x0F, 0x8F], 
    'q':      [0x10, 0x90], 'Q': [LSHIFT_DOWN, 0x10, 0x90, LSHIFT_UP],
    'w':      [0x11, 0x91], 'W': [LSHIFT_DOWN, 0x11, 0x91, LSHIFT_UP],
    'e':      [0x12, 0x92], 'E': [LSHIFT_DOWN, 0x12, 0x92, LSHIFT_UP],
    'r':      [0x13, 0x93], 'R': [LSHIFT_DOWN, 0x13, 0x93, LSHIFT_UP],
    't':      [0x14, 0x94], 'T': [LSHIFT_DOWN, 0x14, 0x94, LSHIFT_UP],
    'y':      [0x15, 0x95], 'Y': [LSHIFT_DOWN, 0x15, 0x95, LSHIFT_UP],
    'u':      [0x16, 0x96], 'U': [LSHIFT_DOWN, 0x16, 0x96, LSHIFT_UP],
    'i':      [0x17, 0x97], 'I': [LSHIFT_DOWN, 0x17, 0x97, LSHIFT_UP],
    'o':      [0x18, 0x98], 'O': [LSHIFT_DOWN, 0x18, 0x98, LSHIFT_UP],
    'p':      [0x19, 0x99], 'P': [LSHIFT_DOWN, 0x19, 0x99, LSHIFT_UP],
    '[':      [0x1A, 0x9A], '}': [LSHIFT_DOWN, 0x1A, 0x9A, LSHIFT_UP],
    ']':      [0x1B, 0x9B], '{': [LSHIFT_DOWN, 0x1B, 0x9B, LSHIFT_UP],
    'ENTER':  [0x1C, 0x9C], '\r': [0x1C, 0x9C], '\n': [0x1C, 0x9C],
    'CTRL':   [CTRL_DOWN, CTRL_UP],
    'a':      [0x1E, 0x9E], 'A': [LSHIFT_DOWN, 0x1E, 0x9E, LSHIFT_UP],
    's':      [0x1F, 0x9F], 'S': [LSHIFT_DOWN, 0x1F, 0x9F, LSHIFT_UP],
    'd':      [0x20, 0xA0], 'D': [LSHIFT_DOWN, 0x20, 0xA0, LSHIFT_UP],
    'f':      [0x21, 0xA1], 'F': [LSHIFT_DOWN, 0x21, 0xA1, LSHIFT_UP],
    'g':      [0x22, 0xA2], 'G': [LSHIFT_DOWN, 0x22, 0xA2, LSHIFT_UP],
    'h':      [0x23, 0xA3], 'H': [LSHIFT_DOWN, 0x23, 0xA3, LSHIFT_UP],
    'j':      [0x24, 0xA4], 'J': [LSHIFT_DOWN, 0x24, 0xA4, LSHIFT_UP],
    'k':      [0x25, 0xA5], 'K': [LSHIFT_DOWN, 0x25, 0xA5, LSHIFT_UP],
    'l':      [0x26, 0xA6], 'L': [LSHIFT_DOWN, 0x26, 0xA6, LSHIFT_UP],
    ';':      [0x27, 0xA7], ':': [LSHIFT_DOWN, 0x27, 0xA7, LSHIFT_UP],
    '\'':     [0x28, 0xA8], '\"':[LSHIFT_DOWN, 0x28, 0xA8, LSHIFT_UP],
    '`':      [0x29, 0xA9], '~': [LSHIFT_DOWN, 0x29, 0xA9, LSHIFT_UP],
    'LSHIFT': [LSHIFT_DOWN, LSHIFT_UP],
    '\\':     [0x2B, 0xAB], '|': [LSHIFT_DOWN, 0x2B, 0xAB, LSHIFT_UP],
    'z':      [0x2C, 0xAC], 'Z': [LSHIFT_DOWN, 0x2C, 0xAC, LSHIFT_UP],
    'x':      [0x2D, 0xAD], 'X': [LSHIFT_DOWN, 0x2D, 0xAD, LSHIFT_UP],
    'c':      [0x2E, 0xAE], 'C': [LSHIFT_DOWN, 0x2E, 0xAE, LSHIFT_UP],
    'v':      [0x2F, 0xAF], 'V': [LSHIFT_DOWN, 0x2F, 0xAF, LSHIFT_UP],
    'b':      [0x30, 0xB0], 'B': [LSHIFT_DOWN, 0x30, 0xB0, LSHIFT_UP],
    'n':      [0x31, 0xB1], 'N': [LSHIFT_DOWN, 0x31, 0xB1, LSHIFT_UP],
    'm':      [0x32, 0xB2], 'M': [LSHIFT_DOWN, 0x32, 0xB2, LSHIFT_UP],
    ',':      [0x33, 0xB3], '<': [LSHIFT_DOWN, 0x33, 0xB3, LSHIFT_UP],
    '.':      [0x34, 0xB4], '>': [LSHIFT_DOWN, 0x34, 0xB4, LSHIFT_UP],
    '/':      [0x35, 0xB5], '?': [LSHIFT_DOWN, 0x35, 0xB5, LSHIFT_UP],
    'RSHIFT': [RSHIFT_DOWN, RSHIFT_UP],
    'PRTSC':  [0x37, 0xB7],
    'ALT':    [ALT_DOWN, ALT_UP],
    'SPACE':  [0x39, 0xB9], ' ': [0x39, 0xB9],
    'CAPS':   [CAPS_DOWN, CAPS_UP],
    'F1':     [0x3B, 0xBB], 
    'F2':     [0x3C, 0xBC], 
    'F3':     [0x3D, 0xBD], 
    'F4':     [0x3E, 0xBE], 
    'F5':     [0x3F, 0xBF], 
    'F6':     [0x40, 0xC0], 
    'F7':     [0x41, 0xC1], 
    'F8':     [0x42, 0xC2], 
    'F9':     [0x43, 0xC3], 
    'F10':    [0x44, 0xC4], 
    'F11':    [0x57, 0xD7], 
    'F12':    [0x58, 0xD8], 
    'NUM':    [0x45, 0xC5], 
    'SCRL':   [0x46, 0xC6], 
    'HOME':   [0x47, 0xC7], 
    'UP':     [0x48, 0xC8], 
    'PGUP':   [0x49, 0xC9], 
    'MINUS':  [0x4A, 0xCA], 
    'LEFT':   [0x4B, 0xCB], 
    'CENTER': [0x4C, 0xCC], 
    'RIGHT':  [0x4D, 0xCD], 
    'PLUS':   [0x4E, 0xCE], 
    'END':    [0x4F, 0xCF], 
    'DOWN':   [0x50, 0xD0], 
    'PGDN':   [0x51, 0xD1], 
    'INS':    [0x52, 0xD2], 
    'DEL':    [0x53, 0xD3],
    'PAUSE':  [0xE1, 0x1D, 0x45, 0xE1, 0x9D, 0xC5],
    'E_DIV':  [0xE054, 0xD4], 
    'E_ENTER':[0xE01C, 0x9C],
    'E_INS':  [0xE052, 0xD2],
    'E_DEL':  [0xE053, 0xD3],
    'E_HOME': [0xE047, 0xC7], 
    'E_END':  [0xE04F, 0xCF], 
    'E_PGUP': [0xE049, 0xC9], 
    'E_PGDN': [0xE051, 0xD1], 
    'E_LEFT': [0xE04B, 0xCB], 
    'E_RIGHT':[0xE04D, 0xCD], 
    'E_UP':   [0xE048, 0xC8], 
    'E_DOWN': [0xE050, 0xD0], 
    'RALT':   [RALT_DOWN, RALT_UP], 
    'RCTRL':  [RCTRL_DOWN, RCTRL_UP], 
}


class IKeyboard(library.IKeyboard):
    __doc__ = library.IKeyboard.__doc__

    def put_keys(self, press_keys=[], hold_keys=[]):
        """Drive the scancodes that represent the keys defined in the 
        iterable 'keys' argument"""
        held_codes = set()
        for k in hold_keys:
            if len(CODES[k]) != 2:
                msg = "Can't hold '%s'. It has more than 2 scancodes" % k
                raise ValueError(msg)
            self.put_scancode(CODES[k][0])
            held_codes.add(CODES[k][0])
        for k in press_keys:
            # Avoid releasing held codes
            if CODES[k][0] in held_codes:
                continue
            self.put_scancodes(CODES[k])
        for k in hold_keys:
            self.put_scancode(CODES[k][1])



