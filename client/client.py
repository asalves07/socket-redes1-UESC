import socket
import datetime
import sys

params = sys.argv[1:]

HOST = "localhost"
PORT = 9902

TIMEOUT = 1
DEST = (HOST, PORT)

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.settimeout(TIMEOUT)

print('''

  ______           __          ____                 __        _____            __        __      
 /_  __/________ _/ /_  ____ _/ / /_  ____     ____/ /__     / ___/____  _____/ /_____  / /______
  / / / ___/ __ `/ __ \/ __ `/ / __ \/ __ \   / __  / _ \    \__ \/ __ \/ ___/ //_/ _ \/ __/ ___/
 / / / /  / /_/ / /_/ / /_/ / / / / / /_/ /  / /_/ /  __/   ___/ / /_/ / /__/ ,< /  __/ /_(__  ) 
/_/ /_/   \__,_/_.___/\__,_/_/_/ /_/\____/   \__,_/\___/   /____/\____/\___/_/|_|\___/\__/____/  
                                                                                                 


  _                                                   _                                _       _       _           
 / |          _ __   __ _ _ __ __ _    ___ _ ____   _(_) __ _ _ __   _   _ _ __ ___   (_)_ __ | |_ ___(_)_ __ ___  
 | |  _____  | '_ \ / _` | '__/ _` |  / _ \ '_ \ \ / / |/ _` | '__| | | | | '_ ` _ \  | | '_ \| __/ _ \ | '__/ _ \ 
 | | |_____| | |_) | (_| | | | (_| | |  __/ | | \ V /| | (_| | |    | |_| | | | | | | | | | | | ||  __/ | | | (_) |
 |_|         | .__/ \__,_|_|  \__,_|  \___|_| |_|\_/ |_|\__,_|_|     \__,_|_| |_| |_| |_|_| |_|\__\___|_|_|  \___/ 
             |_|                                                                                                   

 ____                                                    _                                      _      _             
 |___ \           _ __   __ _ _ __ __ _    ___ _ ____   _(_) __ _ _ __   _   _ _ __ ___   __ _  | | ___| |_ _ __ __ _ 
   __) |  _____  | '_ \ / _` | '__/ _` |  / _ \ '_ \ \ / / |/ _` | '__| | | | | '_ ` _ \ / _` | | |/ _ \ __| '__/ _` |
  / __/  |_____| | |_) | (_| | | | (_| | |  __/ | | \ V /| | (_| | |    | |_| | | | | | | (_| | | |  __/ |_| | | (_| |
 |_____|         | .__/ \__,_|_|  \__,_|  \___|_| |_|\_/ |_|\__,_|_|     \__,_|_| |_| |_|\__,_| |_|\___|\__|_|  \__,_|
                 |_|                                                                                                  

  _____                                                   _                                          _        _             
 |___ /           _ __   __ _ _ __ __ _    ___ _ ____   _(_) __ _ _ __   _   _ _ __ ___   __ _   ___| |_ _ __(_)_ __   __ _ 
   |_ \   _____  | '_ \ / _` | '__/ _` |  / _ \ '_ \ \ / / |/ _` | '__| | | | | '_ ` _ \ / _` | / __| __| '__| | '_ \ / _` |
  ___) | |_____| | |_) | (_| | | | (_| | |  __/ | | \ V /| | (_| | |    | |_| | | | | | | (_| | \__ \ |_| |  | | | | | (_| |
 |____/          | .__/ \__,_|_|  \__,_|  \___|_| |_|\_/ |_|\__,_|_|     \__,_|_| |_| |_|\__,_| |___/\__|_|  |_|_| |_|\__, |
                 |_|                                                                                                  |___/ 

   ___                                              _      
  / _ \           _ __   __ _ _ __ __ _   ___  __ _(_)_ __ 
 | | | |  _____  | '_ \ / _` | '__/ _` | / __|/ _` | | '__|
 | |_| | |_____| | |_) | (_| | | | (_| | \__ \ (_| | | |   
  \___/          | .__/ \__,_|_|  \__,_| |___/\__,_|_|_|   
                 |_|                                       

''')

def log_error(msg):
  print("\nOcorreu um erro!!!")
  print("Erro: " + msg + "\n")

opt = str(input("Digite a opção desejada: "))


while opt != '0':
    resp = None
    end_time = None

    data = str(input("Digite o dado a ser enviado de acordo com a opção: "))
    msg = opt+ "=" +data

    try:
        start_time = datetime.datetime.now()

        udp_server.sendto(bytes(msg, 'utf-8'), DEST)
        resp = udp_server.recv(1024)

        end_time = datetime.datetime.now()

        decoded_resp = resp.decode("utf-8").split("=")

        if decoded_resp[0] == "error":
            log_error(decoded_resp[1])
        else:
            print("\nA resposta é: " + decoded_resp[1] + "\n")

    except Exception as e:
        end_time = datetime.datetime.now()
        log_error(str(e))
        
    finally:
        rtt = end_time - start_time
        rtt_ms = rtt.microseconds / 1000
        print("Round Trip Time: " + str(rtt_ms) + " ms\n")
    print("==========================//==============================\n\n")
    opt = str(input("Digite a opção desejada: "))
