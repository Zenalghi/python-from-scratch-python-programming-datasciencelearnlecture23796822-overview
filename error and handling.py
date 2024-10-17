def cek_umur():
    age = 0
    while age == 0:
        try: #exception handling
            age = int(input('Umur lu: '))  # Menerima input sebagai integer
            income = 2000#int(input("Duit lu?"))
            risk =income / age
            
            if age == 0:
                print('Yakali 0!! Isi ulang!!')
        except ZeroDivisionError:
            print('Yakali 0!! Isi ulang!!')
        except ValueError:
            print('Input tidak valid! Silakan masukkan angka yang benar.')
    
    if age < 3:
        print('Lu masih batita')
    elif age < 5:
        print('Lu masih balita')
    elif age < 18:
        print('Lu masih bocah')
    else:
        print('Lu udah gede')

# Panggil fungsi untuk menjalankan cek umur
cek_umur()
