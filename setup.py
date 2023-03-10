from setuptools import find_packages,setup
from typing import List

loop = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This funtion will return the list of requirements
    """
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if loop in requirements:
            requirements.remove(loop)




setup(
name="DS-Practice",
version='0.01',
author='Shubham5496',
author_email="shubahmgpt23@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)