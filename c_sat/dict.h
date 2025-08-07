#pragma once

typedef struct
{
	int dummy;
}Dict;

Dict* dict_create();
void dict_destroy(Dict* dict);
void dict_set(Dict* dict, int key, int value);
int dict_get(Dict* dict, int key, int* value);