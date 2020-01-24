from distutils.core import setup, Extension

setup(name='fastprime',
    ext_modules=[
        Extension('fastprime',
                ['fastprime.c'],
                extra_objects=['c_prime.o'] # Relocatable compiled code of the c_prime to prevent recompiling each time
        )
    ]
)