import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="codino",
    version="0.0.1",
    author="David Zhang",
    author_email="dyzhang32@gmail.com",
    description="Calculating AA frequencies from codon frequencies and "
                "vice-versa",
    long_description=long_description,
    long_description_content_type="text/md",
    url="https://github.com/dzhang32/codon_aa_freq",
    project_urls={
        "Bug Tracker": "https://github.com/dzhang32/codon_aa_freq/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "codon_aa_freq"},
    packages=setuptools.find_packages(where="codon_aa_freq"),
    python_requires=">=3.8",
)
