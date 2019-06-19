# coding=utf-8
from mirai import Mirai
import time
import threading
import paho.mqtt.client as mqtt

DEFAULT_TEXT_SPEED = 100 # 50 - 400

mirai = None

def mqtt_connected(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("pepper/#")


def mqtt_message(client, userdata, msg):
	topic = msg.topic
	payload = msg.payload

	print("mqtt :: " + topic)

	if topic == 'pepper/say':
		mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay(payload)
	elif topic == 'pepper/dab':
		mirai.motion().run('mirai_moves/dab')
	elif topic == 'pepper/wave':
		mirai.motion().run('animations/Stand/Gestures/Hey_1')
	elif topic == 'pepper/animation':
		mirai.motion().run(payload)
	elif topic == 'pepper/bow':
		mirai.motion().run('animations/Stand/Gestures/BowShort_1')
		mirai.motion().stand()
	elif topic == 'pepper/stand':
		mirai.motion().stand()
	elif topic == 'pepper/sleep':
		mirai.motion().sleep()
	elif topic == 'pepper/show_1':
		show_1()
	elif topic == 'pepper/show_2':
		show_2()
	elif topic == 'pepper/show_3':
		show_3()
	elif topic == 'pepper/show_4':
		show_4()
	elif topic == 'pepper/start_face':
		mirai.face_detection().start_detection()
	elif topic == 'pepper/stop_face':
		mirai.face_detection().stop_detection()
	elif topic == 'pepper/staying_alive':
		dance_staying_alive()
	elif topic == 'pepper/single_ladies':
		dance_single_ladies()


def show_1():
	print("show 1")

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Hey_1',)).start()
	#time.sleep(.4)

	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("^mode(disabled) ^start(animations/Stand/Gestures/Hey_1) Hallo, ik ben dus miray, en ik ben een robot ^wait(animations/Stand/Gestures/Hey_1) ^mode(contextual) maar dat zag je waarschijnlijk al!")
	mirai.speech().asay("Ik woon sinds kort bij de ha b o ICT. en daar zijn wij heel blij mee!")

	mirai.speech().set_speed(90).asay("ha")
	mirai.speech().asay("ha")
	mirai.speech().asay("ha")
	time.sleep(.4)
	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("^mode(disabled) ^start(animations/Stand/Gestures/No_3) Nee zo lachen robots niet ^wait(animations/Stand/Gestures/No_3) ^mode(contextual)")
	mirai.motion().stand(0.7)

	mirai.motion().rotate_halfway()

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Explain_1',)).start()

	mirai.speech().asay("^mode(disabled) ^start(animations/Stand/Gestures/Explain_1) Ook een goede middag voor jullie ^wait(animations/Stand/Gestures/Explain_1) ^mode(contextual)")
	time.sleep(.4)

	mirai.speech().asay("Excuses dat jullie tegen mijn rug moeten kijken, het is een ingewikkeld podium")
	time.sleep(.4)

	mirai.speech().asay("Ik draai weer terug waar ik gebleven was")
	time.sleep(.4)


	mirai.motion().stand()
	mirai.motion().rotate_halfway_back()

	mirai.speech().asay("Oh ja")
	time.sleep(.4)

	mirai.speech().asay("Om even alle misverstanden te voorkomen beste aanwezigen, wil ik jullie uitleggen wat voor robot ik ben")
	time.sleep(.4)

	mirai.speech().asay("Of misschien juist laten zien wat voor robot ik niet ben")
	time.sleep(.4)

	mirai.speech().asay("Kijk maar even mee.")
	time.sleep(.4)

	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/ShowTablet_2',)).start()
	mirai.tablet().open_page('video_1.html')
	time.sleep(10) # do nothing for 10 seconds
	mirai.tablet().open_page('index.html') # back to default screen

	threading.Thread(target=mirai.motion().stand).start()
	time.sleep(.6)

	mirai.speech().asay("Dit ben ik dus niet")
	time.sleep(.4)

	mirai.speech().asay("Ik ben een robot die geprogrammeerd kan worden om mensen te helpen")
	time.sleep(.4)

	mirai.speech().asay("Hier helpt bijvoorbeeld mijn zus Elvie burgers in het gemeentehuis van Leidschendam")
	time.sleep(.4)

	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/ShowTablet_3',)).start()
	mirai.tablet().open_page('video_1.html')
	time.sleep(10)  # do nothing for 10 seconds
	mirai.tablet().open_page('index.html')  # back to default screen

	time.sleep(.6)

	threading.Thread(target=mirai.motion().stand).start()

	mirai.speech().set_speed(20).asay("Of mijn andere zus fie die in de zorg werkt, om patiënten met verstandelijke beperkingen, te helpen met oefeningen of, eenzaamheid te bestrijden")
	time.sleep(.4)

	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Excited_1',)).start()
	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("dat noem ik pas klantenservice!")
	time.sleep(.4)

	mirai.motion().stand()

	#mirai.speech().set_speed(40).set_volume(0.8).asay("en ik ben een robot").set_volume(0.5)

	#time.sleep(.6)

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Explain_8',)).start()
	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Explain_6', 2)).start()
	#mirai.speech().set_speed(40).asay("Ik woon hier bij de hogeschool van amsterdam, tussen de informatica studenten.")
	#mirai.motion().set_head(0, 0)

	#threading.Thread(target=mirai.motion().run, args=('mirai_moves/dab',)).start()


def show_2():
	print("show 2")

	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("Komend jaar gaan studenten van de opleiding ha b o - ict met mij aan de slag. om uit te zoeken hoe ik mijzelf nuttig kan maken.")
	time.sleep(.4)

	# quotes with fingers

	threading.Thread(target=mirai.tablet().open_page, args=('video_2.html', 1)).start()
	mirai.speech().asay("De studenten van ha b o - ict zijn echte toppers")

	#mirai.tablet().open_page('video_2.html')
	time.sleep(6)  # do nothing for 6 seconds

	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/No_3',)).start()
	mirai.tablet().open_page('index.html')  # back to default screen

	mirai.speech().set_speed(40).set_pitch(1.8).asay("Nee!")
	mirai.speech().set_pitch(0.8).asay("Nee!")
	mirai.speech().set_pitch(0.5).asay("Nee!")
	mirai.speech().set_pitch(0.9).asay("Dit loopt helemaal in de soep!")

	mirai.speech().set_default_pitch()

	time.sleep(.8)
	mirai.speech().asay("^mode(disabled) ^start(animations/Stand/Gestures/Enthusiastic_5) hahaha dit is nou ict humor! ^wait(animations/Stand/Gestures/Enthusiastic_5) ^mode(contextual)")
	threading.Thread(target=mirai.motion().stand).start()
	time.sleep(.8)

	mirai.speech().asay("Even terug naar mijn verhaal")
	time.sleep(.4)


def show_3():
	print("show 3")

	threading.Thread(target=mirai.motion().head_move_1).start()

	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("ha b o - ict heeft mij gevraagd jullie toe te spreken en te vertellen over wat wij als opleiding doen.")
	time.sleep(.4)

	mirai.speech().asay("^mode(disabled) ^start(animations/Stand/Gestures/Give_3) ha b o - ict is een community van studenten, docenten, onderzoekers en bedrijven  ^wait(animations/Stand/Gestures/Give_3) ^mode(contextual) die een hart hebben voor ict.")
	threading.Thread(target=mirai.motion().stand).start()
	time.sleep(.4)

	mirai.speech().asay("Ik ben aan de slag gegaan met data zodat jullie een beeld kunnen krijgen.")

	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Waiting/ShowSky_1',)).start()
	time.sleep(6)  # do nothing for 6 + 2 seconds because of info graphic
	mirai.motion().stand()
	time.sleep(2)  # do nothing for 6 + 2 seconds because of info graphic

	mirai.speech().asay("Wij proberen de wereld eerlijker, beter en mooier te maken met ICT.")
	time.sleep(.4)

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/YouKnowWhat_1',)).start()
	mirai.speech().asay("Je kan ons zien als")
	time.sleep(.5)
	mirai.speech().asay("^mode(disabled) ^start(animations/Stand/Gestures/YouKnowWhat_1) de moeder teresa van de ict ^wait(animations/Stand/Gestures/YouKnowWhat_1) ^mode(contextual)")

	threading.Thread(target=mirai.motion().stand).start()
	time.sleep(2)  # fragment moeder theresa

	mirai.speech().asay("Ok ok, misschien is dat een beetje overdreven.")
	time.sleep(.4)
	mirai.speech().asay("Ik ben hier gewoon nog niet zo goed in.")
	time.sleep(.4)
	mirai.speech().asay("Over ICT praten is ook zo 19 80.")
	time.sleep(.4)

	time.sleep(2)  # oude computer + pacman


def show_4():
	print("Show 4")

	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("ict moet je beleven. Daarom heeft ha b o - ict speciaal voor jullie een expositie ingericht.")
	time.sleep(.4)
	mirai.speech().asay("Bezoek de ha b o - ict tent deze week en maak kennis met onze studenten en hun werk.")
	time.sleep(.4)
	mirai.speech().asay("Ben je benieuwd geworden? Neem hier alvast een kijkje.")

	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/ShowTablet_3',)).start()
	mirai.tablet().open_page('video_1.html')
	time.sleep(8)  # do nothing for 10 seconds
	mirai.motion().stand()
	time.sleep(2)
	mirai.tablet().open_page('index.html')  # back to default screen

	time.sleep(1)

	mirai.speech().asay("Ik hoop je daar snel te zien!")

	mirai.motion().run('mirai_moves/dab')

	mirai.speech().asay("laters")

	mirai.motion().run('animations/Stand/Gestures/BowShort_1')

	time.sleep(.5)

	mirai.sleep()

	time.sleep(1)

	mirai.speech().asay("Hallo?")
	time.sleep(.8)
	mirai.speech().set_speed(50).asay("Hallo?")
	time.sleep(.4)
	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("Kan iemand mij van het podium tillen")


def on_face_detected_callback(count):
	print("face detected: " + str(count))
	mirai.speech().asay("Welkom! Heb een mooie dag!")

	mirai.motion().stand()


def dance_staying_alive():
	mirai.audio_player().play_song("staying_alive.wav")
	time.sleep(.8)
	mirai.motion().run('mirai_moves/dance_1')
	mirai.motion().stand()


def dance_single_ladies():
	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/BowShort_1',)).start()
	mirai.audio_player().play_song("single_ladies.wav")
	time.sleep(1)
	mirai.motion().stand(0.5)
	mirai.motion().run('mirai_moves/dance_2')
	mirai.motion().stand()

def on_speech_recognized(word):
	mirai.speech_recognition().stop()

	if word == 'technische informatica':
		mirai.speech().asay("Technische Informatica is een opleiding.")
	elif word == 'bim':
		mirai.speech().asay("Business en IT management is een opleiding.")
	elif word == 'game development':
		mirai.speech().asay("Game development is een opleiding.")
	elif word == 'software engineer':
		mirai.speech().asay("Software engineer is een opleiding.")
	elif word == 'cyber security':
		mirai.speech().asay("Ceiber security is een opleiding.")

	mirai.speech_recognition().start()

def program():
	print("Program started")

	mirai.speech().set_volume(1.0).set_language("Dutch")
	mirai.speech_recognition().set_language("Dutch")

	mirai.face_detection().set_on_face_detected_callback(on_face_detected_callback)
	mirai.face_detection().set_timeout(60000)

	mirai.speech_recognition().set_on_speech_recognized_callback(on_speech_recognized)
	mirai.speech_recognition().set_word_list(['bim', 'technische informatica', 'game development', 'software engineer', 'cyber security'])
	mirai.speech_recognition().start()

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
mirai.speech().asay("Hi ik ben Mirai en ik ben een robot.")
mirai.speech().asay("Excuses dat sommige mensen naar mijn rug moeten kijken")
mirai.speech().asay("Ik woon bij hbo-ict. Hbo-ict is een community van 10000 studenten, 2000 docenten en 200 studenten studeren dit jaar af.")

mirai.speech().asay("Wat we daar doen? Heel simpel. Met ICT de wereld beter en mooier maken.")
mirai.speech().asay("De toekomst van ICT is dat ik en mijn robot genoten jullie leven makkelijker gaan maken.")

mirai.speech().asay("Dat er grote uitdagingen zijn.")
mirai.speech().asay("We zijn allemaal heel sociaal, maar ondertussen ook depressief.")
mirai.speech().asay("Wereld beter en eerlijker maken")
mirai.speech().asay("de hbo-ict community doet dit al in de zorg en onderwijs")
mirai.speech().asay("Hbo-ict community van docenten studenten en bedrijven doen dit al")

mirai.speech().asay("helpen met dementie")
mirai.speech().asay("kinderen helpen met leerachterstand")'''