import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='trails',
     version='1.0',
     scripts=['trails/run.py'] ,
     author="Rameshkanth Subramani",
     author_email="jobs.ksrk@gmail.com",
     description="Demo application",
     long_description=long_description,
     packages=setuptools.find_packages(),
     package_data={'trails': ['data/*', 'templates/stores/*', 
                              'static/stores/*']},
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
