from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse


class WebStore(BaseHTTPRequestHandler):
    """Класс, который отвечает за работу сервиса интернет магазина и обработку входящих запросов от клиентов"""

    def __index_page(self) -> None:
        """Метод выводит главную страницу веб приложения"""
        pass

    def __catalog_page(self) -> None:
        """Метод выводит страницу с каталогом товаров"""
        pass

    def __category1_page(self) -> None:
        """Метод выводит страницу с товаров которые входят в первую категорию"""
        pass

    def __orders_page(self) -> None:
        """Метод выводит страницу с заказами"""
        pass

    def __contacts_page(self) -> None:
        """Метод выводит страницу с контактами"""
        pass

    def _do_GET(self) -> None:
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        page_address = query_components.get('page')
        page_content = self.__index_page()
        if page_address:
            page_content = self.__get_blog_article(page_address[0])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))

    def _do_POST(self) -> None:
        """Метод для обработки входящего POST-запроса"""
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()
