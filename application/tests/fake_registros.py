from faker import Faker
from random import randint, choice
from datetime import date,datetime, time
from pprint import pprint
from bson.json_util import dumps,loads
from diasuteis import dias_uteis
from fake_horarios import fake_hora

def testa():
    t= ponto_Empresa()
    pprint("-"*135)
    print("Entrada -  Inicio da Jornada de Trabalho\n")
    pprint(t.entrada())
    pprint("-"*135)
    print("Saída para o Almoço\n")
    pprint(t.saida_almoco())
    pprint("-"*135)
    print("Retorno do Almoço\n")
    pprint(t.volta_almoco())
    pprint("-"*135)
    print("SAÍda - FIM DO EXPEDIENTE\n")
    pprint(t.saida())
    pprint("-"*135)

class ponto_Empresa():
    def __init__(self, n= 1,n_meses=1, portarias= 1):
        self.portarias = portarias
        self.n_de_colaboradores = 3
        self.lista_de_colab= list(range(1,self.n_de_colaboradores))
        self.datas= [dia for dia in dias_uteis()]
    
    def entrada(self):
        self.lst= {}
        for dia in self.datas:
            self.dados_entrada= {}
            self.dados_colaborador= {}
            for _id in self.lista_de_colab:
                
                self.dados_colaborador[_id]= dict(entrada= fake_hora(9), portaria= randint(1, self.portarias))
                
                self.dados_entrada.update(self.dados_colaborador)

            self.lst[dia] = self.dados_entrada
            
        return self.lst


    def saida_almoco(self):
        self.lst= {}
        for dia in self.datas:
            self.dados_saida_almoco= {}
            self.dados_colaborador= {}
            for _id in self.lista_de_colab:
                self.dados_colaborador[_id]= dict(saida= fake_hora(12), portaria= randint(1, self.portarias))

                self.dados_saida_almoco.update(self.dados_colaborador)
            
            self.lst[dia]= self.dados_saida_almoco
        return self.lst
            
    def volta_almoco(self):
        self.lst= {}
        for dia in self.datas:
            self.dados_volta_almoco= {}
            self.dados_colaborador= {}
            for _id in self.lista_de_colab:

                self.dados_colaborador[_id]= dict(retorno_almoço= fake_hora(13), portaria= randint(1, self.portarias))

                self.dados_volta_almoco.update(self.dados_colaborador)

            self.lst[dia]= self.dados_volta_almoco
        return self.lst
    
    def saida(self):
        self.lst= {}
        for dia in self.datas:
            self.dados_fim_jornada= {}
            self.dados_colaborador= {}
            for _id in self.lista_de_colab:
                
                self.dados_colaborador[_id]= dict(fim_expediente= fake_hora(17),portaria= randint(1, self.portarias))                
                self.dados_fim_jornada.update(self.dados_colaborador)
                                
            self.lst[dia]= self.dados_fim_jornada
        return self.lst
    



if __name__ == "__main__":
    testa()





















                
