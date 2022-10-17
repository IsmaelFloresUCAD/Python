# Practica Clase 5: Calculadora Conversión de números entre sistemas decimal, binario, octal y hexadecimal
# Mejora el programa en clase.
# Implementación: Flores Rosas Ismael Isaac
# Version 1.0 -> 17 Octubre 2022 

print('Calculadora de conversión entre Sistemas Numéricos.')
print('      Decimal - Binario - Octal - Hexadecimal      ')
print('---------------------------------------------------')
print('        Símbolos de cada sistema numérico:         ')
print('* Decimal      (base 10):  0,1,2,3,4,5,6,7,8,9')
print('* Binario      (base 2):   0,1')
print('* Octal        (base 8):   0,1,2,3,4,5,6,7')
print('* Hexadecimal  (base 16):  0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F')
print('---------------------------------------------------')
decimal = int(input('Ingrese número (base 10): '))                  #Pide al usuario el número a convertir (1...1000000)

binario_pfx = bin(decimal)                                          #Se utiliza la función bin() para convertir el numero decimal a binario y guardarlo en la variable binario_pfx.
binario = binario_pfx[2:]                                           #[2:] Indica que almacene a partir del 3er digito del valor binario obtenido excluyendo prefijo '0b' en la variable binario.
hexadecimal_pfx = hex(decimal)                                      #Se utiliza la función hex() para convertir el numero decimal a hexadecimal y guardarlo en la variable hexadecimal_pfx.
hexadecimal = hexadecimal_pfx[2:]                                   #[2:] Indica que almacene a partir del 3er digito del valor hexadecimal obtenido excluyendo prefijo '0x' en la variable hexadecimal.
octal_pfx = oct(decimal)                                            #Se utiliza la función oct() para convertir el numero decimal a octal ey guardarlo en la variable octal_pfx.
octal = octal_pfx[2:]                                               #[2:] Indica que almacene a partir del 3er digito del valor octal obtenido excluyendo prefijo '0o'  en la variable octal.

print("{:<15} {:<20} {:>4}".format('Sistema','Número','Base'))      #Genera una tabla con 3 columnas de 15,20 y 4 espacio ->Título de la tabla
print("{:<15} {:<20} {:>4}".format('Decimal',decimal,10))           #Genera una tabla con 3 columnas de 15,20 y 4 espacio ->Valores decimales
print("{:<15} {:<20} {:>4}".format('Binario',binario,2))            #Genera una tabla con 3 columnas de 15,20 y 4 espacio ->Valores binarios
print("{:<15} {:<20} {:>4}".format('Octal',octal,8))                #Genera una tabla con 3 columnas de 15,20 y 4 espacio ->Valores octales
print("{:<15} {:<20} {:>4}".format('Hexadecimal',hexadecimal,16))   #Genera una tabla con 3 columnas de 15,20 y 4 espacio ->Valores hexadecimales
print('---------------------------------------------------')





