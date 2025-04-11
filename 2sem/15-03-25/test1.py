class Data:
    def init(self, data, ip):
        #Инициализация объекта Data с данными и IP-адресом
        self.data = data #Содержимое данных
        self.ip = ip #IP-адрес назначения

class Server:
    _ip_counter = 0 #Статический счетчик IP-адресов

    def init(self):
        #Увеличиваем счетчик IP-адресов и присваиваем серверу новый IP
        Server._ip_counter += 1
        self.ip = Server._ip_counter #Уникальный IP-адрес сервера
        self.buffer = [] #Буфер для хранения данных

    def send_data(self, data):
        #Отправка данных в роутер
        router.buffer.append(data) #Добавляем данные в буфер роутера

    def get_data(self):
        #Получение данных из буфера сервера
        return_data = self.buffer.copy() #Копируем данные из буфера
        self.buffer.clear() #Очищаем буфер
        return return_data #Возвращаем данные


    def get_ip(self):
        # Получение IP-адреса сервера
        return self.ip


class Router:
    def init(self):
        self.buffer = [] #Буфер для хранения данных, которые нужно отправить
        self.servers = {} #Словарь для хранения связанных серверов по их IP

    def link(self, server):
        #Связывание сервера с роутером
        self.servers[server.get_ip()] = server #Добавляем сервер в словарь по его IP

    def unlink(self, server):
        #Отключение сервера от роутера
        if server.get_ip() in self.servers:
            del self.servers[server.get_ip()] #Удаляем сервер из словаря

    def send_data(self):
        # Отправка данных из буфера роутера к соответствующим серверам
        for data in self.buffer:
            relevant_ip = data.ip #Получаем IP-адрес назначения из данных
            if relevant_ip in self.servers:
                self.servers[relevant_ip].buffer.append(data) #Добавляем данные в буфер соответствующего сервера
        self.buffer.clear() #Очищаем буфер роутера после отправки данных



assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"
assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"
assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"
assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"
router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"