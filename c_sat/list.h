#pragma once

#include <stdint.h>
#include <stdbool.h>

typedef struct
{
    void** ptrArray;
    int capacity;
    int size;
} PtrList;

inline PtrList* list_create(int capacity)
{
    return NULL;
}

inline void list_destroy(PtrList* list)
{
}

inline void list_append(PtrList* list, void* ptr)
{
}

inline bool list_get(PtrList* list, int index, void** ptr)
{
    return 0;
}

//PtrList* list_clone(PtrList* list) {}

inline void list_append_int(PtrList* list, const int value)
{
    list_append(list, (void*)(int64_t)value);
}

inline bool list_get_int(PtrList* list, const int index, int* value)
{
    int64_t v;
    bool ret = list_get(list, index, (void**)&v);
    if(ret) *value = (int)v;
    return ret;
}
