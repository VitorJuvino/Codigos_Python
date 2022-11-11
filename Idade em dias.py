# Atividade do beecrowd

def main():

   i = int(input())

   a = i // 365

   m = i % 365 // 30

   d = i % 365  % 30

   print(f'{a} ano(s)')
   print(f'{m} mes(es)')
   print(f'{d} dia(s)')


main()

   