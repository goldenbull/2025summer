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

// �����µ� PtrList
PtrList* list_create(int capacity)
{
    PtrList* list = (PtrList*)malloc(sizeof(PtrList));
    if (!list) return NULL;

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

// ���� PtrList
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
                    func(list->ptrArray[i]);
                }
            }

            free(list->ptrArray);
        }
        free(list);
    }
}

// ׷��Ԫ��
void list_append(PtrList* list, void* ptr)
{
    if (!list) return;

    // ��Ҫ����
    if (list->size >= list->capacity)
    {
        int new_capacity = list->capacity * 2;
        void** new_array = (void**)realloc(list->ptrArray, sizeof(void*) * new_capacity);
        if (!new_array) return; // ����ʧ��

        list->ptrArray = new_array;
        list->capacity = new_capacity;
    }

    list->ptrArray[list->size] = ptr;
    list->size++;
}

// ��ȡԪ��
bool list_get(PtrList* list, int index, void** ret)
{
    if (!list || index < 0 || index >= list->size)
    {
        return false; // ʧ��
    }

    if (ret)
    {
        *ret = list->ptrArray[index];
    }

    return true; // �ɹ�
}

// ׷������ֵ
void list_append_int(PtrList* list, int value)
{
    list_append(list, (void*)(int64_t)value);
}

// ��ȡ����ֵ
int list_get_int(PtrList* list, int index, int* ret)
{
    void* ptr;
    if (!list_get(list, index, &ptr))
    {
        return false; // ʧ��
    }

    if (ret)
    {
        *ret = (int)(int64_t)ptr;
    }

    return true; // �ɹ�
}

// void qsort(void* base, size_t nitems, size_t size, int (*compar)(const void*, const void*));


// �ȽϺ�����������
static int ptr_compare(const void* a, const void* b)
{
    return (*(void**)a > *(void**)b) ? 1 : -1;
}

// ����
void list_sort(PtrList* list)
{
    if (!list || list->size <= 1) return;
    qsort(list->ptrArray, list->size, sizeof(void*), ptr_compare);
}
