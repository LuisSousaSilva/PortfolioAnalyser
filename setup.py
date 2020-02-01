from setuptools import setup

setup(
    name='PortfolioAnalyser',
    url='https://github.com/LuisSousaSilva/PortfolioAnalyser',
    author='Luis Silva',
    author_email='luis_paulo_silva@hotmail.com',
    packages=['PortfolioAnalyser'],
    install_requires=['numpy', "pandas", 'datetime'],
    version='0.1',
    license='MIT',
    description='Python library for financial portfolio management',
)