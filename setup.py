import setuptools
import calendar
import time

with open("README.md", "r") as fh:
    long_description = fh.read()

ts = calendar.timegm(time.gmtime())

setuptools.setup(
    name="sosi_configuration_manager",
    version="0.0." + str(ts),
    author="Leônidas do Nascimento",
    author_email="leonidas.nascimento@live.com",
    description="Configuration management tool for SoSI project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonidasnascimento/sosi_configuration_manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)