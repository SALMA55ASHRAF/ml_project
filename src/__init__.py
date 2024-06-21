from setuptools import find_packages,setup
hyphen='-e .'
def requirement(file_path):
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements
setup(
    name='ml_project',
    version='0.0.1',
    author='salma',
    author_email='aboelseuioofsefoo@gmail.com',
    packages=find_packages(),
    install_requires=requirement('requirement.txt')
)