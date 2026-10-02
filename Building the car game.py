started = False
while True :
    command =input ("> ").lower()
    if command =="start":
        if started :
            print('car is already started')
        else:
            started= True
            print(" car is starting") 

    elif command =="stop":
        if not started:
            print("Car is already stopped")
        else:
            started=False
            print("your car is stopping")

    elif command=="help":
        print("""
   start- to start car
   stop-to stop car
   quit-to quit""" )
        
    elif command=="quit":
        break
    else:
        print(" i can not understand")
        





