class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        print(f'{self.nome} fez um som genérico')
        
class Cachorro(Animal):
    pass

class Gato(Animal):
    pass



if __name__ == '__main__':
    dog = Cachorro('Spike')
    cat = Gato('Khaleesi')
    
    dog.emitir_som()
    cat.emitir_som()