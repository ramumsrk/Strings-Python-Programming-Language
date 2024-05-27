from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  filemode='+a',
  filename=F'{Path(__file__).parent}/logs/f-String_demo.log'
)

from typing import Literal

# User-defined function
def main() -> Literal[None]:
  sample_name: Literal[str] = 'Alice'
  sample_age: Literal[int] = 30
  sample_message: Literal[str] = f'My name is {sample_name} and I am {sample_age} years old'
  logging.debug(f'{sample_message}')
  return None

if __name__ == '__main__':
  # Function call
  main()