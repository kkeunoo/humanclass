import re
text = ' 고양이입니다.  반갑습니다! 다음입니다? 끝 '
sentences = re.split(r'(?<=[.!?])\s+', text.strip())
print(sentences)
print(re.split(r'(?<=[.!?])\s+', '하나.둘'))
