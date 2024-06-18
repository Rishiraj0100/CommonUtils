import os
import json

from typing import (
  List,
  Callable,
  Optional
)


__all__ = (
  "load",
  "reload",
  "unload"
)

def load(
  file: Optional[str] = ".env.json",
  loader_func: Optional[Callable] = json.load,
  scopes: Optional[List[Dict]] = [],
  other_scopes: Optional[List[Dict]] = []
) -> None:
  """Load environment variables from a file"""
  scopes = scopes or [os.environ]
  scopes.extend(other_scopes)
  with open(file, "r") as f:
    data = loader_func(f)
  for scope in scopes:
    scope.update(
      data
    )

reload = load

def unload(
  file: Optional[str] = ".env.json",
  loader_func: Optional[Callable] = json.load,
  keep_changes: Optional[bool] = False,
  scopes: Optional[List[Dict]] = [],
  other_scopes: Optional[List[Dict]] = []
) -> None:
  """Unload environment variables from a file"""
  scopes = scopes or [os.environ]
  scopes.extend(other_scopes)
  with open(file, "r") as f:
    data = loader_func(f)

  MISSING = object()
  for scope in scopes:
    for key, value in data.items():
      env_val = scope.get(key, MISSING)
    
      if env_val is MISSING:
        continue
      
      if keep_changes:
        if env_val != value:
          continue
    
      del scope[key]

  
