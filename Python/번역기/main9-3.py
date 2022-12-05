from os import linesep
import googletrans

translator = googletrans.Translator() 

read_file_path = r"9. 영어로된 문서를 한글로 자동번역\영어파일.txt"
# python에서 string 앞에 r 을 표기해 주는 것은 해당 string literal을 raw string 으로 만들어 주기 위함이다.  즉 \\이 아닌 \ 쓰기 위함이다.
with open(read_file_path, 'r') as f : 
    readLines = f.readlines()  # string 앞 f 는  formatted string 리터럴 을 의미한다. 즉 직관적인 코드를 작성한다.
for lines in readLines:
    result1 = translator.translate(lines, dest='ko') 
    print(result1.text)
