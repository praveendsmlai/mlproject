from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    '''
    This function return list of reqyirements
    '''

    Hypen_e_dot = "-e ."

    requirements=[]
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements



setup(
    name = "Praveen",
    version="0.0.1",
    author="praveen",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)