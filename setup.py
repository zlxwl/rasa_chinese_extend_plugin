import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()


setuptools.setup(
    name="rasa_chinese_plugin",
    version="6.0",
    author="ZhongLei",
    author_email="625015751@qq.com",
    description="rasa_chi_exd",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/zlxwl/rasa_chinese_extend_plugin.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)