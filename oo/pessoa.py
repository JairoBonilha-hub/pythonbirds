class Pessoa:
    def cumprimentar(self):
        return f'Olá + {id(self)}'
    # ele vai exibir Olá + 30770320
if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())