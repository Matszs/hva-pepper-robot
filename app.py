# coding=utf-8
# error log; tail -f /var/log/naoqi/servicemanager/system.Naoqi_error.log
# Debug log; tail -f /var/log/naoqi/servicemanager/system.Naoqi.log
# Autoload on boot; nano /home/nao/naoqi/preferences/autoload.ini
from mirai import Mirai
import time
import threading
import argparse
import datetime
import paho.mqtt.client as mqtt

DEFAULT_TEXT_SPEED = 100 # 50 - 400

mirai = None
started = False # TODO: Set to False

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
	elif topic == 'pepper/preview_show':
		preview_show()
	elif topic == 'pepper/show_2':
		show_2()
	elif topic == 'pepper/show_3':
		show_3()
	elif topic == 'pepper/show_4':
		show_4()
	elif topic == 'pepper/show_5':
		show_5()
	elif topic == 'pepper/start_face':
		mirai.face_detection().start_detection()
		#mirai.speech_recognition().start()
	elif topic == 'pepper/stop_face':
		mirai.face_detection().stop_detection()
		#mirai.speech_recognition().stop()
	elif topic == 'pepper/staying_alive':
		dance_staying_alive()
	elif topic == 'pepper/single_ladies':
		dance_single_ladies()
	elif topic == 'pepper/reboot':
		mirai.system().reboot()
	elif topic == 'pepper/shutdown':
		mirai.system().shutdown()
	elif topic == 'pepper/start':
		global started
		started = True
	elif topic == 'pepper/showcase1':
		showcase1()
	elif topic == 'pepper/showcase2':
		showcase2()


def show_1():
	print("show 1")
	print(datetime.datetime.now())

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Hey_1',)).start()
	#time.sleep(.4)

	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("^mode(disabled) ^start(animations/Stand/Gestures/Hey_1) Hallo, ik ben dus miray, en ik ben een robot maar dat zag je warschijnlijk al! ^wait(animations/Stand/Gestures/Hey_1) ^mode(contextual)")
	mirai.speech().asay("Ik woon sinds kort bij de opleiding ha b o ICT.")
	mirai.speech().asay("en daar zijn zij heel blij mee!")

	mirai.speech().set_speed(90).asay("ha")
	mirai.speech().asay("ha")
	mirai.speech().asay("ha")
	time.sleep(.4)
	mirai.motion().stand(0.7)

	rotate_done = mirai.motion().rotate_halfway()

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Explain_1',)).start()
	if rotate_done:

		mirai.speech().asay("^mode(disabled) ^start(animations/Stand/Gestures/Explain_1) Ook een goede middag voor jullie ^wait(animations/Stand/Gestures/Explain_1) ^mode(contextual)")
		time.sleep(.4)

		mirai.speech().asay("Excuses dat jullie tegen mijn rug moeten aankijken, het is een ingewikkeld podium")
		time.sleep(.4)

		mirai.speech().asay("Ik draai weer even terug en ga verder waar ik gebleven was.")
		time.sleep(.4)

		mirai.motion().rotate_halfway_back()

	mirai.speech().say("O ja")
	time.sleep(.4)

	mirai.speech().asay("Om even alle misverstanden te voorkomen beste aanwezigen, wil ik jullie uitleggen wat voor robot ik ben")
	time.sleep(.4)

	mirai.speech().asay("Of misschien juist laten zien wat voor robot ik niet ben")
	time.sleep(.4)

	mirai.speech().asay("Kijk maar even mee.")
	time.sleep(.4)

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/ShowTablet_2',)).start()
	#mirai.tablet().open_page('video_1.html')
	#time.sleep(10) # do nothing for 10 seconds
	#mirai.tablet().open_page('index.html') # back to default screen

	#threading.Thread(target=mirai.motion().stand).start()
	#time.sleep(3)

	time.sleep(2)

	mirai.speech().asay("Dit ben ik dus niet")
	time.sleep(.4)

	mirai.speech().asay("Ik ben een robot die geprogrammeerd kan worden om mensen te helpen")
	time.sleep(.4)

	mirai.speech().asay("Hier helpt beivoorbeeld mijn zus Elvie burgers in het gemeentehuis van Leidschendam")
	time.sleep(.4)

	#time.sleep(3)

	time.sleep(.6)

	#threading.Thread(target=mirai.motion().stand).start()

	mirai.speech().asay("Of mijn andere zus fie die in de zorg werkt, om pasjënten met verstandelijke beperkingen, te helpen met oefeningen of eenzaamheid te bestrijden")
	time.sleep(.4)



	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/Excited_1',)).start()
	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Emotions/Positive/Happy_4',)).start()
	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("dat noem ik pas klantenservice!")
	time.sleep(.4)

	print(datetime.datetime.now())
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
	print(datetime.datetime.now())

	mirai.speech().set_speed(40).asay("Komend jaar gaan studenten van de opleiding ha b o - ict met mij aan de slag om uit te zoeken hoe ik mezelf nuttig kan maken").set_speed(DEFAULT_TEXT_SPEED)
	time.sleep(.4)

	# quotes with fingers

	#threading.Thread(target=mirai.tablet().open_page, args=('video_2.html', .1)).start()
	mirai.speech().asay("Onze studenten zijn echte toppers")

	#mirai.tablet().open_page('video_2.html')
	time.sleep(2)  # do nothing for 6 seconds

	threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/No_3',)).start()

	mirai.speech().set_speed(80).set_pitch(1.8).asay("Nee!")
	mirai.speech().set_pitch(0.8).asay("Nee!")
	mirai.speech().set_pitch(0.5).asay("Nee!")
	mirai.speech().set_pitch(0.9).asay("Dit loopt helemaal in de soep!")

	mirai.speech().set_default_pitch()

	time.sleep(.8)
	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("^mode(disabled) ^start(animations/Stand/Gestures/Enthusiastic_5) hahaha. Dit is nou ict humor! ^wait(animations/Stand/Gestures/Enthusiastic_5) ^mode(contextual)")
	threading.Thread(target=mirai.motion().stand).start()
	time.sleep(.8)

	mirai.speech().asay("Even terug naar mijn verhaal")
	time.sleep(.4)
	print(datetime.datetime.now())


