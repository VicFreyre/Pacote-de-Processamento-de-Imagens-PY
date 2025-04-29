from setuptools import setup, find_packages

setup(
    name='meu_pacote',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Adicione dependências se necessário
    author='Seu Nome',
    author_email='seuemail@exemplo.com',
    description='Um pacote simples de exemplo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/meu_pacote',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
