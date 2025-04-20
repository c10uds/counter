from setuptools import setup, find_packages

setup(
    name="counter",
    version="0.1.0",
    author="c10uds",
    author_email="c10uds@foxmail.com",
    description="A simple counter implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/c10uds/software-test",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)