print("здраствойте")
print("Это перевотчик сленга нашово времини ")
print("напиши слова непонятное каторые ты гдето услышал (большими буквами!)")
for i in range(5):  
    word = input("Введите непонятное слово : " ).upper()
    meme_dict = {
                "КРИНЖ": "Что:то очень странное или стыдное",
                "ЛОЛ": "Что:то очень смешное",
                "КРИНЖ" : "что:то странное, стыдное",
                "РОФЛ" : "шутка",
                "ЩИЩ" : "одобрение или восторг",
                "КРИПОВЫЙ" : "страшный, пугающий",
                "АГРИТЬСЯ" : "злиться",
                }
    
    
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Нет!")