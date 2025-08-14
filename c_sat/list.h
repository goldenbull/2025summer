#pragma once

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

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

bool list_int_in_list(PtrList* list, int val);

void list_random_shuffle(PtrList* list);

inline int compare_int(const void* a, const void* b)
{
    int ia = (int)(int64_t)*(void**)a; // 直接转换指针值为整数
    int ib = (int)(int64_t)*(void**)b;
    if (ia < ib) return -1;
    if (ia == ib) return 0;
    return 1;
}

inline int compare_int_list(const PtrList* a, const PtrList* b)
{
    if (a == NULL || b == NULL) return false;

    const int compare_size = min(a->size, b->size);
    for (int i = 0; i < compare_size; i++)
    {
        const int va = (int)(int64_t)a->ptrArray[i];
        const int vb = (int)(int64_t)b->ptrArray[i];
        if (va > vb) return 1;
        if (va < vb) return -1;
    }

    if (a->size > b->size) return 1;
    if (a->size < b->size) return -1;
    return 0;
}

inline int compare_int_list_qsort(const void* a, const void* b)
{
    return compare_int_list(*(PtrList**)a, *(PtrList**)b);
}
