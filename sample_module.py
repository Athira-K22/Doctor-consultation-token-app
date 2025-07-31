from logger_setup import logger_cvgk

def do_something():
    logger_cvgk.info("This is an info log from sample_module.")
    logger_cvgk.info("Another log with more details.")

if __name__ == "__main__":
    do_something()
