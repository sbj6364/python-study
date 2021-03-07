candies = ['딸기맛','레몬맛','수박맛','우유맛','콜라맛','포도맛']
dodo_candies = []

for i in range(len(candies)):
    if candies[i] == '딸기맛':
        cat_candy = candies[i]
    if candies[i] == '레몬맛':
        duck_candy = candies[i]
    if candies[i] == '우유맛' or candies[i] == '콜라맛' or candies[i] == '포도맛':
        dodo_candies.append(candies[i])

print('체셔고양이에게는',cat_candy,'사탕을 줘요.')
print('오리에게는',duck_candy,'사탕을 줘요.')
print('도도새에게는',dodo_candies,'사탕을 줘요.')