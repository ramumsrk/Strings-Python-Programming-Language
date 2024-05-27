from typing import Literal

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  filemode='+a',
  filename=F'{Path(__file__).parent}/logs/string_formatting_with_format_demo'
           F'.log'
)

# User-defined function
def main() -> Literal[None]:
  sample_item: Literal[str] = 'book'
  sample_price: Literal[float] = 20.5
  sample_description: Literal[str] = "Cost of {} is {:.2f}".format(
    sample_item, sample_price)
  logging.debug(F'{sample_description}')
  return None

if __name__ == '__main__':
  # Function call
  main()