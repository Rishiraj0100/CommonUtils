import setuptools


version = "1.0.0a"

try:
  import subprocess
  p = subprocess.Popen(
    ['git', 'rev-list', '--count', 'HEAD'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE
  )
  out, err = p.communicate()
  if out:
    version += out.decode('utf-8').strip()
  p = subprocess.Popen(
    ['git', 'rev-parse', '--short', 'HEAD'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE
  )
  out, err = p.communicate()
  if out:
    version += '+g' + out.decode('utf-8').strip()
except Exception:
  pass

setuptools.setup(
  name="CommonUtils",
  version=version,
  author="Rishiraj0100",
  classifiers=[
    "Programming Language :: Python"
  ]
)
