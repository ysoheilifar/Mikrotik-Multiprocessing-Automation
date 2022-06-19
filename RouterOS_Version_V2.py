import concurrent.futures
import time
import colorama
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from colorama import Fore, Back, Style

with open('devices_list.txt') as f:
	devices_list = f.read().splitlines()

with open('commands_all_devices.txt') as f:
	commands_list = f.read().splitlines()

colorama.init(autoreset=True)
open('log.csv', 'w').close()
log = open('log.csv','a')

def f(device):
	device_Info = device.split(",")
	device_Name = device_Info[0]
	ip_address_of_device = device_Info[1]
	pass_Of_Device = device_Info[2]
	print('\r\nConnecting to ' + ip_address_of_device)
	ios_device = {
		'device_type': 'mikrotik_routeros',
		'ip': ip_address_of_device,
		'username': 'admin',
	    'password': pass_Of_Device,
		 }  
  	
	try:
		net_connect = ConnectHandler(**ios_device)
		output = net_connect.send_config_set(commands_list,cmd_verify=False)
		output = output.splitlines()
		
		for i in output:
			if 'version' in i:
				j = i.replace("                  ","")
				log.write(ip_address_of_device + ',' + device_Name + ',' + j+'\n')
											
	except (AuthenticationException):
		log.write(ip_address_of_device + ',' + device_Name +',Authentication failure: ' + '\n')
		
		
	except (NetMikoTimeoutException):
		log.write(ip_address_of_device + ',' + device_Name +',Timeout to device: ' + '\n')
		
		
	except (EOFError):
		log.write(ip_address_of_device + ',' + device_Name +',End of file while attempting device ' + '\n')
		
		
	except (SSHException):
		log.write(ip_address_of_device + ',' + device_Name +',SSH Issue: Are you sure SSH is enable??? ' + '\n')
		
		
	except Exception as unknown_error:
		log.write(ip_address_of_device + ',' + device_Name +',Some other error: ' + unknown_error + '\n')

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(f, devices_list)	

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(Fore.GREEN + f'\r\nFinished in {round(end-start, 2)} second(s)')