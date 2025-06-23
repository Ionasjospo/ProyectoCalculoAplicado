from setuptools import setup, find_packages

setup(
    name='calculo_aplicado',
    version='0.1',
    packages=find_packages(include=["data", "data.*", "src", "src.*"]),
    install_requires=[
        "numpy",
        "sympy",
        "matplotlib"
    ]
)
