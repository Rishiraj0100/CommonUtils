import os
import json

from typing import Optional, Callable


__all__ = (
  "load",
  "reload",
  "unload"
)

def load(
  file: Optional[str] = ".env.json",
  loader_func: Optional[Callable] = json.load
) -> None:
  """Load environment variables from a file"""
  with open(file, "r") as f:
    os.environ.update(
      loader_func(f)
    )

reload = load

def unload(
  file: Optional[str] = ".env.json",
  loader_func: Optional[Callable] = json.load,
  keep_changes: Optional[bool] = False
) -> None:
  """Unload environment variables from a file"""
  with open(file, "r") as f:
    data = loader_func(f)

  MISSING = object()
  for key, value in data.items():
    env_val = os.environ.get(key, MISSING)
    
    if env_val is MISSING:
      continue
      
    if keep_changes:
      if env_val != value:
        continue
    
    del os.environ[key]

  
