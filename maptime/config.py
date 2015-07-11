import os
import sys
import tempfile

from configobj import ConfigObj


basedir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
global _config
_config = None

def _load_config(filename=None):
  global _config
  _config = {}
  if filename is None:
    filename = 'test.cfg'
  cfg_file = os.path.join(basedir, 'config', filename)
  if os.path.exists(cfg_file):
      _config = ConfigObj(cfg_file, unrepr=True).dict()['global']


def get(key, default=None):
  global _config
  if _config == None:
    _load_config()

  return _config.get(key, default)

def set(key, value):
  update({key : value})

def log_dir():
  path = get('vungle.log.dir', './log')
  return os.path.join(basedir, path)
