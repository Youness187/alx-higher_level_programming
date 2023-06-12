#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: PyObject.
 */
void print_python_list_info(PyObject *p)
{
	long int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
