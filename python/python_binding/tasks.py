import cffi
import invoke
import pathlib


@invoke.task
def clean(c):
    """ Remove any build objects """
    for pattern in ['*.o', '*.so', 'cffi_example*', 'cython_wrapper.cpp']:
        c.run(f'rm -rf {pattern}')


def print_banner(msg):
    print('===============================================')
    print(f'= {msg}')


@invoke.task
def build_cmult(c):
    """ Build the shared library for the sample C code """
    print_banner('Building C Library')
    invoke.run('gcc -c -Wall -Werror -fpic cmult.c -I /usr/include/python3.6')
    invoke.run('gcc -shared -o libcmult.so cmult.o')
    print('* Complete')

@invoke.task(build_cmult)
def test_ctypes(c):
    """ Run the script to test ctypes """
    print_banner('Testing ctypes Module')
    invoke.run('python ctypes_test.py', pty=True)


@invoke.task(build_cmult)
def build_cffi(c):
    """ Build the CFFI Python bindings """
    print_banner('Building CFFI Module')
    ffi = cffi.FFI()

    this_dir = pathlib.Path().absolute()
    h_file_name = this_dir / 'cmult.h'
    with open(h_file_name) as h_file:
        ffi.cdef(h_file.read())

    ffi.set_source(
        'cffi_example',
        # Since we are calling a fully built library directly no custom source
        # is necessary. We need to include the .h files, though, because behind
        # the scenes cffi generates a .c file which contains a Python-friendly
        # wrapper around each of the functions.
        '#include "cmult.h"',
        # The important thing is to include the pre-built lib in the list of
        # libraries we are linking against:
        libraries=['cmult'],
        library_dirs=[this_dir.as_posix()],
        extra_link_args=['-Wl,-rpath,.']
    )

    ffi.compile()
    print('* Complete')


@invoke.task(build_cffi)
def test_cffi(c):
    """Run the script to thest CFFI"""
    print_banner('Testing CFFI Module')
    invoke.run('python cffi_test.py', pty=True)
