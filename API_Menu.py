import os

def display_menu():
	print ("\n\n\n\t\t\tMENU:")
	print ("\n\nPress associated numbers to perform the task of your choice.")
	print ("\n0) Exit\n"
		"1) List all containers\n"
		"2) List running containers\n"
                "3) Inspect a specific container\n"
                "4) Dump specific container logs\n"
                "5) List all services\n"
                "6) List all nodes in the swarm\n"
                "7) Create a new container\n"
                "8) Change a container's state\n"
                "9) Delete a specific container\n"
		"10) Delete all containers\n"
                "11) List all images\n"
                "12) Change a specific image's attributes\n"
                "13) Delete a specific image\n"
                "14) Delete all images\n\n")

	choice = input("Choose menu option: ")

	if choice == 0:
		exit()
	elif choice == 1:
		allCons()
		display_menu()
	elif choice == 2:
                runningCons()
		display_menu()
        elif choice == 3:
                inspectCon()
		display_menu()
        elif choice == 4:
                conLogs()
		display_menu()
        elif choice == 5:
                allServices()
		display_menu()
        elif choice == 6:
                allNodes()
		display_menu()
        elif choice == 7:
                createCon()
		display_menu()
        elif choice == 8:
                conState()
		display_menu()
        elif choice == 9:
                deleteCon()
		display_menu()
        elif choice == 10:
                deleteAllCons()
		display_menu()
        elif choice == 11:
                allImages()
		display_menu()
        elif choice == 12:
                changeTag()
		display_menu()
        elif choice == 13:
                deleteImage()
		display_menu()
        elif choice == 14:
                deleteAllImages()
		display_menu()

def allCons():
	os.system("curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers | python -mjson.tool")

def runningCons():
	os.system("curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers?state=running | python -mjson.tool")

def inspectCon():
	id = raw_input("\n\nEnter id of container to inspect: ")
	os.system("curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers/%s | python -mjson.tool" % id)

def conLogs():
	id = raw_input("\n\nEnter id of container's logs to dump: ")
	os.system("curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers/%s/logs | python -mjson.tool" % id)

def allServices():
	os.system("curl -s -X GET -H 'Accept: application/json' http://localhost:8080/services | python -mjson.tool")

def allNodes():
	os.system("curl -s -X GET -H 'Accept: application/json' http://localhost:8080/nodes | python -mjson.tool")

def createCon():
	image = raw_input("\n\nEnter name of existing image to create container: ")
	os.system("curl -X POST -H 'Content-Type: application/json' http://localhost:8080/containers -d '{\"image\": \"%s\"}'" % image)

def conState():
	id = raw_input("\n\nEnter id of container who's state to change: ")
	status = raw_input("\n\nEnter r for running or s for stop: ")
	if status == 'r':
		os.system("curl -X PATCH -H 'Content-Type: application/json' http://localhost:8080/containers/%s -d '{\"state\": \"running\"}'" % id)
	elif status == 's':
		os.system("curl -X PATCH -H 'Content-Type: application/json' http://localhost:8080/containers/%s -d '{\"state\": \"stopped\"}'" % id)
	else:
		print ("\nINVALID INPUT")

def deleteCon():
	id = raw_input("\n\nEnter id of container you wish to delete: ")
	os.system("curl -s -X DELETE -H 'Accept: application/json' http://localhost:8080/containers/%s | python -mjson.tool" % id)

def deleteAllCons():
	os.system("curl -s -X DELETE -H 'Accept: application/json' http://localhost:8080/containers | python -mjson.tool")

def allImages():
	os.system("curl -s -X GET -H 'Accept: application/json' http://localhost:8080/images | python -mjson.tool")

def changeTag():
	id = raw_input("\n\nEnter id of image you wish to update: ")
	name = raw_input("\n\nEnter a new name value for this image: ")
	tag = raw_input("\n\nEnter a new tag value for this image: ")
	os.system("curl -s -X PATCH -H 'Content-Type: application/json' http://localhost:8080/images/%s -d '{\"%s\": \"%s\"}'" % (id, name, tag))

def deleteImage():
	id = raw_input("\n\nEnter id of image you wish to delete: ")
	os.system("curl -s -X DELETE -H 'Accept: application/json' http://localhost:8080/images/%s | python -mjson.tool" % id)

def deleteAllImages():
	os.system("curl -s -X DELETE -H 'Accept: application/json' http://localhost:8080/images | python -mjson.tool")

display_menu()
