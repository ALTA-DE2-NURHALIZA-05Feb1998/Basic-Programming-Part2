'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
harga_awal = 370000
diskon = 15/100

harga_diskon = 15/100*harga_awal
harga_akhir = harga_awal - harga_diskon

print (f'harga yang harus dibayar adalah :{harga_akhir}')