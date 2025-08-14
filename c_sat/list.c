#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include "list.h"


// �����µ� PtrList
PtrList* list_create(int capacity)
{
    PtrList* list = malloc(sizeof(PtrList));
    if (!list) return NULL;
    list->ptrArray = malloc(sizeof(void*) * capacity);
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
                    //printf("ptrArray[%zu] = %p\n", i, list->ptrArray[i]);
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
    if (!list)
        return;

    // ��Ҫ����
    if (list->size >= list->capacity)
    {
        int new_capacity = list->capacity * 12 / 10 + 10;
        void** new_array = realloc(list->ptrArray, sizeof(void*) * new_capacity);
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
bool list_get_int(PtrList* list, int index, int* ret)
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

// ��������Ԫ��
bool list_set_int(PtrList* list, int index, int value)
{
    if (!list || index < 0 || index >= list->size)
        return false;
    list->ptrArray[index] = (void*)(int64_t)value;
    return true;
}

// ����
void list_sort(PtrList* list, comparer comp)
{
    if (!list || list->size <= 1) return;
    qsort(list->ptrArray, list->size, sizeof(void*), comp);
}


// �ж�Ԫ���Ƿ��ڱ���
bool list_element_in_list(PtrList* list, const void* element, comparer comp)
{
    if (!list || !element) return false;

    for (int j = 0; j < list->size; j++)
    {
        void* val;
        list_get(list, j, &val);
        if (comp(element, val) == 0)
        {
            return true;
        }
    }

    return false;
}

bool list_int_in_list(PtrList* list, int val)
{
    if (!list) return false;

    for (int j = 0; j < list->size; j++)
    {
        if ((int)(int64_t)list->ptrArray[j] == val)
            return true;
    }

    return false;
}

// �������˳��
void list_random_shuffle(PtrList* list)
{
    if (!list || list->size <= 1) return;

    for (int i = 0; i < list->size * 10; i++)
    {
        int x = rand() % list->size;
        int y = rand() % list->size;
        void* temp = list->ptrArray[x];
        list->ptrArray[x] = list->ptrArray[y];
        list->ptrArray[y] = temp;
    }
}
