# Car Game
cmd = ""
started = False
while True:
    cmd = input("> ").lower()
    if cmd == "help":
        print("""
              start - to start the car
              stop - to stop the car
              quit - to exit
            """)
    elif cmd == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif cmd == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif cmd == "quit":
        break
    else:
        print("I don't understand that...'Help' For more Info")
# Compare this snippet from minigames/cargame.py:
# # Car Game
# cmd = ""
# started = False
# while True:
