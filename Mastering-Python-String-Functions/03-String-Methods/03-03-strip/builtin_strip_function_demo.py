from typing import Literal

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  filemode='+a',
  filename=F"{Path(__file__).parent}/logs/builtin_strip_function_demo.log"
)

# User-defined function
def main() -> Literal[None]:
  sample_input_string: str = '   prefix space and suffix space  '
  logging.debug(
    f"'{sample_input_string}' after removing space results in '{sample_input_string.strip()}'"
  )
  return None

if __name__ == '__main__':
  # Function call
  main()