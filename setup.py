from setuptools import find_packages, setup
from typing import List

HYPHEN_E = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    
    return requirements


setup(
    name='MLproj',
    version='0.0.1',
    author="DevG06",
    author_email="devarshi.dg56@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)