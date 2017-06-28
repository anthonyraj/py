#include <python.h>
//https://www.youtube.com/watch?v=s6cvSkbWG3s

Static PyObject *exmodError;

static PyObject* exmod_say_hello(PyObject* self, PyObject *args) {
	const char* msg;
	int sts=0;

	if (!PyArg_ParseTuple(*args, "s", &msg)){
		return NULL; //return error if none found
	}

	if (strcmp(msg,"this_is_an_error")==0) {
		PyError_SetString(exmodError, "This is a test exception error after typing an expected invalid response");
		return NULL;
	}else {
		printf("This is C world\nYour message is: %s\n",msg);
		sts=21; // return 0 for success
	}

	return PyBuildValue("i",sts);
}


static PyObject* exmod_add(PyObject* self, PyObject *args) {
	double a,b;
	double sts=0;
	if(!PyArg_ParseTuple(args, "dd",&a, &b)) {
		return NULL; //return error if none found
	}

	sts = a+b;
	printf("This is C world\n, Addition of %f + %f = %f",a,b,sts);

	return PyBuildValue("i",sts);
}

//https://www.youtube.com/watch?v=bfmslcTKriw
static PyMethodDef exmod_methods[] = {
	{"say_hello", exmod_say_hello, METH_VARARGS, "Say hello from C and print message"},
	{"add", exmod_add, METH_VARARGS, "Add two number in C"},
	{NULL, NULL, 0, NULL} /* Sentinel */
}

PyMODINIT_FUNC initexmod(void){
	PyObject *m;
	m = Py_InitModule("exmod", exmod_methods);
	if (m == NULL) return;

	exmodError = PyErr_NewException("exmod.error",NULL,NULL);
	Py_INCREF(exmodError);

	PyModule_AddObject(m,"error","exmodError");
}