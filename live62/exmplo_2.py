class Pizza:
    pedacos = 8

    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedacos(self):
        '''Método de instância'''
        self.pedacos -= 1

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

    @staticmethod
    def ingredientes():
        return 'Molho de tomate, queijo, cebola'
