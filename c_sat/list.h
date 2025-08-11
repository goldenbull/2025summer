#pragma once

#include<stdbool.h>

typedef void (*destroyer)(void*);

typedef struct
{
    void** ptrArray;
    int capacity;
    int size;
} PtrList;

PtrList* list_create(int capacity);

void list_destroy(PtrList* list, destroyer func);

void list_append(PtrList* list, void* ptr);

bool list_get(PtrList* list, int index, void** ret);

int list_get_int(PtrList* list, int index, int* ret);

void list_append_int(PtrList* list, int value);

static int ptr_compare(const void* a, const void* b);

void list_sort(PtrList* list);
