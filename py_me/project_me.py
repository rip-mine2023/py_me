import os

class project_me:
  def criar_projeto():
    nome = input("qual é o nome do prejeto?: ")
    if not " " in nome:
      pasta_base = os.path.dirname(os.path.abspath(__file__))
      project = os.path.join(pasta_base, f"{nome}_project")
      os.makedirs(project, exist_ok= True)
      pasta_principal = os.path.join(project, f"{nome}")
      os.makedirs(pasta_principal,exist_ok= True)
      __initpy__ = os.path.join(pasta_principal, "__init__.py")
      with open(__initpy__, "w") as __init__:
        inscritura___init__ = f"""from .modulo1 import modulo1 #coloque o nome do modulo"""
        __init__.write(inscritura___init__)
      modulo = os.path.join(pasta_principal, "modulo1.py")
      with open(modulo, "w", encoding="utf-8") as modulo1:
        inscritura_modulo1 = """class modulo1:
        
  def olá_mundo():
    print("olá_mundo")"""
        modulo1.write(inscritura_modulo1)
      licensa = os.path.join(project, "LICENSE.txt")
      with open (licensa, "w", encoding="utf-8") as License:
        inscritura_License = """coloque sua licensa aqui"""
        License.write(inscritura_License)
      toml = os.path.join(project, "pyproject.toml")
      with open (toml, "w", encoding="utf-8") as pyproject_toml:
        inscritura_toml = """[project]
name = {nome}
version = "1.1.1"
description = "coloque descrição"
authors = [{ name = "nome do altor", email = "emaildoaltor@gmail.com" }]
maintainers = [{ name = "", email = "" }]
readme = "README.md"
license = {file = "LICENSE"}
requires-python = ">=verção do python minima para o seu projeto" 
  dependencies = [
      "colocar dependentes"
  ]
keywords = ["coloque", "uma", "tag"]
classifiers = [
  "Programming Language :: Python :: 3", #definido por padrão, mas você pode trocar
  "Topic :: Multimedia :: Sound/Audio",
  "Topic :: Software Development :: Libraries",
  "Intended Audience :: Developers",
  "Operating System :: OS Independent"
  ]

[project.urls]
"Homepage" = "https://github.com/" #coloque aqui o repositorio onde o projeto vai estar
"Source" = "https://github.com/"
"Issues" = "https://github.com/"


[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
        """
        pyproject_toml.write(inscritura_toml)
        leia_me = os.path.join(project, "README.MD")
        with open (leia_me, "w", encoding="utf-8") as README_md:
          inscritura_README_md = f"""# {nome}
## verção
**1.1.1**
## modulo1
### funções
- olá_mundo()
### exemplo
```python
from {nome} import modulo1

  modulo1.olá_mundo()
```
          """
          README_md.write(inscritura_README_md)
        setdown = os.path.join(project, "setup.py")
        with open(setdown, "w", encoding="utf-8") as setup:
          inscritura_setup = f"""from setuptools import setup, find_packages

setup(
name='{nome}',
version='1.1.1',
packages=find_packages(),
description='adicione uma descrição',
author='seu nome',
author_email='seuemail@gmail.com',
)
          """
          setup.write(inscritura_setup)
        

    else:
      raise ValueError(f"{nome} contem um espaço em branco, poderia por favor remove-lo ou substituilo por '_' ")