from typing import Literal

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  filemode='+a',
  filename=F'{Path(__file__).parent}/logs/builtin_lower_and_upper_functions_demo.log'
)

# User-defined function
def main() -> Literal[None]:
  sample_input_string: Literal[str] = 'Guido Van Rossum'
  logging.debug(
    F"'{sample_input_string}' converted to uppercase results in '"
    F"{sample_input_string.upper()}'"
  )
  logging.debug(
    f"'{sample_input_string}' converted to lowercase results in '"
    f"{sample_input_string.upper().lower()}'"
  )
  return None

if __name__ == '__main__':
  # Function call
  main()