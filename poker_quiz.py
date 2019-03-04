# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:50:30 2018

@author: Ricardo Rosa
"""


import random
import pandas
import pandas as pd

score_turn=0
total_turns=0
def turn(strategy_turn,flat_range,hero_is,flop_choose,hand,nr_turns):
    global score_turn
    global total_turns
    
    file_turn=flop_choose+'/'+str(flat_range)+'/'+hero_is+'/'+strategy_turn+'.csv'
    df_t = pandas.read_csv(file_turn, index_col='Overbet', names=['Flop','Turn','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )   
    #half_bet.append(df.index)
    df_t.index = pd.to_numeric(df_t.index, errors='coerce')

    df_t_2 = pandas.read_csv(file_turn, index_col='CHECK', names=['Flop','Turn','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )
    df_t_2.index = pd.to_numeric(df_t_2.index, errors='coerce')
    
    df_t_4 = pandas.read_csv(file_turn, index_col='Half_Bet', names=['Flop','Turn','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )
    df_t_4.index = pd.to_numeric(df_t_4.index, errors='coerce')    
    
    df_t_3 = pandas.read_csv(file_turn, index_col='Turn', names=['Flop','Turn','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )
    df_t_5 = pandas.read_csv(file_turn, index_col='Hand', names=['Flop','Turn','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )
    #df_t_3.index = pd.to_numeric(df_t_2.index, errors='coerce')                        
    
    ob_t=(df_t.index>60) | ((df_t_2.index<40) & (df_t.index>df_t_4.index))
    df_t["Overbet"]=ob_t
    
    check_t=[]
    overbet_t=[]
    check_bet_t=[]
    turn_card=[]
    hands_turn=[]
    bet_t=[]
    nr_rivers=1
    
    
    b_t=(df_t_4.index>=65) | ((df_t_2.index<35) & (df_t.index<df_t_4.index))
    df_t["Half_Bet"]=b_t
    
    x_t=df_t_2.index>65
    df_t["CHECK"]=x_t  
    
    x_b_t=(df_t_2.index>=35) & (df_t_2.index<65)
    df_t["CHECK_BET"]=x_b_t
    
    hands_turn.append(df_t_5.index)
    turn_card.append(df_t_3.index)  
    check_bet_t.append(x_b_t)
    overbet_t.append(ob_t) 
    check_t.append(x_t)
    bet_t.append(b_t)

    ok_hand_turn=0
    while ok_hand_turn==0:            
        hand_turn=random.choice(turn_card[0])
        if hand_turn!="Turn":
            ok_hand_turn=1
    
    print("")
    if strategy_turn=="x_x_x_IP":
        print("Villain checks")
        print("POT:6")
    else:    
        print("Villain calls 3")
        print("POT:10")
    print("Flop",flop[0][1],"Turn:",hand_turn,"Hand:",hand)
    print("1. Cbet 12")
    print("2. Cbet 6")
    print("3. Check")
    print("4. Check/Cbet") 
    
    answer_turn=input("Resposta:")    
    
    ok_turn=0
    for y in range(1,len(turn_card[0])): 
        if hand_turn==turn_card[0][y] and hand==hands_turn[0][y] and ok_turn==0: 
            ok_turn=1
            rivers=1
            
            
            
            if int(answer_turn)==1 and str(overbet_t[0][y])=="True":
                total_turns=total_turns+1
                print("Resposta certa") 
                score_turn=score_turn+1
                if rivers==1:
                    if strategy_turn=='x_b_c_x_IP':
                        strategy_river='x_b_c_x_ob_c_x_IP'
                    else:    
                        strategy_river='x_x_x_ob_c_x_IP'
                    for k in range (int(nr_rivers)):                        
                        river(strategy_river,flat_range,hero_is,flop_choose,hand_turn,hand)
            if int(answer_turn)==1 and str(overbet_t[0][y])=="False":
                total_turns=total_turns+1
                print("Resposta errada")                                                            
                if str(check_bet_t[0][y])=="True":
                    print("A Resposta correcta é Check/Bet")
                if str(bet_t[0][y])=="True":
                    print("A Resposta correcta é Half Bet")   
                if str(check_t[0][y])=="True":
                    print("A Resposta correcta é Check")    
                    
                    
            if int(answer_turn)==2 and str(bet_t[0][y])=="True":
                total_turns=total_turns+1
                print("Resposta certa") 
                score_turn=score_turn+1
                if rivers==1:
            
                    if strategy_turn=='x_b_c_x_IP':
                        strategy_river='x_b_c_x_b_c_x_IP'
                    else:                        
                        strategy_river='x_x_x_b_c_x_IP'
                    for k in range (int(nr_rivers)):                        
                        river(strategy_river,flat_range,hero_is,flop_choose,hand_turn,hand)
            if int(answer_turn)==2 and str(bet_t[0][y])=="False":
                total_turns=total_turns+1
                print("Resposta errada")                                                            
                if str(check_bet_t[0][y])=="True":
                    print("A Resposta correcta é Check/Bet")
                if str(overbet_t[0][y])=="True":
                    print("A Resposta correcta é Overbet")   
                if str(check_t[0][y])=="True":
                    print("A Resposta correcta é Check")                            
                    
            if int(answer_turn)==3 and str(check_t[0][y])=="True":
                total_turns=total_turns+1
                print("Resposta certa")
                score_turn=score_turn+1                        
            if int(answer_turn)==3 and str(check_t[0][y])=="False":
                total_turns=total_turns+1
                print("Resposta errada")                                                            
                if str(check_bet_t[0][y])=="True":
                    print("A Resposta correcta é Check/Bet")
                if str(overbet_t[0][y])=="True":
                    print("A Resposta correcta é Overbet")   
                if str(bet_t[0][y])=="True":
                    print("A Resposta correcta é HalfBet")                
    
                    
            if int(answer_turn)==4 and str(check_bet_t[0][y])=="True":
                total_turns=total_turns+1
                print("Resposta certa")                        
            if int(answer_turn)==4 and str(check_bet_t[0][y])=="False":
                total_turns=total_turns+1
                print("Resposta errada")                                                            
                if str(bet_t[0][y])=="True":
                    print("A Resposta correcta é HalfBet")
                if str(overbet_t[0][y])=="True":
                    print("A Resposta correcta é Overbet")   
                if str(check_t[0][y])=="True":
                    print("A Resposta correcta é Check")                             





def river(strategy_river,flat_range,hero_is,flop_choose,hand_turn,hand):
    
    
    file_river=flop_choose+'/'+str(flat_range)+'/'+hero_is+'/'+strategy_river+'.csv'
    df_r = pandas.read_csv(file_river, index_col='Overbet', names=['Flop','Turn','River','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )   
    #half_bet.append(df.index)
    df_r.index = pd.to_numeric(df_r.index, errors='coerce')

    df_r_2 = pandas.read_csv(file_river, index_col='CHECK', names=['Flop','Turn','River','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )   
    df_r_2.index = pd.to_numeric(df_r_2.index, errors='coerce')
    
    df_r_4 = pandas.read_csv(file_river, index_col='Half_Bet', names=['Flop','Turn','River','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )   
    df_r_4.index = pd.to_numeric(df_r_4.index, errors='coerce')    
    
    df_r_3 = pandas.read_csv(file_river, index_col='Turn', names=['Flop','Turn','River','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )   
    df_r_6 = pandas.read_csv(file_river, index_col='River', names=['Flop','Turn','River','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )   
    df_r_5 = pandas.read_csv(file_river, index_col='Hand', names=['Flop','Turn','River','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Overbet','Overbet EV','Half_Bet','BET 6 EV', 'CHECK', 'CHECK EV'] )   
    
    #df_t_3.index = pd.to_numeric(df_t_2.index, errors='coerce')                        
    
    ob_r=(df_r.index>60) | ((df_r_2.index<40) & (df_r.index>df_r_4.index))
    df_r["Overbet"]=ob_r
    
    check_r=[]
    overbet_r=[]
    check_bet_r=[]
    river_card=[]
    hands_turn=[]
    hands_river=[]
    bet_r=[]
    
    b_r=(df_r_4.index>=65) | ((df_r_2.index<35) & (df_r.index<df_r_4.index))
    df_r["Half_Bet"]=b_r
    
    x_r=df_r_2.index>=65
    df_r["CHECK"]=x_r  
    
    x_b_r=(df_r_2.index>=35) & (df_r_2.index<65)
    df_r["CHECK_BET"]=x_b_r
    
    hands_river.append(df_r_5.index)
    hands_turn.append(df_r_3.index)
    river_card.append(df_r_6.index)  
    check_bet_r.append(x_b_r)
    overbet_r.append(ob_r) 
    check_r.append(x_r)
    bet_r.append(b_r)

    ok_hand_river=0
    while ok_hand_river==0:            
        hand_river=random.choice(river_card[0])
        if hand_river!="River":
            ok_hand_river=1
    
    print("")
    if strategy_river=="x_x_x_IP":
        print("Villain checks")
        print("POT:10")
    else:    
        print("Villain calls 3")
        print("POT:34")
        print("POT:22")
    print("Flop",flop[0][1],"Turn:",hand_turn,"River:",hand_river,"Hand:",hand)
    print("1. Cbet 41")
    print("2. Cbet 19")
    print("3. Check")
    print("4. Check/Cbet") 
    
    answer_river=input("Resposta:")    
    
    ok_river=0
    for y in range(1,len(river_card[0])): 
        if hand_river==river_card[0][y] and hand_turn==hands_turn[0][y] and hand==hands_river[0][y] and hand_river!=hand_turn and ok_river==0: 
            ok_river=1
            
            
            
            
            if int(answer_river)==1 and str(overbet_r[0][y])=="True":
                print("Resposta certa")                        
            if int(answer_river)==1 and str(overbet_r[0][y])=="False":
                print("Resposta errada")                                                            
                if str(check_bet_r[0][y])=="True":
                    print("A Resposta correcta é Check/Bet")
                if str(bet_r[0][y])=="True":
                    print("A Resposta correcta é Half Bet")   
                if str(check_r[0][y])=="True":
                    print("A Resposta correcta é Check")    
                    
                    
            if int(answer_river)==2 and str(bet_r[0][y])=="True":
                print("Resposta certa")                        
            if int(answer_river)==2 and str(bet_r[0][y])=="False":
                print("Resposta errada")                                                            
                if str(check_bet_r[0][y])=="True":
                    print("A Resposta correcta é Check/Bet")
                if str(overbet_r[0][y])=="True":
                    print("A Resposta correcta é Overbet")   
                if str(check_r[0][y])=="True":
                    print("A Resposta correcta é Check")                            
                    
            if int(answer_river)==3 and str(check_r[0][y])=="True":
                print("Resposta certa")                        
            if int(answer_river)==3 and str(check_r[0][y])=="False":
                print("Resposta errada")                                                            
                if str(check_bet_r[0][y])=="True":
                    print("A Resposta correcta é Check/Bet")
                if str(overbet_r[0][y])=="True":
                    print("A Resposta correcta é Overbet")   
                if str(bet_r[0][y])=="True":
                    print("A Resposta correcta é HalfBet")                
    
                    
            if int(answer_river)==4 and str(check_bet_r[0][y])=="True":
                print("Resposta certa")                        
            if int(answer_river)==4 and str(check_bet_r[0][y])=="False":
                print("Resposta errada")                                                            
                if str(bet_r[0][y])=="True":
                    print("A Resposta correcta é HalfBet")
                if str(overbet_r[0][y])=="True":
                    print("A Resposta correcta é Overbet")   
                if str(check_r[0][y])=="True":
                    print("A Resposta correcta é Check")        




if __name__ == "__main__":
    position_dic = {
            "BB":-2,
            "SB":-1,
            "BTN":0,
            "CO":1,
            "MP":2,
            "UTG":3,
            }
    #flops_list=["R_A_High","FD_J_High","FD_LowCards","GUT_FD_J_High","OS_FD_RegBoard","OS_FD_J_High","PAIRED_FD_J_High","MADESTR_A_High"]
    flops_list=["R_A_High","FD_J_High","FD_LowCards","GUT_FD_J_High","OS_FD_RegBoard","OS_FD_J_High","PAIRED_FD_J_High","MADESTR_A_High"]
    ok_hero=0
    ok_villain=0
    position_list=["BB","SB","BTN","CO","MP","UTG"]
    profile_OOP=["standart","cbhighf","cblowf"]
    profile_IP=["standart","cbhighf","cblowf"]
    cards=[]
    half_bet=[]
    check_bet=[]
    bet=[]
    check=[]
    flop=[]
    ok_hand=0
    score=0
    turns=0
    p_r_ip=0
    score_turn=0
    f_r=0
    
    #position_steal_list=["BTN","CO","SB"]
    #position_steal_flat_list=["BTN","SB","BB"]
    print("Choose Flop:")
    print(flops_list)
    print("R-Random")
    answer=input("Resposta:")
    
    if answer!='R' and answer!='r':
        flop_choose=flops_list[int(answer)]
    else:
        flop_choose=random.choice(flops_list)
        f_r=1
    while ok_hero==0:
        print("Choose Hero Position:")
        print(position_list)
        print("R-Random")
        answer=input("Resposta:")
        if answer!="R" and answer!="r":
            position_hero=position_list[int(answer)]
        else:        
            position_hero=random.choice(position_list)
        if position_hero!="BB":
            ok_hero=1
    #print (position_list["BTN"])
    while ok_villain==0:
        print("Choose Villain Position:")
        print(position_list)
        print("R-Random")
        answer=input("Resposta:")
        if answer!="R" and answer!="r":
            position_villain=position_list[int(answer)]
        else:        
            position_villain=random.choice(position_list)
        if position_dic[position_hero]>position_dic[position_villain]:
            ok_villain=1
    #print ("Hero: ",position_hero," Villain: ",position_villain)
    
    
    if position_villain=="BB" and position_dic[position_hero]>=0:
        villain_is="OOP"
        hero_is="IP"
        print("Choose Profile:")
        print(profile_IP)
        print("R-Random")
        answer=input("Resposta:")
        if answer!="R" and answer!="r":
            profile=profile_IP[int(answer)]
        else:        
            profile=random.choice(profile_IP)
            p_r_ip=1
        strategy="x_IP"
        if profile!="standart":
            strategy="x_IP_"+profile
            
            
    else:
        villain_is="IP"
        hero_is="OOP"
        print("Choose Profile:")
        print(profile_OOP)
        print("R-Random")
        answer=input("Resposta:")
        if str(answer)!="R" and str(answer)!="r":
            profile=profile_OOP[int(answer)]
        else:        
            profile=random.choice(profile_OOP)
        strategy="OOP"
        if profile!="standart":
            strategy="OOP_"+profile        
    
    if position_dic[position_hero]<=1 and position_villain=="BB":
        flat_range=30
    else:
        flat_range=7
    
    #print("Hero is",hero_is,"Villain is",villain_is," flat range villain ",flat_range)    
    #file='report_'+hero_is+'_Full.csv'
    
    file=flop_choose+'/'+str(flat_range)+'/'+hero_is+'/'+strategy+'.csv'
    df = pandas.read_csv(file, index_col='Hand', names=['Flop','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Half_Bet','BET 3 EV', 'CHECK', 'CHECK EV'] )   
    
    
    cards.append(df.index)
    flop.append(df.Flop)
    
    

        
    if profile=='standart':    
        print("how many turns?")     
        nr_turns=int(input("Resposta"))
        if nr_turns>0:
            turns=1
    print("Quantas maos quer treinar?")
    it=input("Resposta:")
    for i in range (int(it)):
        half_bet=[]
        check_bet=[]
        bet=[]
        check=[]
        flop=[]
        
        ok_hand=0
        while ok_hand==0:            
            hand=random.choice(cards[0])
            if hand!="Hand":
                ok_hand=1
        if p_r_ip==1:        
            profile=random.choice(profile_IP)
            strategy="x_IP"
            if profile!="standart":
                strategy="x_IP_"+profile
        
        if f_r==1:
            flop_choose=random.choice(flops_list)

        file=flop_choose+'/'+str(flat_range)+'/'+hero_is+'/'+strategy+'.csv'
        df_flop = pandas.read_csv(file, index_col='Hand', names=['Flop','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Half_Bet','BET 3 EV', 'CHECK', 'CHECK EV'] )   
        flop.append(df_flop.Flop)
        if profile!="standart":
            df = pandas.read_csv(file, index_col='BET_EV', names=['Flop','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Half_Bet','BET_EV', 'CHECK', 'CHECK_EV'] )   
            #half_bet.append(df.index)
            df.index = pd.to_numeric(df.index, errors='coerce')
            
            df_2 = pandas.read_csv(file, index_col='CHECK_EV', names=['Flop','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Half_Bet','BET_EV', 'CHECK', 'CHECK_EV'] )   
            check.append(df_2.index)        
            df_2.index = pd.to_numeric(df_2.index, errors='coerce')
            
            b=df.index>df_2.index
            df["BET"]=b
            
            check=[]
            x=df_2.index>df.index
            df["CHECK"]=x 
            
            x_b=df_2.index>10000
            df["CHECK_BET"]=x_b        
            
            check_bet.append(x_b)
            bet.append(b)
            check.append(x)
    
        else:
            
            df = pandas.read_csv(file, index_col='Half_Bet', names=['Flop','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Half_Bet','BET 3 EV', 'CHECK', 'CHECK EV'] )   
            #half_bet.append(df.index)
            df.index = pd.to_numeric(df.index, errors='coerce')
    
            df_2 = pandas.read_csv(file, index_col='CHECK', names=['Flop','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Half_Bet','BET 3 EV', 'CHECK', 'CHECK EV'] )   
            df_2.index = pd.to_numeric(df_2.index, errors='coerce')
            
            b=df.index>=65
            df["BET"]=b
            
            check=[]
            x=df_2.index>=65
            df["CHECK"]=x  
            
            x_b=(df_2.index>=35) & (df_2.index<65)
            df["CHECK_BET"]=x_b
            
            check_bet.append(x_b)
            bet.append(b) 
            check.append(x)
                
                
        print("")
        print("Profile:",profile)                                                        
        print("Strategy:",strategy) 
        print("")               
        print("Hero on the",position_hero,"with",hand)
        print("Hero raises to $5 and",position_villain,"calls")
        print("")
        print("Flop ($6):",flop[0][1],"type:",flop_choose)
        if hero_is=="OOP":
            print("Hero...?")
        else:    
            print(position_villain,"checks. Hero...?")
        print("")        
        print("1. Cbet 3")
        print("2. Check")
        print("3. Check/Cbet")
        print(i+1,"/",it)
        answer=input("Resposta:")
        if answer!="1" and answer!="2" and answer!="3":
            answer=1
        df = pandas.read_csv(file, index_col='Hand', names=['Flop','Hand','Weight IP', 'IP Equity', 'IP EV', 'IP EQR', 'Half_Bet','BET 3 EV', 'CHECK', 'CHECK EV'] )   
        df.Half_Bet = pd.to_numeric(df.Half_Bet, errors='coerce')
        for x in range(1,len(cards[0])): 
            #print(x)
            
                
            if hand==cards[0][x]:
                #print (bet[0][x])
                print("ok")
                #print(bet[0][x],check[0][x],check_bet[0][x])
                
                if int(answer)==1 and str(bet[0][x])=="True":
                    print("Resposta certa")
                    score=score+1
                    if turns==1 and profile!="standart":
                        
                        strategy_turn='x_b_c_x_IP'
               
                        for j in range (int(nr_turns)):
                            turn(strategy_turn,flat_range,hero_is,flop_choose,hand,nr_turns)
                        
                if int(answer)==1 and str(bet[0][x])=="False":
                    print("Resposta errada")
                    if str(check_bet[0][x])=="True":
                        print("A Resposta correcta é Check/Bet")
                        score=score+0.5
                    else:
                        print("A Resposta correcta é Check")
                    #print(df.loc[df["Half_Bet"]>=60,["Flop","Half_Bet"]])
                    #print(df.loc[df["Half_Bet"]<=40,["Flop","Half_Bet"]])
                if int(answer)==2 and str(bet[0][x])=="False" and str(check[0][x])=="True" :
                    print("Resposta certa")
                    score=score+1

                    if turns==1 and profile!="standart":
                        
                        strategy_turn='x_x_x_IP'
                        for j in range (int(nr_turns)):
                            turn(strategy_turn,flat_range,hero_is,flop_choose,hand,nr_turns)         
 
    
                if int(answer)==2 and str(bet[0][x])=="False" and str(check_bet[0][x])=="True" :
                    print("Resposta errada")                
                    print("A Resposta correcta é Check/Bet")
                    score=score+0.5
                if int(answer)==2 and str(bet[0][x])=="True":
                    print("Resposta errada")
                    print("A Resposta correcta é CBet")                
    
                        
                if int(answer)==3 and str(check_bet[0][x])=="True" :
                    print("Resposta certa")  
                    score=score+1
                if (int(answer)==3 and str(check_bet[0][x])=="False" ):
                    print("Resposta errada")
                    if str(bet[0][x])=="True":
                        print("A Resposta correcta é CBet")
                        score=score+0.5
                    else:
                        print("A Resposta correcta é Check")                
                        score=score+0.5
                    #print(df.loc[df["Half_Bet"]<=40,["Flop","Half_Bet"]])
                    #print(df.loc[df["Half_Bet"]>=60,["Flop","Half_Bet"]])
                #break                
    print("Score Flops:",(score/(int(it)))*100)                
    print("Score Turns:",(score_turn/(total_turns))*100)                