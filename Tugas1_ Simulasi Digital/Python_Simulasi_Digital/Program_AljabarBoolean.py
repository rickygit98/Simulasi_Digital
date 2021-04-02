'''
Created on Jan 20, 2021

@author: RICKY
'''
class operasiBitwise():
    
    def cekPilihan(self):
        cek = 0
        while not cek:
            pilihan = int(input("PILIH OPERASI YANG INGIN DILAKUKAN : "))    
            if pilihan == 1:
                self.displayBitwise()
                break
            elif pilihan == 2:
                self.displayConverter()
                break
            else:
                print("Masukkan nomor yang tertera pada pilihan!")
                cek == 0
                
    def Bitwise(self,a,b):
        
        print(f'a bernilai = {a} (10) , dalam biner = {bin(a)} (2)')
        print(f'b bernilai = {b} (10) , dalam biner = {bin(b)} (2)')
        
        print(f'a AND b = {a & b} = {bin(a & b)}')
        print(f'a OR b = {a | b} = {bin(a | b)}')
        print(f'a XOR b = {a ^ b} = {bin(a ^ b)}')
        
        print(f'COMPLEMENT a = {~a} = {bin(~a)}')
        print(f'COMPLEMENT b = {~b} = {bin(~b)}')
        
        print(f'LEFT SHIFT a = {a<<2} = {bin(a<<2)}')
        print(f'LEFT SHIFT b = {b<<2} = {bin(b<<2)}')
        
        print(f'RIGHT SHIFT a = {a>>2} = {bin(a>>2)}')
        print(f'RIGHT SHIFT b = {b>>2} = {bin(b>>2)}')
        print()
        
    def konversiBilangan(self,n):
        print(f'Desimal n bernilai = {n} (10)')
        print(f'Biner n bernilai = {bin(n)} (2)')
        print(f'Octal n bernilai = {oct(n)} (8)')
        print(f'Hexadecimal n bernilai = {hex(n)} (16)')
        print()
        
    def displayBitwise(self):
        print()
        print("------------------------OPERASI BITWISE (LOGIKA)---------------------------------")
        
        print()
        operation = operasiBitwise()
        
        a = int(input("Masukkan bilangan pertama :"))
        b = int(input("Masukkan bilangan kedua :"))
        
        operation.Bitwise(a, b)
        
        print()
        
    def displayConverter(self):
        print()
        print("----------------------- KONVERSI BILANGAN ---------------------------------------")
        
        print()
        operation = operasiBitwise()
        n = int(input("Masukkan Bilangan yang ingin dikonversi :"))
        operation.konversiBilangan(n)