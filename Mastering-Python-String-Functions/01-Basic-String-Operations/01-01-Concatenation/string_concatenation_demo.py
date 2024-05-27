from typing import Literal

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  #datefmt="%Y-%m-%d %H:%M:%S,%s",
  filemode='+a',
  filename=f'{Path(__file__).parent}/logs/string_concatenation_demo.log'
)
def main() -> Literal[None]:
  first_name: Literal[str] = 'Guido '
  middle_name: Literal[str] = 'Van '
  last_name: Literal[str] = 'Rossum'
  fullname: Literal[str] = first_name + middle_name + last_name
  logging.debug(
    f'Concatenating {first_name}, {middle_name}, and {last_name} results in {fullname}'
  )
  return None

if __name__ == '__main__':
  # Function call
  main()