class EmptyQueueException(Exception):
    def __init__(self, mensagem="The queue is empty. It´s not possible to remove element."):
        super().__init__(mensagem)