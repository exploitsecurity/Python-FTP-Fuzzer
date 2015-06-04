import socket

def main():
    ip = '192.168.207.133'
    port = 21
    username = 'ftp'
    password = 'ftp'

    buffer = ["A"]
    counter = 20
    commands = ["USER", "PASS", "ABOR", "ACCT", "ADAT", "ALLO", "APPE", "AUTH", "CCC", "CDUP", "CONF", "CWD", "DELE", "ENC", "EPRT", "EPSV", "FEAT", "HELP", "LANG", "LIST", "LPRT", "LPSV", "MDTM", "MIC", "MKD", "MLSD", "MLST", "MODE", "NLST", "NOOP", "OPTS", "PASV", "PBSZ", "PORT", "PROT", "PWD", "REIN", "REST", "RETR", "RMD", "RNFR", "RNTO", "SITE", "SIZE", "SMNT", "STAT", "STOR", "STOU", "STRU", "SYST", "TYPE", "XCUP", "XMKD", "XPWD", "XRCP", "XRMD", "XRSQ", "XSEM", "XSEN"]

    while len(buffer) <= 30:
        buffer.append("A" * counter)
        counter = counter + 100
        
    for command in commands:
        for string in buffer:
            print "Fuzzing " + command + " with lenght: " + str(len(string))

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect = sock.connect((ip, port))
            sock.recv(1024)
            if command == 'PASS':
                sock.send('USER ' + username + '\r\n')
                sock.recv(1024)
            elif command is not 'USER' and command is not 'PASS':
                sock.send('USER ' + username + '\r\n')
                sock.recv(1024)
                sock.send('PASS ' + password + '\r\n')
                sock.recv(1024)
            sock.send(command + ' ' + string + '\r\n')
            sock.recv(1024)
            sock.send('QUIT\r\n')
            sock.close()
            
if __name__ == '__main__':
    main()