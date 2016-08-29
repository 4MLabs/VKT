##############################
###    VNC KILLER TOOL     ###
###    By: Metalerk        ###
##############################

import subprocess as sp

cmd_output = sp.check_output(['tasklist'])
tasklist = cmd_output.split('\n')
winvnc_process = ''
winvnc_is_active = False

print("\n\t\t ..::: VNC KILLER TOOL :::..")
print("\n\t\t     By: Metalerk Labs")
print("\n")

for line in tasklist:

    if "winvnc.exe" in line:
	
	    winvnc_process = line
	    winvnc_is_active = True

if not winvnc_is_active:

    print("[-] VNC not running !!\n")

else:

    print("[+] VNC instance detected !\n")
	
    name_img, pid, name_session, num, mem_usage_num, kb = winvnc_process.split()
    
    print("\n[+] Name: {}".format(name_img))
    print("\n[+] PID: {}".format(pid))
    print("\n[+] Memory Usage: {} {}".format(mem_usage_num, kb))
	
    terminate = sp.check_output(['taskkill', '/PID', pid, '/f'])
	
    if "Correct" in terminate:
	
	    print("\n\n[+] VNC killed succesfully.")
            raw_input("Press a key to continue...")