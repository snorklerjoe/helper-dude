"""Installs the helper_dude Python package"""

from setuptools import setup


# Metadata:
VERSION: str = "0.0.1"
"""Version string"""

AUTHORS: str = "Joseph R. Freeston"
"""A comma-separated list of contributors"""

GITHUB_URL: str = "https://github.com/snorklerjoe/helper-dude"
"""A URL to the source code and info on GitHub"""

DESCRIPTION = (
      'My personal ai assistant based on langchain,'
      'gpt4all, and other open source frameworks'
)

# Setup:
setup(name='helper_dude',
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHORS,
      url=GITHUB_URL,
      packages=["helper_dude"],
      install_requires=[
            'pygpt4all>=1.0.1',
            'pyllamacpp>=1.0.6',
            'langchain>=0.0.151',
            'colorama>=0.4.6',
            'pexpect>=4.8.0'
      ]
    )
