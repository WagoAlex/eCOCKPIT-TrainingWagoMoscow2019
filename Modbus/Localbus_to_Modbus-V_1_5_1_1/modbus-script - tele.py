# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.
# cd C:\Program Files (x86)\WAGO Software\e!COCKPIT
# e!COCKPIT.exe --runscript:C:\<directory>\<to>\<script>.py

import os
PFC_IP ="192.168.1.212"

scriptDir = os.path.dirname(os.path.realpath(__file__))
# get the path of the archive file
archiveFile = os.path.join(scriptDir, "Localbus_to_Modbus-V_1_5_1_1_Tele.eca")
print(archiveFile)
# open archive file
project = e_projects.open_archive(archiveFile)
# set the credentials for the device
online.set_default_credentials("admin", "wago")


#e!COCKPIT: Connect the device(s) - Codesys and WAGO connection
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
device0 = project.get_device("PFC200_G2_2ETH_RS")
device0.ip_address= PFC_IP

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
device0.connect()

app = project.find("Application", True) # get the first PFC
# Get the online application
onlineapp = online.create_online_application(app[0])
onlineapp.login(0, True)
print("Project is in state: {0}".format(onlineapp.application_state))

if not onlineapp.application_state == ApplicationState.run:
    onlineapp.start()
print("Project is in state: {0}".format(onlineapp.application_state))    
onlineapp.create_boot_application()
print("Bootproject loaded...")
print("Online application is logged in: {0}".format(onlineapp.is_logged_in))

#e!COCKPIT: Disconnect the device(s) - Codesys and WAGO connection
device0.disconnect()
print("Disconnected")