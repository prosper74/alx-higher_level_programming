#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information 
 *
 * @pyObject: Python Object 
 * Return: no return
*/
void print_python_bytes(PyObject *pyObject)  
{
  char *str;
  long int size, i, limit;

  printf("[.] bytes object info\n");
  if (!PyBytes_Check(pyObject))
  {
    printf("  [ERROR] Invalid Bytes Object\n");
    return; 
  }

  size = ((PyVarObject *)(pyObject))->ob_size;
  str = ((PyBytesObject *)pyObject)->ob_sval;

  printf("  size: %ld\n", size);
  printf("  trying string: %s\n", str);

  if (size >= 10)
    limit = 10;
  else  
    limit = size + 1;

  printf("  first %ld bytes:", limit);

  for (i = 0; i < limit; i++)
    if (str[i] >= 0)
      printf(" %02x", str[i]);
    else
      printf(" %02x", 256 + str[i]);

  printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @pyObject: Python Object
 * Return: no return
*/
void print_python_list(PyObject *pyObject)
{
  long int size, i;
  PyListObject *pyList;
  PyObject *listItem;

  size = ((PyVarObject *)(pyObject))->ob_size;
  pyList = (PyListObject *)pyObject;

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", pyList->allocated);

  for (i = 0; i < size; i++)
  {
    listItem = ((PyListObject *)pyObject)->ob_item[i];
    printf("Element %ld: %s\n", i, ((listItem)->ob_type)->tp_name);
    if (PyBytes_Check(listItem))
      print_python_bytes(listItem);
  }
}
