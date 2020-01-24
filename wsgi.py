from application import create_app
from pprint import pprint



if __name__ == "__main__":
    api = create_app(__name__, "dev")
    api.run(debug=True, use_reloader= True)

