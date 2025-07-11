from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Gen AI RAG Medical Chatbot",
    version="0.1",
    author="rajeshr",
    packages=find_packages(),
    install_requires = requirements,
)