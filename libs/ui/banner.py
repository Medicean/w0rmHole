# coding:utf-8

class BANNER:
    '''
    banner
    '''
    def __init__(self, ui):
        self.ui = ui
        self.github = 'http://github.com/Medicean/w0rmHole'
        self.version = '1.0'

    def __call__(self):
        self.ui.p(
            '                   ___           _   ___ _     ', self.ui.RED
        ).p('             _ _ _|   |___ _____| |_|   | |___ ', self.ui.RED
        ).p('            | | | | | |  _|     |   | | | | -_|', self.ui.RED
        ).p('            |_____|___|_| |_|_|_|_|_|___|_|___|', self.ui.RED, False
        ).p(' [ ', self.ui.GREY, False
        ).p('Ver: ', self.ui.YELLOW, False
        ).p(self.version, self.ui.GREEN, False
        ).p(' ]', self.ui.GREY)

        self.ui.p(
            '\n        ---+[ ', self.ui.GREY, False
        ).p(self.github, self.ui.CYAN, False
        ).p(' ]\n', self.ui.GREY)

        return self.ui