# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 00:03:07 2020

@author: Tianyang Yu
"""

import factory as fac
import pop
import numpy as np
import re
import country as c

name=['USA']
country=[]

def load_country():
    for i in range(len(name)):
        temp=c.Country()
        #basic info
        print("-"*20)
        print("loading country:{}".format(name[i]))
        print("-"*20)
        config=np.loadtxt('country/{}.txt'.format(name[i]),dtype=str)
        temp.name=re.search('name=(.*)',config[0]).group(1)
        temp.eco_type=int(re.search('type=(.*)',config[1]).group(1))
        #pop initial
        print("loading population")
        temp.undereducated=int(re.search('undereducated=(.*)',config[2]).group(1))
        temp.worker=int(re.search('worker=(.*)',config[3]).group(1))
        temp.educated=int(re.search('educated=(.*)',config[4]).group(1))
        temp.elite=int(re.search('elite=(.*)',config[5]).group(1))
        #fact initial
        print("loading factories")
        temp.mine_coal=int(re.search('mine_coal=(.*)',config[6]).group(1))
        temp.mine_oil=int(re.search('mine_oil=(.*)',config[7]).group(1))
        temp.mine_material=int(re.search('mine_material=(.*)',config[8]).group(1))
        temp.mine_U235=int(re.search('mine_U235=(.*)',config[9]).group(1))
        temp.farm=int(re.search('farm=(.*)',config[10]).group(1))
        temp.factory=int(re.search('factory=(.*)',config[11]).group(1))
        temp.high_tech=int(re.search('high_tech=(.*)',config[12]).group(1))
        temp.bank=int(re.search('bank=(.*)',config[13]).group(1))
        temp.power=int(re.search('power=(.*)',config[14]).group(1))
        #national capital
        print("loading capital")
        temp.c_liquid=float(re.search('c_liquid=(.*)',config[15]).group(1))
        temp.c_solid=float(re.search('c_solid=(.*)',config[16]).group(1))
        temp.c_bank=float(re.search('c_bank=(.*)',config[17]).group(1))
        #private capital
        temp.p_liquid=float(re.search('p_liquid=(.*)',config[18]).group(1))
        temp.p_solid=float(re.search('p_solid=(.*)',config[19]).group(1))
        temp.p_bank=float(re.search('p_bank=(.*)',config[20]).group(1))
        #political power in this country
        print("loading political power")
        temp.undereducated_pp=int(re.search('undereducated_pp=(.*)',config[21]).group(1))
        temp.worker_pp=int(re.search('worker_pp=(.*)',config[22]).group(1))
        temp.educated_pp=int(re.search('educated_pp=(.*)',config[23]).group(1))
        temp.elite_pp=int(re.search('elite_pp=(.*)',config[24]).group(1))
        #stockpile
        print("loading stockpile")
        temp.food=float(re.search('food=(.*)',config[25]).group(1))
        temp.material=float(re.search('material=(.*)',config[26]).group(1))
        temp.industrial=float(re.search('industrial=(.*)',config[27]).group(1))
        temp.high_tech=float(re.search('high_tech=(.*)',config[28]).group(1))
        temp.oil=float(re.search('oil=(.*)',config[29]).group(1))
        temp.energy=float(re.search('energy=(.*)',config[30]).group(1))
        temp.coal=float(re.search('coal=(.*)',config[31]).group(1))
        temp.U235=float(re.search('U235=(.*)',config[32]).group(1))
        temp.nuclear=float(re.search('nuclear=(.*)',config[33]).group(1))
        #school
        print("loading school")
        temp.high_school=int(re.search('high_school=(.*)',config[34]).group(1))
        temp.public_university=int(re.search('public_university=(.*)',config[35]).group(1))
        temp.private_universty=int(re.search('private_university=(.*)',config[36]).group(1))
        country.append(temp)
        print("-"*20)
        print("loading complete")
        print("-"*20)
        
load_country()
country[0].init_pop_entity()
country[0].print_stock
country[0].calculate_demand()





#country_config=load_country('country_{}'.format(name[0]))



