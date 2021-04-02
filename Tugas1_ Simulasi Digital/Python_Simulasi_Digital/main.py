'''
Created on Jan 21, 2021

@author: RICKY
'''
from Program_AljabarBoolean import operasiBitwise

main = operasiBitwise()
 
count = 'y'
while count == "y" or count == "Y":
    
    print("------OPERASI ALJABAR BOOLEAN------")
    print("1. Gerbang logika")
    print("2. Konvesi bilangan")
    print("-----------------------------------")
    print()
    
    main.cekPilihan()
         
    count = input("Apakah ingin mengulang program lagi?(y/n)")

print("Terima Kasih , program diakhiri")