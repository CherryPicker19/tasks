class Graph:
    def __init__(self, data: list, is_show=True):
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data: list):
        self.data = data.copy()

    def show_table(self):
        if self.is_show == False:
            print("Отоброжение данных закрыто")
            return None
        print(str(self.data).replace(', ', ' ')[1:-1])

    def show_graph(self):
        if self.is_show == False:
            print("Отоброжение данных закрыто")
            return None
        print("Графическое отображение данных:", end=' ')
        print(str(self.data).replace(', ', ' ')[1:-1])

    def show_bar(self):
        if self.is_show == False:
            print("Отоброжение данных закрыто")
            return None
        print("Столбчатая диограмма:", end=' ')
        print(str(self.data).replace(', ', ' ')[1:-1])

    def set_show(self, fl_show):
        self.is_show = fl_show

data_graph = list(map(int, input("Введите числа: ").split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
