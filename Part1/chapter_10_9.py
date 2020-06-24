#Cats and Dogs

filepath_1 = input('filepath')
while True:
    try:
        with open(filepath_1,'r') as f_cats:
            cats = f_cats.read()
            break
    except:
        pass




cats_words = cats.split()


print(cats_words)
