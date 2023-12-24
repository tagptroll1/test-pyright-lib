from requests import Request

class MyList(Request):
    def __init__(self, args):
        super().__init__(args)

    def custom(self):
        print("hello")
