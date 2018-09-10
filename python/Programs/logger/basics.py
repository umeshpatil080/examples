import logging


def write_to_stderr_and_file():
    fileName = "sam.log"
    with open(fileName, "a") as fileHandler:
        fileStream = logging.StreamHandler(stream=fileHandler)
        logging.basicConfig(level = "INFO")
        log = logging.getLogger(__name__)
        log.addHandler(fileStream)
        log.info("Here goes log message")

def list_log_handlers():
    pass

def main():
    write_to_stderr_and_file()

if __name__ == '__main__':
    main()
