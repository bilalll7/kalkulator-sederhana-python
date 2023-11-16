print(20*'=')
print('Kalkulator')
print(20*'=')

angka1 = float(input('Masukan angka ke-1 : '))
operator = input('Masukan operator yg akan dipilih +,-,*,/ : ')
angka2 = float(input('Masukan angka ke-2 : '))

if operator == '+':
  hasil = angka1 + angka2
  print('Hasilnya adalah: ', hasil)
elif operator == '-':
  hasil = angka1 - angka2
  print('Hasilnya adalah: ', hasil)
elif operator == '*':
  hasil = angka1 * angka2
  print('Hasilnya adalah: ', hasil)
elif operator == '/':
  hasil = angka1 / angka2
  print('Hasilnya adalah: ', hasil)