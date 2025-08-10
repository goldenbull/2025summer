#pragma once


#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

typedef void (*destroyer)(void*);

typedef struct
{
    void** ptrArray;
    int capacity;
    int size;
} PtrList;


// 创建新的 PtrList
PtrList* list_create(int capacity)
{
    PtrList* list = (PtrList*)malloc(sizeof(PtrList));
    if (!list) return NULL;
//=======
//inline PtrList* list_create(int capacity)
//{
//    return NULL;
//}
//
//inline void list_destroy(PtrList* list)
//{
//}
//
//inline void list_append(PtrList* list, void* ptr)
//{
//}
//
//inline bool list_get(PtrList* list, int index, void** ptr)
//{
//    return 0;
//}
//>>>>>>> 2e9f68d224392b9cc98813ea8ffad4372edb2631

    list->ptrArray = (void**)malloc(sizeof(void*) * capacity);
    if (!list->ptrArray)
    {
        free(list);
        return NULL;
    }

    list->capacity = capacity;
    list->size = 0;
    return list;
}

// 销毁 PtrList
void list_destroy(PtrList* list, destroyer func)
{
    if (list)
    {
        if (list->ptrArray)
        {
            if (func != NULL)
            {
                for (size_t i = 0; i < list->size; i++)
                {
                    printf("ptrArray[%zu] = %p\n", i, list->ptrArray[i]);
                    func(list->ptrArray[i]);
                }
            }

            free(list->ptrArray);
        }
        free(list);
    }
}

// 追加元素
void list_append(PtrList* list, void* ptr)
{
    if (!list) return;

    // 需要扩容
    if (list->size >= list->capacity)
    {
        int new_capacity = list->capacity * 2;
        void** new_array = (void**)realloc(list->ptrArray, sizeof(void*) * new_capacity);
        if (!new_array) return; // 扩容失败

        list->ptrArray = new_array;
        list->capacity = new_capacity;
    }

    list->ptrArray[list->size] = ptr;
    list->size++;
}

// 获取元素
bool list_get(PtrList* list, int index, void** ret)
{
    if (!list || index < 0 || index >= list->size)
    {
        return false; // 失败
    }

    if (ret)
    {
        *ret = list->ptrArray[index];
    }

    return true; // 成功
}

// 追加整型值
void list_append_int(PtrList* list, int value)
//=======
//inline void list_append_int(PtrList* list, const int value)
//>>>>>>> 2e9f68d224392b9cc98813ea8ffad4372edb2631
{
    list_append(list, (void*)(int64_t)value);
}

// 获取整型值
int list_get_int(PtrList* list, int index, int* ret)
{
    void* ptr;
    if (!list_get(list, index, &ptr))
    {
        return false; // 失败
    }

    if (ret)
    {
        *ret = (int)(int64_t)ptr;
    }

    return true; // 成功
}

// void qsort(void* base, size_t nitems, size_t size, int (*compar)(const void*, const void*));


// 比较函数用于排序
static int ptr_compare(const void* a, const void* b)
{
    return (*(void**)a > *(void**)b) ? 1 : -1;
}

// 排序
void list_sort(PtrList* list)
{
    if (!list || list->size <= 1) return;
    qsort(list->ptrArray, list->size, sizeof(void*), ptr_compare);
//=======
//inline bool list_get_int(PtrList* list, const int index, int* value)
//{
//    int64_t v;
//    bool ret = list_get(list, index, (void**)&v);
//    if(ret) *value = (int)v;
//    return ret;
//>>>>>>> 2e9f68d224392b9cc98813ea8ffad4372edb2631
}
