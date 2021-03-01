"""                                    @DeCoder_uz                                         """

import pyttsx3
engine = pyttsx3.init() # object yaratish

""" RATE """
rate = engine.getProperty('rate')   # hozirgi nutq tezligi tafsilotlarini olish
print (rate)                        # tafsilotlarni consolga chiqarish
engine.setProperty('rate', 125)     # yangi ovoz tezligini sozlash


""" VOLUME """
volume = engine.getProperty('volume')   # joriy tovush darajasi bilan tanishish (min = 0 va max = 1)
print (volume)                          # tafsilotlarni consolga chiqarish
engine.setProperty('volume',1.0)    	# tovush darajasini sozlash

""" VOICE """
voices = engine.getProperty('voices')       # hozirgi ovoz tafsilotlarini olish
#engine.setProperty('voice', voices[0].id)  # indexni almashtirish, ovozni almashtirish. 0 erkak
engine.setProperty('voice', voices[1].id)   # indexni almashtirish, ovozni almashtirish. 1 ayol

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

""" Ovozni saqlab qo'yish """
# Linuxda 'espeak' va 'ffmpeg' o'rnatilganligiga ishonch hosil qiling
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()