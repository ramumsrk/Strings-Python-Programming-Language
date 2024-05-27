from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  filemode='+a',
  filename=F"{Path(__file__).parent}/logs/builtin_len_function_demo.log"
)

from typing import Literal

def main() -> Literal[None]:
  sample_input_string: Literal[str] = 'Guido Van Rossum'
  logging.debug(
    f'Length of {sample_input_string} is {len(sample_input_string)}'
  )
  return None

if __name__ == '__main__':
  # Function call
  main()