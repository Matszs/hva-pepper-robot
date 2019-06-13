from mirai import Mirai
import time
import threading

mirai = Mirai("145.28.47.180")

mirai.motion().run('animations/Stand/Gestures/Hey_1')


#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Hey_1',)).start()




#mirai.motion().run('mirai_moves/dab')
#mirai.motion().run('animations/Stand/Gestures/Hey_6')
#mirai.motion().run('animations/Stand/Gestures/Nothing_1')
#mirai.motion().stand()

#mirai.motion().dab()

#mirai.speech().set_volume(0.5).set_language("Dutch")
#mirai.speech().set_speed(150).say("Hey Hallo!")
#time.sleep(.4)
#mirai.speech().set_speed(40).say("Ik ben Miray")
#mirai.speech().set_speed(40).set_volume(0.8).say("en ik ben een robot").set_volume(0.5)

#mirai.motion().wave()
#time.sleep(3)









#mirai.motion().wake_up().set_head(-0.5, -0.5)
#time.sleep(3)
#mirai.motion().set_head(0.5, 0.5)

#mirai.sleep()
#time.sleep(10)
#mirai.wake_up()
#time.sleep(3)

#mirai.motion().rotate()


'''while True:
	mirai.motion().move_head_left()
	mirai.motion().arm_up('right').arm_down('left')
	time.sleep(10)
	mirai.motion().move_head_right()
	mirai.motion().arm_down('right').arm_up('left')
	time.sleep(10)'''

'''mirai.speech().set_language("Dutch")
mirai.speech().say("Hi ik ben Mirai en ik ben een robot.")
mirai.speech().say("Excuses dat sommige mensen naar mijn rug moeten kijken")
mirai.speech().say("Ik woon bij hbo-ict. Hbo-ict is een community van 10000 studenten, 2000 docenten en 200 studenten studeren dit jaar af.")

mirai.speech().say("Wat we daar doen? Heel simpel. Met ICT de wereld beter en mooier maken.")
mirai.speech().say("De toekomst van ICT is dat ik en mijn robot genoten jullie leven makkelijker gaan maken.")

mirai.speech().say("Dat er grote uitdagingen zijn.")
mirai.speech().say("We zijn allemaal heel sociaal, maar ondertussen ook depressief.")
mirai.speech().say("Wereld beter en eerlijker maken")
mirai.speech().say("de hbo-ict community doet dit al in de zorg en onderwijs")
mirai.speech().say("Hbo-ict community van docenten studenten en bedrijven doen dit al")

mirai.speech().say("helpen met dementie")
mirai.speech().say("kinderen helpen met leerachterstand")'''