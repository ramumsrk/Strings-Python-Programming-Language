from typing import Literal

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  filemode='+a',
  filename=F'{Path(__file__).parent}/logs/string_repetition_demo.log'
)

# User-defined function
def main() -> Literal[None]:
  sample_input_string: Literal[str] = 'Guido Van Rossum'
  repetition_count: Literal[int] = 3
  logging.debug(
    F'Repeating {sample_input_string} for {repetition_count} results in {sample_input_string * repetition_count}'
  )
  return None

if __name__ == '__main__':
  # Function call
  main()