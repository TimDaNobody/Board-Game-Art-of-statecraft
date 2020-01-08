# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 01:30:24 2020

@author: Tianyang Yu
"""
import factory as fac
import pop
import numpy as np

class Country(object):
    def __init__(self):
        #country settings
        self.name=''
        self.eco_type=0
        #country population
        self.undereducated=0
        self.worker=0
        self.educated=0
        self.elite=0
        #country factory
        self.mine_coal=0
        self.mine_oil=0
        self.mine_material=0
        self.mine_U235=0
        self.farm=0
        self.factory=0
        self.high_tech=0
        self.bank=0
        self.power=0
        #national capital
        self.c_liquid=0.00
        self.c_solid=0.00
        self.c_bank=0.00
        #private capital
        self.p_liquid=0.00
        self.p_solid=0.00
        self.p_bank=0.00
        #political power in this country
        self.undereducated_pp=0
        self.worker_pp=0
        self.educated_pp=0
        self.elite_pp=0
        #stock_pile
        self.food=0
        self.material=0
        self.industrial=0
        self.high_tech=0
        self.oil=0
        self.energy=0
        self.coal=0
        self.U235=0
        self.nuclear=0
        #school
        self.high_school=0
        self.public_university=0
        self.private_university=0
        #factory entity
        self.farm_list=[]
        self.factory_list=[]
        self.mine_material_list=[]
        self.mine_U235_list=[]
        self.high_tech_list=[]
        self.bank_list=[]
        self.power_list=[]
        #school entity
        self.high_school_list=[]
        self.public_university_list=[]
        self.private_university_list=[]
        #pop entity
        self.undereducated_list=[]
        self.worker_list=[]
        self.educated_list=[]
        self.elite_list=[]
        #peoples needs
        self.undereducated_food=1
        self.undereducated_industrial=0
        self.undereducated_high_tech=0
        self.undereducated_oil=0
        self.undereducated_energy=0
        
        self.worker_food=1
        self.worker_industrial=0.1
        self.worker_high_tech=0
        self.worker_oil=0
        self.worker_energy=0.5
        
        self.educated_food=1
        self.educated_industrial=0.5
        self.educated_high_tech=0.1
        self.educated_oil=0.1
        self.educated_energy=1
        
        self.elite_food=1
        self.elite_industrial=1
        self.elite_high_tech=0.5
        self.elite_oil=0.2
        self.elite_energy=1
        #production needs
        self.farm_oil=1
        self.farm_energy=1
        self.farm_industrial=0
        self.farm_high_tech=0
        
        self.mine_energy=2
        self.mine_industrial=0
        self.mine_high_tech=0
        
        self.industrial_energy=2
        self.industrial_material=1
        
        self.high_tech_energy=2
        self.high_tech_industiral=1
        self.high_tech_oil=0.5
        #construction list
        self.construction=[]
        #the wage section
        self.lowest_wage=0
        self.wage_counter=3
        #gov_contract
        self.gov_purchase=np.zeros(8) #in order food,energy,oil,goods,high_tech,material,coal,U_235
        self.demand=np.zeros(8)
    def print_info(self):
        print('-'*20)
        print("Basic status")
        print('-'*20)
        print ("Name:",self.name)
        if self.eco_type==1:
            print ("Type:mixed economy")
        else:
            print ("Type:planned economy")
    def print_pop(self):
        print('-'*20)
        print("Population status")
        print('-'*20)
        print("Undereducated:",self.undereducated)
        print("worker:",self.worker)
        print("educated:",self.educated)
        print("elite:",self.elite)
    def print_factory(self):
        print('-'*20)
        print("Factory status")
        print('-'*20)
        print("Mine:",self.mine_material)
        print("U235 Mine:",self.mine_U235)
        print("Farm:",self.farm)
        print("Factory:",self.factory)
        print("High tech:",self.high_tech)
        print("Bank:",self.bank)
        print("Bpower plant:",self.power)
    def print_pp(self):
        print('-'*20)
        print("Power of people")
        print('-'*20)
        print("Unemployed power:",self.unemployed_pp)
        print("Worker power:",self.worker_pp)
        print("Midclass power:",self.educated_pp)
        print("Elite power:",self.elite_pp)
#    def print_capital(self):
    def print_stock(self):
        print('-'*20)
        print("Stockpile")
        print('-'*20)
        print("Food:",self.food)
        print("Energy:",self.energy)
        print("Oil:",self.oil)
        print("Goods:",self.industrial)
        print("High tech:",self.high_tech)

#    def print_school(self):
    def init_pop_entity(self):
        total_pp=self.undereducated_pp+self.worker_pp+self.educated_pp+self.elite_pp
        
        for i in range(self.undereducated):
            temp=pop.population()
            temp.liquid=self.undereducated_pp/total_pp*self.p_liquid/self.undereducated
            temp.solid=self.undereducated_pp/total_pp*self.p_solid/self.undereducated
            temp.bank=self.undereducated_pp/total_pp*self.p_bank/self.undereducated
            temp.name="Undereducated"
            temp.education=0
            temp.number=i
            temp.country=self.name
            temp.consumer_need=self.undereducated_industrial
            temp.food_need=self.undereducated_food
            temp.energy_need=self.undereducated_energy
            temp.high_tech=self.undereducated_high_tech
            temp.oil_need=self.undereducated_oil
            self.undereducated_list.append(temp)
        for i in range(self.worker):
            temp=pop.population()
            temp.liquid=self.worker_pp/total_pp*self.p_liquid/self.worker
            temp.solid=self.worker_pp/total_pp*self.p_solid/self.worker
            temp.bank=self.worker_pp/total_pp*self.p_bank/self.worker
            temp.name="Worker"
            temp.education=1
            temp.number=i
            temp.country=self.name
            temp.consumer_need=self.worker_industrial
            temp.food_need=self.worker_food
            temp.energy_need=self.worker_energy
            temp.high_tech=self.worker_high_tech
            temp.oil_need=self.worker_oil
            self.worker_list.append(temp)
        for j in range(self.educated):
            temp=pop.population()
            temp.liquid=self.educated_pp/total_pp*self.p_liquid/self.educated
            temp.solid=self.educated_pp/total_pp*self.p_solid/self.educated
            temp.bank=self.educated_pp/total_pp*self.p_bank/self.educated
            temp.name="Educated"
            temp.education=2
            temp.number=j
            temp.country=self.name
            temp.consumer_need=self.educated_industrial
            temp.food_need=self.educated_food
            temp.energy_need=self.educated_energy
            temp.high_tech=self.educated_high_tech
            temp.oil_need=self.educated_oil
            self.educated_list.append(temp)
        for j in range(self.elite):
            temp=pop.population()
            temp.liquid=self.elite_pp/total_pp*self.p_liquid/self.elite
            temp.solid=self.elite_pp/total_pp*self.p_solid/self.elite
            temp.bank=self.elite_pp/total_pp*self.p_bank/self.elite
            temp.name="Elite"
            temp.education=3
            temp.number=j
            temp.country=self.name
            temp.consumer_need=self.elite_industrial
            temp.food_need=self.elite_food
            temp.energy_need=self.elite_energy
            temp.high_tech=self.elite_high_tech
            temp.oil_need=self.elite_oil
            self.elite_list.append(temp)
    def add_civil_contract(self,food,energy,oil,goods,high_tech,material,coal,U):
        self.gov_purchase[0]=food
        self.gov_purchase[1]=energy
        self.gov_purchase[2]=oil
        self.gov_purchase[3]=goods
        self.gov_purchase[4]=high_tech
        self.gov_purchase[5]=material
        self.gov_purchase[6]=coal
        self.gov_purchase[7]=U
    def calculate_demand(self):
        temp=[]
        for i in range(len(self.undereducated_list)):
            single_demand=self.undereducated_list[i].return_demand()
            temp.append(single_demand)
        for i in range(len(self.worker_list)):
            single_demand=self.worker_list[i].return_demand()
            temp.append(single_demand)
        for i in range(len(self.educated_list)):
            single_demand=self.educated_list[i].return_demand()
            temp.append(single_demand)
        for i in range(len(self.elite_list)):
            single_demand=self.elite_list[i].return_demand()
            temp.append(single_demand)
        
        np.asarray(temp)
        print(np.sum(temp,0))
#    def calculate_price(self):

#    def calculate_basic_wage(self):
        
    def init_factory_entity(self):
        for j in range (self.mine_coal):
            temp=fac.factory()
#    def worker_consume(self):
#        stock=[10,100,100,50,10]
#        demand=[50,50,50,50,50]
#        price=np.zeros(5)
#        for i in range(5):
#            price[i]=demand[i]/stock[i]
#        
#        for i in range(len(self.worker_list)):
#            condition,unhappy=self.worker_list[i].consume(stock,demand,price,self.worker_pp)
#            print("Stock",stock)
#            print("demand",demand)
#            print("condition",condition)
#            print("unhappy",unhappy)
#            print("-"*20)