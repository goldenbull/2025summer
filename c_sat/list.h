#pragma once

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef void (*destroyer)(void*);
typedef int (*comparer)(const void* a, const void* b);

typedef struct
{
    void** ptrArray;
    int capacity;
    int size;
} PtrList;

PtrList* list_create(int capacity);

void list_destroy(PtrList* list, destroyer func);

void list_append(PtrList* list, void* ptr);

void list_append_int(PtrList* list, int value);

bool list_get(PtrList* list, int index, void** ret);

bool list_get_int(PtrList* list, int index, int* ret);

bool list_set_int(PtrList* list, int index, int value);

void list_sort(PtrList* list, comparer comp);

bool list_element_in_list(PtrList* list, const void* element, comparer comp);

void list_random_shuffle(PtrList* list);

inline int compare_int(const void* a, const void* b) {
	int ia = (int)(intptr_t)a;  // 直接转换指针值为整数
	int ib = (int)(intptr_t)b;
	return (ia > ib) - (ia < ib);
}

inline int compare_int_list(const PtrList* a, const PtrList* b)
{
	if (a == NULL || b == NULL) return false;
	int compare_size = a->size - b->size;
	if(!compare_size)
	{
		int co_size = a->size;
		int compare_mem = memcmp(a->ptrArray, b->ptrArray, co_size);
		if (!compare_mem)
			return 0;
	}
	return 1;
}