rating = [7, 5, 3, 3, 2]
new_rating = int(input("Ведите рейтинг: "))
i = 0
for r in rating:
    if new_rating <= r:
        i += 1
rating.insert(i, str(new_rating))
print(rating)



