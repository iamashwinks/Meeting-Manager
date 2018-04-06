from meeting import MeetingManager

dict = MeetingManager()

adminpassword = "admin"
print(" -"*20, "\n Time scheduling for meeting manager \n","- "*20)
while True:
    print("\n")
    option=int(input("Enter the option \n 1. Schedule a meeting with the manager?\n 2. Cancel the Meeting \n 3. View all Scheduled Meetings \n"))
    if option == 1:
        dict.name=input("\nEnter your name: ")
        while True:
            index=int(input("1. Check Time Slots \n2. Schedule a Meeting \n"))
            if index == 1:
                print("The available time slots for meeting are: \n")
                dict.time_view()
            elif index == 2:
                dict.schedule()
                break
            else:
                break
    elif option == 2:
        Name=input("\nEnter your name:")
        search=input("\nEnter the time slot previously taken:")
        for timeslot in dict.allocated.keys():
            if timeslot == search:
                dict.allocated.pop(timeslot)
                dict.available[timeslot]="Available"
                print("\nYour meeting has been canceled.\nYou can Reschedule now.")
                break
    elif option == 3:
        print("Admin View")
        password = input("Enter Password: ")
        if password == adminpassword:
            print("----Scheduled Meetings----")
            dict.occupied()
    else:
        break
