pw = ['re23749','rey2356','rad24567']

max_attempts = 3
attempts = 0
correct_passwords = 0

while attempts < max_attempts and correct_passwords < len(pw):
    attempts += 1
    password = input(f"Masukkan password {correct_passwords + 1}: ")
    if password == pw[correct_passwords]:
        print(f"Password {correct_passwords + 1} benar!")
        correct_passwords += 1
    else:
        remaining_attempts = max_attempts - attempts
        print(f"Password salah. Anda memiliki {remaining_attempts} percobaan lagi untuk password {correct_passwords + 1}.")

if correct_passwords == len(pw):
    print("Selamat Anda Login!")
else:
    print("Anda telah melebihi batas percobaan. Akun terkunci.")