from setuptools import setup, find_packages

setup(
    name='Encripted Network',
    version='1.3',
    description='This application using Shannon-Fano algorithm to encoding messages given the'
                ' probabilities for each text',
    author='Reinier Hernández Ávila',
    author_email='rhernandeza@facinf.uho.edu.cu',
    # url='http://www.encriptednetwork.com',
    license='GPL',
    scripts=['main.py'],
    packages=find_packages(),
)
