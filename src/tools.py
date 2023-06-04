from time import localtime, strftime

def get_actual_time() -> str:
    return strftime("%Y.%m.%d %H:%M:%S", localtime())