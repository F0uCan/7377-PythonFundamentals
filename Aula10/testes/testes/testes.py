from unittest import TestCase, main 
from modulo import soma, soma_multipla, sub, multi, div

### Crie um script de testes que
### valide as funcionalidades de uma calculadora
### adicione os scripts dentro da pasta modulo
### realize o import aqui.

class testeCalculadora(TestCase):
    
    def test_soma(self):
        n1 = 10
        n2 = 10
        res = soma(n1,n2)
        self.assertEqual(20,res)

    def test_somaCaractere(self):
        n1 = 'c'
        n2 = 'w'
        res = soma(n1,n2)
        self.assertEqual('cw',res)

    def test_somaMultipla(self):
        n1=10
        n2=20
        n3=40
        res = soma_multipla(n1,n2,n3)
        self.assertEqual(70,res)
        
    def test_subtracao(self):
        res = sub(40,20)
        self.assertEqual(20,res)
        
    def test_multiplicacao(self):
        res = multi(5,5)
        self.assertEqual(25,res)
        
    def test_divisao(self):
        res = div(10,2)
        self.assertEqual(5,res)
    
    def test_divZero(self):
        res = div(10,0)
        self.assertEqual('Não dividirás por zero', res) #return code
    
        

if __name__ == '__main__':
    main()
