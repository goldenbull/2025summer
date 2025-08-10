#pragma once

#include "list.h"
#include<stdbool.h>

typedef struct
{
    int key;
    int value;
} KV;

inline int hash(int x)
{
    x = ((x >> 16) ^ x) * 0x45d9f3b;
    x = ((x >> 16) ^ x) * 0x45d9f3b;
    x = (x >> 16) ^ x;
    if (x < 0) x = -x;
    return x;
}

typedef struct
{
    PtrList** buckets;
    int bucket_cnt;
} Dict;

inline Dict* dict_create(int bucket_cnt)
{
    Dict* dict = malloc(sizeof(Dict));
    dict->buckets = (PtrList**)malloc(sizeof(PtrList*) * bucket_cnt);
    for (int i = 0; i < bucket_cnt; ++i)
    {
        dict->buckets[i] = list_create(32);
    }
    dict->bucket_cnt = bucket_cnt;
    return dict;
}

inline void dict_destory(Dict* dict)
{
    for (int i = 0; i < dict->bucket_cnt; ++i)
    {
        PtrList* bucket = dict->buckets[i];
        for (int j = 0; j < bucket->size; ++j)
        {
            KV* kv = bucket->ptrArray[j];
            free(kv);
        }
        list_destroy(bucket,free);
    }

    free(dict->buckets);
    free(dict);
}

inline PtrList* dict_get_bucket(const Dict* dict, const int key)
{
    // get bucket by hash of key
    const int bucket_idx = hash(key) % dict->bucket_cnt;
    PtrList* bucket = dict->buckets[bucket_idx];
    return bucket;
}

inline KV* dict_find_kv(const Dict* dict, const int key)
{
    PtrList* bucket = dict_get_bucket(dict, key);

    // search key in bucket
    KV* kv = NULL;
    for (int i = 0; i < bucket->size; ++i)
    {
        KV* kv2 = bucket->ptrArray[i];
        if (kv2->key == key)
        {
            kv = kv2;
            break;
        }
    }

    return kv;
}

inline void dict_set(const Dict* dict, const int key, const int value)
{
    KV* kv = dict_find_kv(dict, key);
    if (kv == NULL)
    {
        // insert new kv into bucket
        kv = malloc(sizeof(KV));
        kv->key = key;
        kv->value = value;

        PtrList* bucket = dict_get_bucket(dict, key);
        list_append(bucket, kv);
    }
    else
    {
        kv->value = value;
    }
}

inline bool dict_get(const Dict* dict, const int key, int* value)
{
    KV* kv = dict_find_kv(dict, key);
    if (kv == NULL)
    {
        return false;
    }
    else
    {
        *value = kv->value;
        return true;
    }
}

static int dic_compare(const void* a, const void* b)
{
    const KV* kv1 = *(const KV**)a;
    const KV* kv2 = *(const KV**)b;
    return kv2->key - kv1->key;
}

//从大到小排序
PtrList* dict_sorted(const Dict* dict)
{
    //取出所有键值对
    PtrList* kvs = list_create(dict->bucket_cnt * 32);
    for (int i = 0; i < dict->bucket_cnt; i++)
    {
        PtrList* bucket = dict->buckets[i];
        for (int j = 0; j < bucket->size; j++)
        {
            KV* kv = bucket->ptrArray[j];
            list_append(kvs, kv);
        }
    }
    qsort(kvs->ptrArray, kvs->size, sizeof(KV*), dic_compare);
    return kvs;
}