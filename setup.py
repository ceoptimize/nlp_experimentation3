
from setuptools import setup, find_packages

setup(
    name='nlp_experimentation3',
    version='0.1.0',  # Initial version
    packages=find_packages(),
    install_requires=['python-dotenv', 'requests', 'nltk', 'spacy', 'openai', 'transformers', 'torch' ],
    dependency_links=['file:///Users/christieentwistle/VsCodeProjects/temp_dir/packageutilities/packageutilities#egg=packageutilities'],
)
