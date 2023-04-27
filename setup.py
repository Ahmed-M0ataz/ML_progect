from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
        this function return list of requirements (libraries)
    """
    # -e . in requirments.txt that link setup.py in requirments.txt
    dot_e = '-e .'
    requirements = []

    with open(file_path) as req:
        requirements = req.readlines()
        requirements = [req.replace('\n', '')for req in requirements]
        if dot_e in requirements:
            requirements.remove(dot_e)


setup(

    name='mlproject',
    version='0.0.1',
    author='Mo3taz',
    author_email='ahmedmoataz192@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
