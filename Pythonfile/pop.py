# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 23:35:10 2020

@author: Tianyang Yu
"""
import numpy as np
class population(object):
    def __init__(self):
        self.country=''
        self.name = ''
#        self.social_class=0
        self.satisfied=np.zeros(5)
        self.education=0
        self.unemployed=0
        self.number=0
        self.liquid=0.0
        self.solid=0.0
        self.bank=0.0
        self.employor=''
        #pop needs goods
        self.food_need=1
        self.consumer_need=0
        self.high_tech=0
        self.oil_need=0
        self.energy_need=0
        #political_power=0
        self.need_daily=0.5
        self.need_luxery=0.1
    def print_info(self):
        print("-"*20)
        print("Country:",self.country)
        print(self.name)
        print("SIN:",self.number)
        if self.satisfied==1:
            print("satisfied")
        else:
            print("not satisfied")
        print("education:",self.education)
    def consume(self,stockpile,demand,price,pop_pp):
        need=[self.food_need,self.energy_need,self.oil_need,self.consumer_need,self.high_tech]
        weight=[1,1,0.5,0.5,0.1]
        unhappy=0
        for i in range(len(need)):
            cost=need[i]*price[i]
            if cost<=self.liquid:
                demand[i]=demand[i]-need[i]
                stockpile[i]=stockpile[i]-need[i]
                self.liquid=self.liquid-cost
                self.satisfied[i]=1
            elif cost<=(self.liquid+self.bank):
                demand[i]=demand[i]-need[i]
                stockpile[i]=stockpile[i]-need[i]
                self.bank=self.bank+self.liquid-cost
                unhappy=unhappy+0.1*weight[i]*pop_pp
                self.satisfied[i]=1
            elif cost<=(self.liquid+self.bank+self.solid):
                demand[i]=demand[i]-need[i]
                stockpile[i]=stockpile[i]-need[i]
                self.bank=self.bank+self.liquid+self.solid-cost
                unhappy=unhappy+0.5*weight[i]*pop_pp
                self.satisfied[i]=1
            else:
                unhappy=unhappy+weight[i]*pop_pp
                self.satisfied[i]=0
                break
        return self.satisfied,unhappy
    def return_demand(self):
        demand=[self.food_need,self.energy_need,self.oil_need,self.consumer_need,self.high_tech]
        return demand
        
        