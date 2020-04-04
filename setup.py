import tokenize
import setuptools
from distutils.command.build_ext import build_ext
"""
                    "src/sipgen/export.c",
                    "src/sipgen/extracts.c",
                    "src/sipgen/gencode.c",
                    "src/sipgen/heap.c",
                    "src/sipgen/lexer.c",
                    "src/sipgen/main.c",
                    "src/sipgen/parser.c",
                    "src/sipgen/transform.c",
                    "src/sipgen/type_hints.c"
"""

try:
    _detect_encoding = tokenize.detect_encoding
except AttributeError:
    pass
else:
    def detect_encoding(readline):
        try:
            return _detect_encoding(readline)
        except SyntaxError:
            return 'latin-1', []

    tokenize.detect_encoding = detect_encoding

class MyBuildExt(build_ext):

    def run(self):
        build_ext.run(self)

        self.compiler.add_include_dir("src/sipgen")
        self.compiler.add_include_dir("src/siplib")

        """
        self.compiler.compile(
                [
                    "src/sipgen/export.c",
                    "src/sipgen/extracts.c",
                    "src/sipgen/gencode.c",
                    "src/sipgen/heap.c",
                    "src/sipgen/lexer.c",
                    "src/sipgen/main.c",
                    "src/sipgen/parser.c",
                    "src/sipgen/transform.c",
                    "src/sipgen/type_hints.c",
                    ],
                include_dirs=["src/sipgen", "src/siplib"])
        """

        self.compiler.link_executable(
                [
                    "src/sipgen/export.c",
                    "src/sipgen/extracts.c",
                    "src/sipgen/gencode.c",
                    "src/sipgen/heap.c",
                    "src/sipgen/lexer.c",
                    "src/sipgen/main.c",
                    "src/sipgen/parser.c",
                    "src/sipgen/transform.c",
                    "src/sipgen/type_hints.c",
                    ],
                'sip',
                output_dir="bin",
                )
        return


setuptools.setup(
        name='python-sip',
        version='0.1',
        scripts=["bin/sip"],
        py_modules=["sipconfig", "sipdistutils"],
        ext_modules=[
            setuptools.Extension(
                "sip",
                [
                    "src/siplib/array.c",
                    "src/siplib/bool.cpp",
                    "src/siplib/descriptors.c",
                    "src/siplib/int_convertors.c",
                    "src/siplib/objmap.c",
                    "src/siplib/qtlib.c",
                    "src/siplib/siplib.c",
                    "src/siplib/threads.c",
                    "src/siplib/voidptr.c",
                    ],
                include_dirs=["src/siplib"]
                ),
            ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        cmdclass = {'build_ext': MyBuildExt},
        )
