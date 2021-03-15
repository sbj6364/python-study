'''
문제
문자열 내 모든 단어의 첫 글자를 대문자로 바꾸는 코드를 작성하세요.
'''

s = "hello world"

def capitalize_every_word(s):
    return s.title()

print(capitalize_every_word(s))