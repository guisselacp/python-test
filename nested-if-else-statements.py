exit_program = True
manual_override = False
critical_systems_shutdown = False

if not exit_program and not critical_systems_shutdown:
    if manual_override:
        print("Shutting system down manually")
    else:
        print("This program will not exit just yet")
elif exit_program and critical_systems_shutdown is not True:
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")

#Challenge
admin = True
update_required = True

if admin == True:
    if update_required == True:
        print("You are authorized to update")
    else:
        print("No update required")
else:
    print("You need admin privileges to do this")