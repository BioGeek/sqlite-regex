from setuptools import setup, Extension
import os
import platform

VERSION = "0.2.0"

system = platform.system()
machine = platform.machine()

print(system, machine)

if system == 'Darwin':
  if machine not in ['x86_64', 'arm64']:
    raise Exception("unsupported platform")  
elif system == 'Linux':
  if machine not in ['x86_64']:
    raise Exception("unsupported platform")
elif system == 'Windows':
  # TODO only 64 bit I think
  pass
else: 
  raise Exception("unsupported platform")

setup(
    name="sqlite-regex",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    author="Alex Garcia",
    url="https://github.com/asg017/sqlite-regex",
    project_urls={
        "Issues": "https://github.com/asg017/sqlite-regex/issues",
        "CI": "https://github.com/asg017/sqlite-regex/actions",
        "Changelog": "https://github.com/asg017/sqlite-regex/releases",
    },
    license="MIT License, Apache License, Version 2.0",
    version=VERSION,
    packages=["sqlite_regex"],
    package_data={"sqlite_regex": ['*.so', '*.dylib', '*.dll']},
    install_requires=[],
    # Adding an Extension makes `pip wheel` believe that this isn't a 
    # pure-python package. The noop.c was added since the windows build
    # didn't seem to respect optional=True
    ext_modules=[Extension("noop", ["noop.c"], optional=True)],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)