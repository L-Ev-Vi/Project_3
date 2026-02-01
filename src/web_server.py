from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse


class WebStore(BaseHTTPRequestHandler):
    """Класс, который отвечает за работу сервиса интернет магазина и обработку входящих запросов от клиентов"""

    __index_page: str = "src/index_page.html"  # Главная страница
    __catalog_page: str = "src/catalog_page.html"  # Страница с каталогом товаров
    __category1_page: str = "src/category1_page.html"  # Страница с товарами которые входят в первую категорию
    __orders_page: str = "src/orders_page.html"  # Страница с заказами
    __contacts_page: str = "src/contacts_page.html"  # Страница с контактами

    def __index(self, path) -> str:
        """Метод для вывода страниц веб приложения в браузере."""
        with open(path, 'r', encoding='utf-8') as index:
            result = index.read()
        return f"""{result}"""

    def do_GET(self) -> None:
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        page_address = query_components.get('page')
        page_content = self.__index(self.__index_page)
        if page_address:
            if page_address[0] == "catalog_page":
                page_content = self.__index(self.__catalog_page)
            elif page_address[0] == "orders_page":
                page_content = self.__index(self.__orders_page)
            elif page_address[0] == "contacts_page":
                page_content = self.__index(self.__contacts_page)
            elif page_address[0] == "category1_page":
                page_content = self.__index(self.__category1_page)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))

    def do_POST(self) -> None:
        """Метод для обработки входящего POST-запроса"""
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()
