'''
문제
섭씨온도를 화씨온도로 바꾸는 코드
'''
celsius = 180

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return int(fahrenheit)

print(celsius_to_fahrenheit(celsius))