candies = ['딸기맛','레몬맛','수박맛','박하맛','우유맛']

# 조건1) 콜라맛, 포도맛 사탕을 candies에 추가.
candies.append('콜라맛') # 콜라맛 사탕 추가
candies.append('포도맛') # 포도맛 사탕 추
print(candies)

# 조건2) candies에서 박하맛 사탕을 제거.
for i in range(len(candies)-1): # 가방을 하나씩 훑어보다가
    if candies[i] == '박하맛': # 사탕이 박하맛이면
        del candies[i] # 해당 사탕을 제거한다.
print(candies)