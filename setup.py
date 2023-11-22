from setuptools import setup, find_packages
import pathlib
setup(
    keywords='TeX, LaTeX, latexcalc, texcalc, calctex, calclatex, calculate',
    packages=find_packages(),
    python_requires='>=3.7, <4',
    install_requires=['latexcalc'],
    project_urls={
        'Bug Reports': 'https://github.com/polarwinkel/latexcalc/issues',
        'Source': 'https://github.com/polarwinkel/latexcalc',
    },
)
