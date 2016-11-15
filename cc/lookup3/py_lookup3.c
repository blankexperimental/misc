#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "lookup3.h"

static PyObject* lookup3_hashlittle(PyObject *self, PyObject *args) {
  const char *key;
  uint32_t hash = 0;

  if (!PyArg_ParseTuple(args, "s", &key)) {
    return NULL;
  }

  hash = hash32(key, strlen(key));
  return Py_BuildValue("I", hash);
}

static PyObject* lookup3_hashlittle2(PyObject *self, PyObject *args) {
  const char *key;
  uint64_t hash = 0;

  if (!PyArg_ParseTuple(args, "s", &key)) {
    return NULL;
  }
  hash = hash64(key, strlen(key));
  return Py_BuildValue("K", hash);
}

static PyMethodDef lookup3_methods[] = {
  {"hash32", (PyCFunction)lookup3_hashlittle, METH_VARARGS | METH_KEYWORDS, "lookup3 hashlittle"},
  {"hash64", (PyCFunction)lookup3_hashlittle2, METH_VARARGS | METH_KEYWORDS, "lookup3 hashlittle2"},
  {NULL, NULL, 0, NULL}   /* sentinel */
};

void initlookup3(void) {
  Py_InitModule("lookup3", lookup3_methods);
}