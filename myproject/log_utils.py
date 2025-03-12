import logging
from pathlib import Path


class Colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


class ColoredFormatter(logging.Formatter):
    LOGGER_LEVEL_COLORS = {
        'DEBUG': Colors.BLUE,
        'INFO': Colors.GREEN,
        'WARNING': Colors.YELLOW,
        'ERROR': Colors.RED,
        'CRITICAL': Colors.RED + Colors.BOLD,
    }
    ABSTRACTION_LEVEL_COLORS = {
        'myproject.domain': Colors.CYAN,
        'myproject.application': Colors.GREEN,
        'myproject.presentation': Colors.MAGENTA,
        'myproject.infrastructure': Colors.YELLOW,
        'myproject': Colors.WHITE,
    }
    
    def format(self, record):
        # Save the original
        original_name = record.name
        original_levelname = record.levelname
        
        # Apply colors to the logger name
        for module, color in self.MODULE_COLORS.items():
            if record.name.startswith(module):
                record.name = f"{color}{record.name}{Colors.RESET}"
                break
        
        # Apply colors to the level name
        level_color = self.LEVEL_COLORS.get(record.levelname, '')
        record.levelname = f"{level_color}{record.levelname}{Colors.RESET}"
        
        # Format the message
        result = super().format(record)
        
        # Restore the original values
        record.name = original_name
        record.levelname = original_levelname
        
        return result


def setup_logging():
    # Make sure logs directory exists
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    log_config_path = Path(__file__).parent / "logging.yaml"
    if log_config_path.exists():
        with open(log_config_path, "r") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        raise NotImplementedError(f'File {log_config_path} not exists.')
