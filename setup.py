import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()


setuptools.setup(
    name="rasa_chinese_plugin",
    version="1.0",
    author="ZhongLei",
    author_email="625015751@qq.com",
    decciption="rasa中文拓展包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zlxwl/rasa_chinese_extend_plugin.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT Liense",
        "Operating System :: OS Independent",
    ],
)