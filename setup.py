import codecs
from setuptools import setup


with codecs.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="nonshadowsocks",
    version="3.0.1",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="A fast tunnel proxy that help you get through firewalls",
    author='clowwindy, NotStatilko',
    author_email='clowwindy42@gmail.com, thenonproton@pm.me',
    url='https://github.com/NotStatilko/shadowsocks',
    packages=['shadowsocks', 'shadowsocks.crypto'],
    package_data={
        'shadowsocks': ['README.md', 'LICENSE']
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    sslocal = shadowsocks.local:main
    ssserver = shadowsocks.server:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
