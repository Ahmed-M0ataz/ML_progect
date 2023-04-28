import sys
import logging
# handle error if the exption rised call this func


def error_message_detail(error, error_detail: sys):
    # frist and secound index not importa
    # third information about
    # if the exption is rised get
    # which file that make this error and which line to

    _, _, exc_tb = error_detail.exc_info()

    # file name from exc
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}] "

    return error_message


class CustomExption(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
