import os
import json

from typing import Optional, Callable


def load(
  file: Optional[str] = ".env.json",
  loader_func: Optional[Callable] = json.load
):
  with open(file, "r") as f:
    os.environ.update(
      loader_func(f)
    )

reload = load
