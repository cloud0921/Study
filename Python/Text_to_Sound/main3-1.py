from gtts import gTTS

text = "안녕하세요. 파이썬입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"Practice\Text_to_Sound\hi.mp3")
