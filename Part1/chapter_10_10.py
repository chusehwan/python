#Cats and Dogs

filepath_1 = input('filepath')
while True:
    try:
        with open(filepath_1,'r') as f_cats:
            cats = f_cats.read()
            break
    except:
        filepath_1=input('pls try put path again')


cats_words = cats.split()

print(cats.count('cat'))
print(cats.lower())
print(cats.lower().count('cat'))
print(cats_words)
