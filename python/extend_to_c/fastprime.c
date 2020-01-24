#include "python3.7m/Python.h"  // Python provides its API via Python.h header file
#include "primeheader.h"

// A static function which takes PyObjects arguments and returns a PyObject result
static PyObject* py_kthPrime(PyObject* self, PyObject* args) {
    int n;
    // date and parse the arguments received to function so that its usable by C
    if (!PyArg_ParseTuple(args, "i", &n)) 
        return NULL;
    return Py_BuildValue("i", kthPrime(n)); // Get result from C, wrap it up with a PyObject and return it
}

// Define a collection of methods collable from our module
static PyMethodDef PyFastPrimeMethods[] = {
    {"kthPrime", py_kthPrime, METH_VARARGS, "Find the kth prime number"}
};

// Module definition
static struct PyModuleDef fastprimemodule = {
    PyModuleDef_HEAD_INIT,
    "fastprime",
    "This module calculates the kth prime number",
    -1,
    PyFastPrimeMethods
};

// This method is called when you import your code in python. It instantiates the module and returns a reference to it
PyMODINIT_FUNC PyInit_fastprime(void) {
    return PyModule_Create(&fastprimemodule);
}
