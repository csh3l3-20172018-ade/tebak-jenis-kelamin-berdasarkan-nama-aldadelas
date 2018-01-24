# lakilaki dan perempuan adalah variable klasifikasi untuk huruf yang telah ditentukan.
lakilaki = 0
perempuan = 0

names = raw_input("Your name : ").lower().split(" ")
Fname = names[0] # mengambil nama depannya saja
Arr = list(Fname) # konversi nama depan dari string ke dalam sebuah list char

# a,i,u,e,t,l adalah huruf yang sering muncul di nama perempuan. sehingga variable perempuan akan bertambah valuenya
# b, d, dan o adalah huruf yang sering muncul di nama laki laki. sehingga variable lakilaki akan bertambah valuenya
for name in Arr:
    if name == "a" or name == "i" or name == "u" or name == "e" or name == "t" or name == "l":
        perempuan = perempuan + 1
    elif name == "b" or name == "d" or name == "o":
        lakilaki = lakilaki + 1

if perempuan > lakilaki:
    print("seorang perempuan")
elif lakilaki > perempuan:
    print("seorang laki laki")
else:
    print("Tidak diketahui")