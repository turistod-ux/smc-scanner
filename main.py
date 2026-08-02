import logging
from config import LOG_DIR, PROJECT_NAME, VERSION, AUTO_TRADING_ENABLED

LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "smcx.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("smcx")

def main() -> None:
    logger.info("%s %s запускается", PROJECT_NAME, VERSION)
    logger.info("Автоторговля: %s", "ВКЛ" if AUTO_TRADING_ENABLED else "ВЫКЛ")
    logger.info("Каркас проекта создан успешно")

if __name__ == "__main__":
    main()
