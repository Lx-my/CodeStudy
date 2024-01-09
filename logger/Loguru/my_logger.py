import sys
from loguru import logger


class PolarisLogger:
    def __init__(self, folder="./log/", prefix="polaris-", rotation="10 MB", retention="30 days",
                 encoding="utf-8", backtrace=True, diagnose=True):
        self.folder = folder
        self.prefix = prefix
        self.rotation = rotation
        self.retention = retention
        self.encoding = encoding
        self.backtrace = backtrace
        self.diagnose = diagnose

        self.format = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> ' \
                      '| <magenta>{process}</magenta>:<yellow>{thread}</yellow> ' \
                      '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<yellow>{line}</yellow> - <level>{message}</level>'

        # 定义日志级别和对应的文件名
        self.log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

        # 设置公共参数
        self.common_params = dict(
            backtrace=self.backtrace, diagnose=self.diagnose,
            format=self.format, colorize=False,
            rotation=self.rotation, retention=self.retention, encoding=self.encoding
        )

        # 配置各级别的日志文件
        for level in self.log_levels:
            file_path = f"{self.folder}{self.prefix}{level.lower()}.log"
            logger.add(file_path, level=level,
                       filter=lambda record: record["level"].no >= logger.level(level).no,
                       **self.common_params)

        # 配置控制台输出，级别为CRITICAL
        logger.add(sys.stderr, level="CRITICAL", colorize=True,
                   filter=lambda record: record["level"].no >= logger.level("CRITICAL").no,
                   **self.common_params)


# 示例用法
if __name__ == "__main__":
    # 创建PolarisLogger实例
    polaris_logger = PolarisLogger()

    # 使用logger记录日志
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
