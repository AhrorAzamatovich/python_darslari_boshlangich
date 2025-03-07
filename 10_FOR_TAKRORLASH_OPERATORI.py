# FOR TAKRORLASH OPERATORI
# FOR operatori bilan ishlashni o'rganamiz
# for BILAN TANISHAMIZ
# Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin. Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo. 
# Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi. 

# Keling quyidagi misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz. Buning uchun quyidagi kodni yozamiz:

# mehmonlar = ['Sabrina','Jasmina','Bunyod', 'Nigina','Ahror']
# for mehmon in mehmonlar:
#     print(mehmon)

# Keling, kodni tahlil qilaylik. 
# 1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan to'ldirdik.
# 2-qatorda for tsiklini bohladik. Bu qator Pythonga mehmonlar degan ro'yxatdan har bir elementini olib uni yangi, mehmon degan o'zgaruvchiga yuklashni buyuryapti (o'zgaruvchiga istalgan nom berishingiz mumkin. Biz tushunarli bo'lishi uchun mehmon deb atadik)
# 3-qatorda biz mehmon degan o'zgaruvchining qiymatini konsolga chiqardik. Bu tsikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.
# "For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.
# Yuqoridagi kodni oddiy tilga tarjima qilsak "Mehmonlar ro'yxatidagi har bir mehmon uchun uning ismini konsolga chiqar" degan ma'noni beradi. 

# for QANDAY ISHLAYDI:
# Keling yana bir misol ko'raylik. 

# mehmonlar = ['Dilnoza','Madina','Eldor', 'Sardor','Abdulhamid', "Nizomiddin"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Ahmedovlar oilasi.\n")

# Yuqoridagi kodda 2-qator bu tsikl boshi deyiladi. Aynan shu qator kodimiz nech marta takrorlanishini aniqlaydi. Bizning holatimizda tsikl mehmonlar ro'yxati ichidagi elementlar tugagunga qadar takrorlanadi. Tsikl boshlanishi ikki nuqta (:) bilan tugaydi. Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi.  
# Tsikl badani surilish (indentation) bilan ajratiladi, ya'ni tsiklning takrorlanuvchi qismi asosiy koddan bir muncha o'ngroqqa surilgan bo'ladi. Agar biz mana shu surilishni tark qilsak kodimiz xato beradi:

# mehmonlar = ['Sabrina','Jasmina','Bunyod', 'Nigina','Ahror']
# for mehmon in mehmonlar:
# print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Ahmedovlar oilasi.\n")

# Natija: IndentationError: expected an indented block
# Ko'rib turganingizdek for dan keyingi qatorni o'ngga surmaganimiz uchun indentation error (surishda xatolik) degan xabarni oldik.

# Shunigdek, ko'pchilik yo'l qo'yadigan yana bir xato, qo'shimcha qatorlarni surish esdan chiqishi:

# mehmonlar = ['Sabrina','Jasmina','Bunyod', 'Nigina','Ahror']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Ahmedovlar oilasi.\n")

# Yuqoridagi kodimizda 4-qatorni o'ngga surmaganimiz uchun, Python bu qatorni tsikl tashqarisida deb qabul qildi va faqatgina 1 marta, tsikl tugaganidan so'ng bajardi. 
# Huddi shu kabi agar takrorlanishi kerak bo'magan kodni tsikldan so'ng o'ngga surib qo'ysak Python bu qatorni tsiklning tarkibida deb hisoblab, qayta-qayta bajaradi:

# mehmonlar = ['Sabrina','Jasmina','Bunyod', 'Nigina','Ahror']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
 
#     print("Hurmat bilan, Ahmedovlar oilasi.\n")

# Yuoqirdagi misolda 5-qator o'ngga surilib qolgani uchun Python bu qatorni ham bir necha bor takrorlab, konsolga chiqardi. To'g'ri kod quyidagicha bo'ladi:

# mehmonlar = ['Sabrina','Jasmina','Bunyod', 'Nigina','Ahror']
# for mehmon in mehmonlar:
#     print(mehmon)

# print(mehmonlar)

# for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
# Keling quyidagi misolni ko'ramiz

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# for yordamida yangi ro'yxat ham shakllantirish mumkin:

# sonlar = list(range(1,11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

# print(sonlar)
# print(sonlar_kvadrati)

# for va input()
# for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:

# dostlar = [] # bo'sh ro'yxat
# print("6 ta eng yaqin do'stingiz kim?")
# for n in range(6): # n bu yerda 0 dan 7 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(f"{dostlar}".title())


# a=list(range(6))
# print(a)
# Kodni tahlil qilamiz:
# 1-qatorda bo'sh dostlar ro'yxatini yaratdik
# 2-qatorda ekranga "6 ta eng yaqin do'stingiz kim?" degan xabarni chiqardik
# 3-qatorda tsiklni boshladik. range(6) funktsiyasi 0 dan 7 gacha sonlar ketma-ketligini yaratadi (0,1,2,3,4,5,6) tsikl esa n shularning har biriga teng bo'lib chiqquncha davom etadi. 
# 4-qatorda tsikl badani kelgan. Bu yerda biz foydalanuvchidan n+1 do'stingizni kiriting deb so'radik. Nima uchun n+1 (n emas)? Sababi n 0 dan 4 gacha qiymatlarni oladi, foydalanuvchiga tushunarli bo'lishi uchun esa biz "0-do'stingizni ismini kiriting:" deb emas, balki n+1 ya'ni 1-ismni kiriting deb murojat qilyapmiz.
# 5-qatorda shakllangan ro'yxatni konsolga chiqardik.

# for tsikli har qanday dasturlash tilining eng muhim qismlaridan hisoblanadi va biz bu operatoraga hali takror-takror qaytamiz.

# AMALIYOT

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.