from itertools import count
from pathlib import Path
import logging


def main():
    # increment number of run_count.txt
    current = Path(__file__)
    counter = current.parent / 'run_count.txt'
    assert counter.exists()

    number = int(counter.read_text())
    logger.info("Run number %d", number)
    number += 1
    logger.info("incrementing run count to %d", number)
    counter.write_text(str(number))
    logger.info("write to file")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    main()
