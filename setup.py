##  If you create a Python library that others can use, setup.py will help you package it and distribute it to PyPI, where others can easily install it using pip install your-package-name
# it basically convert python project into package so that others can use it using only simple pip install command
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements ]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        
setup(

    name="MLproject",
    version='0.0.1',
    author='Arun',
    author_email='erarunkumawat50@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)