from distutils.core import setup

setup(
    name='bluematador',
    version='0.1dev',
    packages=['bluematador'],
    license='MIT',
    description='Send StatsD-style custom metrics to your Blue Matador account.',
    long_description=open('README').read(),
    url='https://github.com/bluematador/bluematador-metrics-client-python',
    author='Mark Siebert',
    author_email='mark@bluematador.com',
)
