from distutils.core import setup

setup(
      name='serachTour',
      version='1.0',
      author='DY&EK',
      author_email='neltique123@gmail.com',
      url = "https://github.com/neltique/2020_script_language_with_DY",
      description='Tkinter search Tour Project by DY&Ek',
      python_requires='>=3',
      install_requires = ['selenium==3.141.0',
      'pymongo==3.10.1',
      'bs4==0.0.1',
      'telepot==12.7',
      'urllib3==1.25.9',
      'Pillow==7.1.2',
      'requests==2.23.0',
      'tkinterhtml==0.7'],
      py_modules = ['chatbot','kakaoMap','tourData','toursearchgui','dictToHTML']

)


