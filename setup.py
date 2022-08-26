import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py_sql_table_copy_service',
    version='0.0.1',
    author='Sean Branner',
    author_email='sean.branner@dominos.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://stash.us.dominos.com/scm/~brannes/py-sql-table-copy-service',
    project_urls={
        "Bug Tracker": "https://stash.us.dominos.com/scm/~brannes/py-sql-table-copy-service/issues"
    },
    license='MIT',
    packages=['py_sql_table_copy_service'],
    install_requires=[
        'coverage',
        'deprecation',
        'ffmpeg',
        'filetype',
        'mutagen',
        'packaging',
        'pydub',
        'pyparsing',
        'toml',
        'youtube - dl',
    ],
)
