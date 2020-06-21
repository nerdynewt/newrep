from setuptools import setup

setup(name='newrep',
      version='1.0',
      description='Make LaTeX Reports from Markdown',
      url='http://github.com/spandananupam/reportinator',
      author='Spandan Anupam',
      author_email='flyingcircus@example.com',
      license='GPL v3.0',
      packages=['newrep'],
      entry_points={
          "console_scripts": [
              "newrep = newrep.main:main",
              ],
          },
      install_requires=[
          'matplotlib',
          'numpy',
          'ruamel.yaml',
          'doi2bib',
          'pandas',
          'pyyaml',
          'configurator',
          ],
      include_package_data=True,
      zip_safe=False,
)

