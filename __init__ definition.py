class User:
    """
     a função initialize permite que sejam atribuidos valores (atributos) iniciais no momento em que um objeto for
     criado.
    """
    def __init__(self, user_id, username):  # self indica o próprio objeto inicializado
        # self = define_user_1 (object) / define_user_2 (object)
        self.user_id = user_id
        self.username = username
        self.followers = 0  # default (valor padrão)

    def shows_user_data(self):
        print(f'ID: {self.id}\nUSERNAME: {self.username}')


# __init__() é útil quando é necessário criar vários objetos que possuem os mesmos atributos (menos reduntante), como por exemplo:
define_user_1 = User(100, 'Chaeyoung')
define_user_1.shows_user_data()
define_user_2 = User(101, 'Mina')
define_user_2.shows_user_data()
