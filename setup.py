import setuptools
setuptools.setup(
  name = 'web-sws-py-bootstrap',
  packages = ['web_sws_py_bootstrap'],
  version = '0.1',
  license='MIT',
  description = 'Here we store all the common functionality that we use across our services.',
  author = 'Andrii Osmak',
  author_email = 'andrii.osmak@serato.com',
  url = 'https://github.com/serato/web-sws-py-bootstrap',
  python_requires='>=3.6',
  install_requires=[
    'pytest'
  ]
)
