import socket
import threading

# 서버 설정
host = '127.0.0.1'  # 로컬 호스트 (localhost)
port = 55559

# 소켓 생성
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# 연결된 클라이언트 목록
clients = []
nicknames = []

# 브로드캐스트 함수 (모든 클라이언트에게 메시지 전송)
def broadcast(message):
    for client in clients:
        client.send(message)

# 클라이언트 핸들러 함수
def handle_client(client):
    while True:
        try:
            # 메시지를 수신하고 브로드캐스트
            message = client.recv(1024)
            broadcast(message)
        except:
            # 오류 발생 시 연결 종료 및 클라이언트 목록에서 제거
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# 서버 시작 함수
def receive():
    while True:
        # 클라이언트 연결 수락
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # 닉네임 요청 및 저장
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # 알림 브로드캐스트
        print(f'Nickname is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        # 클라이언트 핸들링 쓰레드 시작
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is listening...")
receive()
