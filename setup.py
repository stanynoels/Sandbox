from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    The function will get the list of requirements
    """
    HYPEN_E_dot = '-e .'
    with open(file_path) as file_obj:
        requirments= file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

    if HYPEN_E_dot in requirments:
        requirments.remove(HYPEN_E_dot)
    
    return requirments


setup(
    name='ML Project',
    version='0.0.1',
    author='Noel Stany',
    author_email='stanynoel4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')                                      
)