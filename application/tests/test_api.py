from fake_users import random_user

baseURL = "http://127.0.0.1:5000/api/v0.1"
class Test_insere_colaborador:
    def test_insert_one(self, test_client):
        self.response = test_client.post(baseURL + "/colaboradores",
                            data= random_user(),
                            content_type= "application/json")

        assert (self.response.status_code == 201)
class Test_busca_colaborador:
    def test_busca_id(self, test_client):
        self.response= test_client.get(baseURL + "/colaboradores?id=5e24e962bfc56ddd824836e2")
        assert self.response.status_code == 200

    def test_busca_nome(self, test_client):
        self.response= test_client.get(baseURL + "/colaboradores?name=Gustavo da Rocha")
        assert self.response.status_code == 200

class Test_modifica_dados:
    def test_altera_um_colaborador(self, test_client):
        self.response = test_client.patch(baseURL + "/colaboradores?id=5e24ee902ca74171fd0e0d17",
                            data= random_user(),
                            content_type= "application/json")
        assert self.response.status_code == 200