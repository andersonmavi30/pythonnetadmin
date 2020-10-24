import getpass
import telnetlib

HOST = "172.20.30.1"
user = input("Usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"configure terminal\n")
tn.write(b"hostname SWCACCESO1\n")
tn.write(b"username anderson.martinez privilege 15 secret cisco\n")
tn.write(b"no ip domain-lookup\n")
tn.write(b"vlan 10\n")
tn.write(b"name TECNOLOGIA\n")
tn.write(b"exit\n")
tn.write(b"interface range GigabitEthernet 0/1-2\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 10\n")
tn.write(b"description TECNOLOGIA\n")
tn.write(b"exit\n")
tn.write(b"line console 0\n")
tn.write(b"history size 256\n")
tn.write(b"login local\n")
tn.write(b"exec-timeout 3\n")
tn.write(b"session-timeout 3\n")
tn.write(b"session-limit 2\n")
tn.write(b"logging synchronous\n")
tn.write(b"exit\n")
tn.write(b"shell processing full\n")
tn.write(b"do write memory\n")

print(tn.read_all().decode('ascii'))
