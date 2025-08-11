#include<stdio.h>
#include<stdlib.h>
#include "dict.h"
#include "list.h"

//嵌套PtrList销毁（用于子句列表）
void destroy_clause(void* element) {
	PtrList* clause = (PtrList*)element;
	list_destroy(clause, NULL);
}

//处理赋值的文字
PtrList* assign(int x, PtrList* _clauses)
{
	PtrList* new_clauses = list_create(_clauses->capacity);
	for (int i = 0; i < _clauses->size; i++)
	{
		PtrList* clause;
		list_get(_clauses, i, (void**)&clause);
		bool x_in_clause = false;
		for (int j = 0; j < clause->size; j++)
		{
			int val;
			list_get_int(clause, j, &val);
			if (val == x)
			{
				x_in_clause = true;
				break;
			}
		}
		if (x_in_clause)
			continue;

		PtrList* new_clause = list_create(clause->capacity);
		for (int j = 0; j < clause->size; j++)
		{
			int l;
			list_get_int(clause, j, &l);
			if (l != -x)
				list_append_int(new_clauses, l);
		}
		list_append(new_clauses, new_clause);
	}
	return new_clauses;
}

//找到出现次数最多的文字
int find_literal(PtrList* clauses)
{
	Dict* freq = dict_create(16);
	for (int i = 0; i < clauses->size; i++)
	{
		PtrList* c;
		list_get(clauses, i, (void**)&c);
		for (int j = 0; j < c->size; j++)
		{
			int lit;
			list_get_int(c, j, &lit);
			int cur_cnt;
			if (!dict_get(freq, lit, &cur_cnt))
				cur_cnt = 0;
			dict_set(freq, lit, cur_cnt + 1);
		}
	}

	PtrList* kvs = dict_sorted(freq);
	int max_lit = 0;
	int max_cnt = -1;
	for (int i = 0; i < kvs->size; i++)
	{
		KV* item;
		list_get(kvs, i, (void**)&item);
		if (item->value>max_cnt)
		{
			max_cnt = item->value;
			max_lit = item->key;
		}
	}
	list_destroy(kvs, NULL);
	dict_destory(freq);

	return max_lit;
}

//dpll函数
PtrList* dpll_reduce(PtrList* cur_literals, PtrList* cur_clauses)
{
	//通过单子句规则化简
	while (1)
	{
		bool found = false;
		for (int i = 0; i < cur_clauses->size; i++)
		{
			PtrList* c;
			list_get(cur_clauses, i, (void**)&c);
			if (c->size == 1)
			{
				found = true;
				break;
			}
		}
		if (!found)
			break;

		PtrList* single_litral_clauses = list_create(cur_clauses->capacity);
		for (int i = 0; i < cur_clauses->size; i++)
		{
			PtrList* c;
			list_get(cur_clauses, i, (void**)&c);
			if (c->size == 1)
				list_append(single_litral_clauses, c);
		}

		PtrList* first_clause;
		list_get(single_litral_clauses, 0, (void**)& first_clause);
		int single_literal;
		list_get_int(first_clause, 0, &single_literal);
		list_destroy(single_litral_clauses, NULL);

		list_append_int(cur_literals, single_literal);
		PtrList* new_clauses = assign(single_literal, cur_clauses);
		list_destroy(cur_clauses, destroy_clause);  // 通过函数指针指定销毁方式
		cur_clauses = new_clauses;

		//判断是否结束
		if (cur_clauses->size==0)
			return cur_literals;
		bool found_empty_clause = false;
		for (int i = 0; i < cur_clauses->size; i++)
		{
			PtrList* c;
			list_get(cur_clauses, i, (void**)&c);
			if (c->size == 0)
			{
				found_empty_clause = true;
				break;
			}
		}
		if (found_empty_clause)
			return NULL;
	}

	if (cur_clauses->size==0)
		return cur_literals;
	bool found_empty_clause = false;
	for (int i = 0; i < cur_clauses->size; i++)
	{
		PtrList* c;
		list_get(cur_clauses, i, (void**)&c);
		if (c->size == 0)
		{
			found_empty_clause = true;
			break;
		}
	}
	if (found_empty_clause)
		return NULL;

	//选择文字赋值
	int next_lit = find_literal(cur_clauses);

	//尝试赋值为true
	PtrList* reduced_clauses_true = assign(next_lit, cur_clauses);
	PtrList* new_literals_true = list_create(cur_literals->size + 1);
	for (int i = 0; i < cur_literals->size; i++)
	{
		int lit;
		list_get_int(cur_literals, i, &lit);
		list_append_int(new_literals_true, lit);
	}
	list_append_int(new_literals_true, next_lit);
	PtrList* result = dpll_reduce(new_literals_true, reduced_clauses_true);
	if (result != NULL)
	{
		list_destroy(new_literals_true,NULL);
		list_destroy(reduced_clauses_true, destroy_clause);
		return result;
	}
	list_destroy(new_literals_true, NULL);
	list_destroy(reduced_clauses_true, destroy_clause);

	//尝试赋值为false
	PtrList* reduced_clauses_false = assign(-next_lit, cur_clauses);
	PtrList* new_literals_false = list_create(cur_literals->size + 1);
	for (int i = 0; i < cur_literals->size; i++) 
	{
		int lit;
		list_get_int(cur_literals, i, &lit);
		list_append_int(new_literals_false, lit);
	}
	list_append_int(new_literals_false, -next_lit);
	result = dpll_reduce(new_literals_false, reduced_clauses_false);
	list_destroy(new_literals_false, NULL);
	list_destroy(reduced_clauses_false, destroy_clause);
	return result;
}