#pragma once

typedef struct
{
	void** ptrArray;
	int capacity;
	int size;
}PtrList;

PtrList* list_create(int init_size) {}
void list_destroy(PtrList* list) {}
void list_append(PtrList* list, void* ptr) {}
int list_get(PtrList* list, int index, void** ret) {} // 0-fail 1-success

//PtrList* list_clone(PtrList* list) {}

void list_append_int(PtrList* list, int value)
{
	list_append(list, (void*)(__int64)value);
}

int list_get_int(PtrList* list, int index, int* ret)
{
	return list_get(list, index, (void**)(__int64*)ret);
}
