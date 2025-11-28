class Animal:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        
    def descrever(self):
        print(f'[ANIMAL] Nome: {self.nome} | Peso: {self.peso}kg.')
        
    def emitir_som(self):
        print(f'{self.nome} fez um som genérico.')
        
class Cachorro(Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
        
    def emitir_som(self):
        print(f'{self.nome} está latindo: au au!')

class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} está miando: miau!')
        
class Vaca(Animal):
    def emitir_som(self):
        print(f'{self.nome} está mugindo: muu!')
        
class Ave(Animal):
    def __init__(self, nome, peso, envergadura):
        super().__init__(nome, peso) #pega o nome do animal
        self.envergadura = envergadura
        
    def descrever(self):
        super().descrever()
        print(f'Envergadura: {self.envergadura}m.')
    
    def emitir_som(self):
        #chamando o método da classe pai
        super().emitir_som() #opcional
        print(f'{self.nome} está cantando: fiuuu!')


if __name__ == '__main__':
    animais = [
        Cachorro('Spike', 25),
        # Gato('Khaleesi'),
        # Vaca('Mimosa'),
        Ave('Loro', 3, 1.98)
    ]
    
    for animal in animais:
        print('-' * 40)
        animal.descrever()
        animal.emitir_som()
        print('-' * 40)