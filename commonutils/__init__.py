from .envloader import load as load_env


def _(**kwargs):
  load_env(**kwargs.get("load_env",{})
