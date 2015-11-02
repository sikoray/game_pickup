# -*- coding: utf-8 -*-

import time

print ("екшен сторі 'Мастєр пікапу'")
time.sleep(1)
print (".............................................................................")
time.sleep(1)
print("Ти самець у розквіті сил, який шукає самку на сьогоднішню ніч")
time.sleep(1)
print('Місце:')
time.sleep(1)
print('якийсь прокурений барєвіч')
time.sleep(1)
print('Час:')
time.sleep(1)
print('середа 22:05')
time.sleep(1)
print('за барною стійкою три чікі')
time.sleep(1)
print('Nina-задротка')
time.sleep(1)
print('Oksana-бичка')
time.sleep(1)
print('Lera-високомірна турістка зі сталіци ')
time.sleep(1)
print('Для вибору цілі напиши її  імя')
time.sleep(1)

Nina={11:"Nina:перших шість цифр числа Пі?",12:"Nina:дивлюсь не такий вже й тупий як виглядаєш:)а скажи з якого числа починає рахувати пайтон?",13:"Nina:МАЛАДЄЦ!!!(але швидше за все тобі сьогодні не світить,бо в неї не бриті ноги, але тести сильно мудрої тьолочки ти пройшов)"}
Oksana={21:"Oksana:здорова, пити будеш?",22:"Oksana:ну це вже інтірєсно,а ШО пєш?",23:"Oksana:пічаль-боль, мама зятя не шукає",24:"Oksana:ШИК-БЛЄСК, але нинька мені треба хлопа,а не гламура",25:"Oksana:файно, батя оцінить такого зятя,гайда на сіновал"}
Lera={31:"Lera:Чьо нада?",32:"Lera:я твоя, мой павєлітєль...любі мєня,любі",33:"Lera:пішов нахрєн слабак"}
you={40:"you:привіт мацьонька",41:"ти підходиш до неї, але не встигаєш нічого сказати, як вона ставить запитання",42:'ти розумієш що ситуацію треба терміново брати у свої руки,дати їй в бошку?',43:"ти просто розвернувся і пішов",44:"ТИ БОГ ПІКАПУ!!!",45:"Ти програв!!!Вдалого вечора,дрочєр;)"}
y=1
n=0
while True:
    choice = input ('Кого обираєш?')
    if choice == Nina:
        print (you[41])
        time.sleep(2)
        print (Nina[11])
        
        while True:
            choice=input ('Пі=')
            if choice == 3.14159:
                print (Nina[12])            
                break
                    
        while True:
            choice=input ('?')
            if choice == 0:
                print (Nina[13])
                break                   
                       
    if choice == Oksana:
        print (you[40])
        time.sleep(2)
        print (Oksana[21])
        
        while True:
            choice=input ('y/n')
            if choice ==1:
                print (Oksana[22])
            if choice == 0:                
                print (Oksana[23])
                time.sleep(2)
                print(you[45])
            break
                

        while True:
            whiski=1
            vodka=2
            choice=input ('whiski/vodka')
            if choice == 1:
                print (Oksana[24])
                time.sleep(2)
                print(you[45])
            elif choice == 2:
                print (Oksana[25])
                time.sleep(2)
                print (you[44])
            break                

    if choice == Lera:
        print (you[40])
        time.sleep(2)
        print (Lera[31])
        time.sleep(2)
        print(you[42])
        while True:
            
            choice=input ('y/n')
            if choice ==1:
                print (Lera[32])

                time.sleep(2)
                print (you[44])
            elif choice == 0:
                print (you[43])
                time.sleep(2)
                print (Lera[33])
                time.sleep(2)
                print(you[45])
            
            break
                    
        
    break
time.sleep(1)
print (".............................................................................")
time.sleep(1)
print ("Всі герої цієї мініатюрки видумані.Під час написання коду ніхто не постраждав")

        