def show_3():
	print("show 3")
	print(datetime.datetime.now())

	threading.Thread(target=mirai.motion().head_move_1).start()

	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("ha b o - ict heeft mij gevraagd jullie toe te spreken en te vertellen over wat wij als opleiding doen.")
	time.sleep(.4)

	mirai.speech().asay("^mode(disabled) ^start(animations/Stand/Gestures/Give_3) Wij zijn een community van studenten, docenten, onderzoekers en bedrijven  ^wait(animations/Stand/Gestures/Give_3) ^mode(contextual) die een hart hebben voor ict.")
	threading.Thread(target=mirai.motion().stand).start()
	time.sleep(.4)

	#mirai.speech().asay("Ik ben aan de slag gegaan met data zodat jullie een beeld kunnen krijgen.")

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Waiting/ShowSky_1',)).start()
	#time.sleep(3)  # do nothing for 6 + 2 seconds because of info graphic
	#mirai.motion().stand()
	#time.sleep(2)  # do nothing for 6 + 2 seconds because of info graphic

	mirai.speech().asay("Wij proberen de wereld eerlijker, beter en mooier te maken met ICT.")
	time.sleep(.4)

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/YouKnowWhat_1',)).start()
	mirai.speech().asay("Je kan ons zien als ^mode(disabled) ^start(animations/Stand/Gestures/YouKnowWhat_1) de moeder teresa van de ict ^wait(animations/Stand/Gestures/YouKnowWhat_1) ^mode(contextual)")

	threading.Thread(target=mirai.motion().stand).start()
	time.sleep(1)  # fragment moeder theresa

	mirai.speech().asay("Ok ok, misschien is dat een beetje overdreven.")
	time.sleep(.4)
	mirai.speech().asay("Ik ben hier gewoon nog niet zo goed in.")
	time.sleep(.4)
	mirai.speech().asay("Over ICT praten is ook zó 19 80.")
	time.sleep(.4)

	print(datetime.datetime.now())
	time.sleep(2)  # oude computer + pacman


def show_4():
	print("Show 4")
	print(datetime.datetime.now())

	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("ict moet je beleven. Daarom hebben wij speciaal voor jullie een expositie ingericht.")
	time.sleep(.4)
	mirai.speech().asay("Bezoek de ha b o - ict ekspeeriuns deze week en maak kennis met onze studenten en hun werk.")
	time.sleep(.4)
	mirai.speech().asay("Ben je benieuwd geworden? Neem hier alvast een kijkje.")

	#threading.Thread(target=mirai.motion().run, args=('animations/Stand/Gestures/ShowTablet_3',)).start()
	#mirai.tablet().open_page('video_1.html')
	#time.sleep(8)  # do nothing for 10 seconds
	#mirai.motion().stand()
	#time.sleep(2)
	#mirai.tablet().open_page('index.html')  # back to default screen

	time.sleep(10)

	threading.Thread(target=mirai.motion().run, args=('mirai_moves/dab',)).start()
	mirai.speech().asay("Ik hoop je daar snel te zien!")
	mirai.speech().asay("laters")
	mirai.motion().run('animations/Stand/Gestures/BowShort_1')

	time.sleep(.5)

	mirai.sleep()
	print(datetime.datetime.now())

