from .envloader import (
  load as load_env,
  reload as reload_env
)


def _(**kwargs) -> None:
  """Main Function"""
  load_env(**kwargs.get("load_env",{})
