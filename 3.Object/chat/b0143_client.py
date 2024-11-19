import socket
import threading

# 클라이언트 설정
host = '127.0.0.1'  # 서버 주소 (localhost)
port = 55559

# 소켓 생성
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# 메시지 수신 함수
def receive():
    while True:
        try:
            # 서버로부터 메시지 수신
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # 오류 발생 시 연결 종료
            print("An error occurred!")
            client.close()
            break

# 메시지 전송 함수
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# 닉네임 설정
nickname = input("Choose your nickname: ")

# 수신 및 전송 쓰레드 시작
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
