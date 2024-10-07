from setuptools import setup, find_packages
# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="projecao_cubo",
    version="0.1.0",
    author="Manoela Sola Saragoca",
    author_email="manoelass1@al.insper.edu.br",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saragocams/projecao_cubo.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'projecao_cubo=projecao_cubo.main:main',
        ],
    },
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines()
    ],
)