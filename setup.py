from setuptools import setup

setup(name='pushould-python',
      version='0.0.3',
      description='RealTime without pain.',
      url='https://pushould.com',
      author='Yu Hoshino',
      author_email='yhoshino11@gmail.com',
      license='MIT',
      packages=['pushould'],
      install_requires=['requests==2.9.1', 'nose==1.3.7'],
      tests_require=['nose', 'httpretty'],
      zip_safe=False)
