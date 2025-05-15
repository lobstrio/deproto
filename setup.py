"""Setup script for deproto."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="deproto",
    version="0.2.5",
    author="lobstr.io",
    author_email="contact@lobstr.io",
    description="A Python library for decoding Google Maps protocol buffer (protobuf) responses into readable data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lobstrio/deproto",
    packages=find_packages(),
    maintainer="lobstr.io",
    maintainer_email="contact@lobstr.io",
    project_urls={
        "Website": "https://lobstr.io",
        "Source": "https://github.com/lobstrio/deproto",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    extras_require={
        "dev": [
            "pytest>=8.3.4",
            "pytest-cov>=6.0.0",
            "flake8>=7.1.1",
            "black>=24.10.0",
            "isort>=5.13.2",
            "pre-commit>=4.0.1",
        ],
    },
)
