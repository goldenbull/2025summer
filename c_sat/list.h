#pragma once

#include<stdbool.h>

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

int list_get_int(PtrList* list, int index, int* ret);

void list_sort(PtrList* list, comparer comp);

bool list_element_in_list(PtrList* list, const void* element, comparer comp);

inline int compare_int(const void* a, const void* b)
{
	if (!a || !b) return false;
	else if (*(int*)a < *(int*)b) return -1;
	else if (*(int*)a == *(int*)b) return 0;
	else return 1;
}