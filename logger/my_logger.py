import os
import logging


class MyLogger:
    _logger = None

    def __new__(cls, log_file='my_log.log'):
        if not cls._logger:
            cls._logger = super(MyLogger, cls).__new__(cls)
            cls._logger._initialize_logger(log_file)
        return cls._logger

    def _initialize_logger(self, log_file):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # 获取文件夹路径
        log_folder = os.path.dirname(log_file)

        # 创建文件夹（如果不存在）
        os.makedirs(log_folder, exist_ok=True)

        # 创建文件处理器并设置日志级别
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # 创建控制台处理器并设置日志级别
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # 创建格式化器并将其添加到处理器
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - Line:%(lineno)d - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将处理器添加到日志对象
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def exception(self, message):
        self.logger.exception(message)


def test(my_logger):
    my_logger.info("This is an informational message.")
    my_logger.warning("This is a warning message.")
    my_logger.error("This is an error message.")
    try:
        # Simulate an exception
        result = 1 / 0
    except Exception as e:
        my_logger.exception("An exception occurred: {}".format(e))


# 使用示例
if __name__ == "__main__":
    # 在当前工作目录下创建日志文件夹
    log_file_path = os.path.join(os.getcwd(), "logs", "my_log.log")
    # 创建 MyLogger 实例
    logger = MyLogger(log_file_path)
    test(logger)
