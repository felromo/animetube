import ez_setup

ez_setup.use_setuptools()

from setuptools import setup, find_packages
setup (
  name = "AnimeTube",
  version = "0.1",
  packages = find_packages(),

install_requires = ['BeautifulSoup4', 'colorama'],

author = "TyrantWarship",
author_email = "raymanv3@gmail.com",
description = "Simple anime streaming api",

)
