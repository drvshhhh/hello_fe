fruits = {
    'apple': 1.5,
    'banana': 0.5,
    'orange': 0.8,
    'grape': 2.0,
    'kiwi': 1.2
}

print(max(fruits, key=fruits.get))
