class Fila:
    '''Abstração de qualquer tipo de Fila
        - supermercado
        - processos
        ...
    '''

    '''Todo mundo compartilha, atributo da classe'''
    c_fila = []

    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)

    def __init__(self, obj):
        '''Atributo da instância, apenas o objeto concreto consegue enxergar'''
        self.s_fila = []

    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)
