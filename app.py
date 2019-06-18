from mirai import Mirai
import time
import threading
import paho.mqtt.client as mqtt

mirai = None

def mqtt_connected(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("pepper/#")


def mqtt_message(client, userdata, msg):
	topic = msg.topic
	payload = msg.payload

	if topic == 'pepper/say':
		mirai.speech().set_speed(40).say(payload)
	elif topic == 'pepper/dab':
		mirai.motion().run('mirai_moves/dab')
	elif topic == 'pepper/wave':
		mirai.motion().run('animations/Stand/Gestures/Hey_1')
	elif topic == 'pepper/bow':
		mirai.motion().run('animations/Stand/Gestures/BowShort_1')
		mirai.motion().stand()
	elif topic == 'pepper/show_1':
		show_1()

def show_1():
	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Hey_1',)).start()
	time.sleep(.4)
	mirai.speech().set_volume(0.5).set_language("Dutch")
	mirai.speech().set_speed(150).say("Hey Hallo!")
	time.sleep(.4)
	mirai.speech().set_speed(40).say("Ik ben Miray")
	mirai.speech().set_speed(40).set_volume(0.8).say("en ik ben een robot").set_volume(0.5)

	time.sleep(.6)

	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Explain_8',)).start()
	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Explain_6', 2)).start()
	mirai.speech().set_speed(40).say("Ik woon hier bij de hogeschool van amsterdam, tussen de informatica studenten.")
	mirai.motion().set_head(0, 0)

	threading.Thread(target=mirai.motion().run, args=('mirai_moves/dab',)).start()

def program():
	#show_1()
	print("Computer says no")

if __name__ == '__main__':
	mirai = Mirai("145.28.47.180")

	mqtt_client = mqtt.Client(client_id="pepper_robot")
	mqtt_client.on_connect = mqtt_connected
	mqtt_client.on_message = mqtt_message
	mqtt_client.username_pw_set("ldr", "xJPriWagGxc68tpwYmDdHWEkg")
	mqtt_client.connect("akoo.nl", 7777, 60)

	threading.Thread(target=program).start()
	mqtt_client.loop_forever()



#mirai.motion().run('animations/Stand/Emotions/Neutral/Embarrassed_1')


#exit()
#mirai.motion().run('animations/Stand/Gestures/Hey_1')



#mirai.motion().run('mirai_moves/dab')
#mirai.motion().run('animations/Stand/Gestures/Hey_6')
#mirai.motion().run('animations/Stand/Gestures/Nothing_1')
#mirai.motion().stand()

#mirai.motion().dab()


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