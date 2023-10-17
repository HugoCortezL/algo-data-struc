class EmptyStackException(Exception):
    def __init__(self, mensagem="The stack is empty."):
        super().__init__(mensagem)