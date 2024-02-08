from datetime import datetime
import os
import logging


class Pipeline(object):
    """ Class for wrapping pipeline and logging setup """
    def __init__(self, name, etl_main_function, logging_level = logging.INFO):
        """Constructor.

        :param name: pipeline name.
        :param etl_main_function: pipeline main function.
        :param logging_level: Set the root logger level to the specified level.
        """
        self.name = name
        self.etl = etl_main_function
        self.logging_level = logging_level


    def _set_logging(self):
        """ set loggin pipeline configuration """
        today = datetime.now().strftime("%Y-%m-%d")
        log_path = f"{os.getcwd()}/logs"
        log_file = f"{log_path}/{self.name}_{today}.log"

        # Create log folder if not exist
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        # Create an empty log file if not exist
        if not os.path.exists(log_file):
            open(log_file, "a", encoding="utf-8")
        else:
            pass
        # Set logging config
        logging.basicConfig(filename=log_file,
                            encoding="utf-8",
                            level=self.logging_level,
                            filemode="a",
                            format="%(asctime)s %(levelname)s: %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")


    def start(self):
        """ start pipeline """
        print(f"Pipeline '{self.name}' started...")
        self._set_logging()
        try:
            result = self.etl()
            print(f"Pipeline '{self.name}' completed successfully with resul:\n {result}")
            return result
        except Exception as e:
            error_message = f"Error occurred in pipeline '{self.name}': {e}"
            print(error_message)
            logging.error(error_message)
            raise e
