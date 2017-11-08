from setuptools import setup,find_packages

# setup(
#     name='pyautoenv',
#     version='1.0.0',
#     desctiption='Python Environment Setup',
#     url='https://github.com/pbprathi/python_Subprocess',
#     author='Bhageerath Babu Prathi',
#     author_email='pbprathi@gmail.com',
#     license='prathi',
#     packages=find_packages()
# )

setup(
    name = "autopy",
    version = "2.0.0",
    author = "Bhageerath",
    author_email = "pbprathi@gmail.com",
    description = ("My first application using subprocess module."),
    license = "prathi",
    keywords = "example documentation tutorial",
    include_package_data=True,
    url = "https://github.com/pbprathi/python_Subprocess",
    #install_requires=['subprocess'],
    packages=find_packages(exclude=['test','docs']),
    classifiers=["Development Status :: 3 - Alpha"],

    entry_points={
    'console_scripts': ['sapp=autopy.mainmodule:main']
    }
    #long_description=read('README'),

)
