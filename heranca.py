class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        print(f'{self.nome} fez um som genérico')
        
class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} está latindo: au au!')

class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} está miando: miau!')
        
class Vaca(Animal):
    def emitir_som(self):
        print(f'{self.nome} está mugindo: muu!')


if __name__ == '__main__':
    animais = [
        Cachorro('Spike'),
        Gato('Khaleesi'),
        Vaca('Mimosa')
    ]
    
    for animal in animais:
        animal.emitir_som()