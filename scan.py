def get_random_ip():
    from random import randint
    return str(randint(0, 255)) + "." + str(randint(0, 255)) + "." + str(randint(0, 255)) + "." + str(randint(0, 255))


def scam(_ports, _ip):
    import socket
    import requests
    print("|IP|", _ip)
    ch = False
    for port in _ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            connect = sock.connect((_ip, port))
            print('|PORT|', port, '|OPEN|')
            r = requests.get('http://' + _ip + '/', headers={'host': 'example.com'})
            print("|STATUS HTTP|", r.status_code)
            ch = True
            connect.close()

        except:
            if not ch:
                print("|PORT|", port, "|CLOSE|")


if __name__ == '__main__':
    import sys

    _type = sys.argv[1]
    try:
        _ports = [int(x) for x in sys.argv[2].split(",")]
        if _type == '-p':
            _ip = sys.argv[3]
        elif _type == '-random' and len(sys.argv) == 3:
            _ip = get_random_ip()
        else:
            _ip = 3 / 0
        scam(_ports, _ip)
    except ValueError:
        print("Format ports error!")
    except:
        print("Parameters error!")
