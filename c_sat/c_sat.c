#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include "list.h"
#include "dict.h"
#include "sudoku.h"
#include "sudoku_to_sat.h"


void test1()
{
	while (1)
	{
		PtrList* list = list_create(1000000);
		for (int i = 0; i < 1000000; i++)
		{
			Coordinate* c = malloc(sizeof(Coordinate));
			if (c)
			{
				c->row = 1;
				c->col = 2;
				list_append(list, c);
			}
		}
		list_destroy(list, free);
	}
}

void test2()
{
	PtrList* list = list_create(10);
	int a = 10, b = 4;
	list_append_int(list, a);
	list_append_int(list, b);
	list_append_int(list, 8);
	for (int i=0; i < list->size; i++)
	{
		printf("%lld ", (int64_t)list->ptrArray[i]);
	}
	printf("\n");
	list_sort(list, compare_int);
	for (int i=0; i < list->size; i++)
	{
		printf("%lld ", (int64_t)list->ptrArray[i]);
	}
	list_destroy(list, NULL);
}

void test3()
{
	Dict* dict = dict_create(5);
	dict_set(dict, 1, 100);
	dict_set(dict, 2, 200);
	int val;
	dict_get(dict, 2, &val);
	printf("%d\n", val);
	dict_set(dict, 2, 222);
	dict_set(dict, 3, 300);
	dict_set(dict, 4, 400);
	for (int i = 0; i < dict->bucket_cnt; i++)
	{
		PtrList* bucket = dict->buckets[i];
		for (int j = 0; j < bucket->size; j++)
		{

			KV* kv = bucket->ptrArray[j];
			printf("%d,%d ", kv->key, kv->value);
		}
	}
	printf("\n");
	PtrList* kvs = list_create(4);
	//kvs = dict_sorted(dict);
	//for (int i = 0; i < kvs->size; i++) {
	//	KV* kv = kvs->ptrArray[i];
	//	printf("%d,%d ", kv->key, kv->value);
	//}
	dict_destory(dict);
}

void test4()
{
	while (1)
	{
		Dict* dict = dict_create(1000);
		for (int i = 0; i < 1000000; i++)
		{
			dict_set(dict, i, i*i);
		}
		dict_destory(dict);
	}
}

int main(void)
{
	init_sudoku_structures();

	test4();
	return 0;
}