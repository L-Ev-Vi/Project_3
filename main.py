from http.server import HTTPServer

from src.web_server import WebStore

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети

if __name__ == "__main__":

    web_server = HTTPServer((hostName, serverPort), WebStore)
    print("Сервер запущен http://%s:%s" % (hostName, serverPort))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Сервер остановлен.")