def show_5():
	print(datetime.datetime.now())
	mirai.speech().asay("Hallo?")
	time.sleep(.8)
	mirai.speech().set_speed(50).asay("Hallo?")
	time.sleep(.4)
	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("Kan iemand mij van het podium tillen?")
	print(datetime.datetime.now())

def preview_show():
	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("^mode(disabled) ^start(animations/Stand/Gestures/Hey_2) Hey Hallo, ik ben miray en ik hoop jou maandag 1 juli te zien bij Outburst! ^wait(animations/Stand/Gestures/Hey_2) ^mode(contextual)")

def on_face_detected_callback(count):
	print("face detected: " + str(count))
	mirai.speech().set_speed(DEFAULT_TEXT_SPEED).asay("^mode(disabled) ^start(animations/Stand/Gestures/Hey_1) Hallo! Welkom bij de ha b o - ict ekspeeriuns. ^wait(animations/Stand/Gestures/Hey_1) ^mode(contextual)")

	mirai.motion().stand(0.7)
	mirai.motion().set_head(0, 0.3)


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

def on_speech_recognized(word, probability):
	if probability < 0.3:
		print("no match, word: " + word + ", prob: " + str(probability))
		# When a word is recognized we stop listening, so we have to enable the recognition again.
		mirai.speech_recognition().start()
		return

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

	# When a word is recognized we stop listening, so we have to enable the recognition again.
	mirai.speech_recognition().start()

def showcase1():
	mirai.motion().stand()
	mirai.speech().disable_auto_movement()
	mirai.speech().set_speed(90)
	mirai.speech().asay("Hallo ik ben miray en ik ben de robot van ha b o ICT. Ik wil je vertellen over Outburst Amsterdam.")
	mirai.speech().asay("Het festival van faculteit digitale media en creatieve industrie van 1 tot 5 juli. Kom naar HvA locatie Kohnstamhuis en bekijk wat alle opleidingen doen.")
	mirai.speech().asay("Ben je benieuwd naar wat ha b o ICT doet? Bezoek de tentoonstelling in de ha b o ICT tent, praat mee over sijber security en Beleef vie ar ervaringen.")
	#threading.Thread(target=mirai.motion().run, args=('mirai_moves/dab', 3)).start()
	mirai.speech().asay("Kijk voor meer informatie op www punt outburst punt amsterdam")

	mirai.speech().asay("Laters")
	mirai.motion().stand()

def showcase2():
	mirai.motion().stand()
	mirai.speech().disable_auto_movement()
	mirai.speech().set_speed(90)
	mirai.speech().asay("Hallo, ik ben miray")
	mirai.speech().asay("en ik wil je welkom heten op outburst Amsterdam!")
	mirai.speech().asay("Ben je nieuwschierig naar wat studenten bij onze opleiding ha b o ICT doen? Bekijk de videos en bezoek onze activiteiten de hele week.")
	mirai.speech().asay("Bekijk ons programma op www punt outburst punt amsterdam")
	#mirai.speech().asay("Wil je meer weten over ha b o ICT? Bezoek dan onze website; www punt hva punt nl slash ha b o streepje ict")
	mirai.speech().asay("Veel plezier!")
	mirai.motion().stand()


def program():
	while not started:
		print("Waiting to start..")
		time.sleep(1)

	mirai.start()
	print("Program started")

	mirai.speech().set_volume(1.0).set_language("Dutch")
	mirai.speech_recognition().set_language("Dutch")

	mirai.face_detection().set_on_face_detected_callback(on_face_detected_callback)
	mirai.face_detection().set_timeout(60000)

	mirai.speech_recognition().set_on_speech_recognized_callback(on_speech_recognized)
	mirai.speech_recognition().set_word_list(['bim', 'technische informatica', 'game development', 'software engineer', 'cyber security'])

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--pip", type=str, default="127.0.0.1", help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
	parser.add_argument("--pport", type=int, default=9559, help="Naoqi port number")

	args = parser.parse_args()


	#mirai = Mirai("145.28.47.180")
	#mirai = Mirai("192.168.50.121")
	mirai = Mirai(args.pip, args.pport)

	mqtt_client = mqtt.Client(client_id="pepper_robot")
	mqtt_client.on_connect = mqtt_connected
	mqtt_client.on_message = mqtt_message
	mqtt_client.username_pw_set("ldr", "xJPriWagGxc68tpwYmDdHWEkg")
	mqtt_client.connect("akoo.nl", 7777, 60)

	threading.Thread(target=program).start()
	mqtt_client.loop_forever()