from mirai import Mirai
import time

mirai = Mirai("145.28.47.180")

mirai.motion().set_head(-0.5, -0.5)
time.sleep(3)
mirai.motion().set_head(0.5, 0.5)

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