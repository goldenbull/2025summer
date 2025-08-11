#include<stdio.h>
#include<stdlib.h>
#include "dict.h"
#include "list.h"

//Ƕ��PtrList���٣������Ӿ��б�
void destroy_clause(void* element) {
	PtrList* clause = (PtrList*)element;
	list_destroy(clause, NULL);
}

int comp_by_v(const KV* a, const KV* b)
{
	return a->value - b->value;
}

PtrList* clone_clause(PtrList* clause)
{
	PtrList* new_clause = list_create(clause->size + 1);
	for (int i = 0; i < clause->size; i++)
	{
		int lit;
		list_get_int(clause, i, &lit);
		list_append_int(new_clause, lit);
	}
	return new_clause;
}

//����ֵ������
PtrList* assign(int x, PtrList* _clauses)
{
	PtrList* new_clauses = list_create(_clauses->capacity);
	for (int i = 0; i < _clauses->size; i++)
	{
		PtrList* clause;
		list_get(_clauses, i, &clause);

		if (list_element_in_list(clause, &x, compare_int))
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

//�ҵ����ִ�����������
int find_literal(PtrList* clauses)
{
	Dict* freq = dict_create(16);
	for (int i = 0; i < clauses->size; i++)
	{
		PtrList* c;
		list_get(clauses, i, &c);
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

	PtrList* sorted_kv = dict_sorted(freq, comp_by_v);
	KV* first_kv = NULL;
	list_get(sorted_kv, 0, &first_kv);
	int max_lit = first_kv->key;

	list_destroy(sorted_kv, NULL);
	dict_destory(freq);

	return max_lit;
}

//dpll����
PtrList* dpll_reduce(PtrList* cur_literals, PtrList* cur_clauses)
{
	//ͨ�����Ӿ���򻯼�
	while (1)
	{
		bool found = false;
		for (int i = 0; i < cur_clauses->size; i++)
		{
			PtrList* c;
			list_get(cur_clauses, i, &c);
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
			list_get(cur_clauses, i, &c);
			if (c->size == 1)
				list_append(single_litral_clauses, c);
		}

		PtrList* first_clause;
		list_get(single_litral_clauses, 0, & first_clause);
		int single_literal;
		list_get_int(first_clause, 0, &single_literal);
		list_destroy(single_litral_clauses, NULL);

		list_append_int(cur_literals, single_literal);
		PtrList* new_clauses = assign(single_literal, cur_clauses);
		list_destroy(cur_clauses, destroy_clause);  // ͨ������ָ��ָ�����ٷ�ʽ
		cur_clauses = new_clauses;

		//�ж��Ƿ����
		if (cur_clauses->size==0)
			return cur_literals;
		bool found_empty_clause = false;
		for (int i = 0; i < cur_clauses->size; i++)
		{
			PtrList* c;
			list_get(cur_clauses, i, &c);
			if (c->size == 0)
			{
				found_empty_clause = true;
				break;
			}
		}
		if (found_empty_clause)
			return NULL;
	}

	//�ж��Ƿ����
	if (cur_clauses->size==0)
		return cur_literals;
	bool found_empty_clause = false;
	for (int i = 0; i < cur_clauses->size; i++)
	{
		PtrList* c;
		list_get(cur_clauses, i, &c);
		if (c->size == 0)
		{
			found_empty_clause = true;
			break;
		}
	}
	if (found_empty_clause)
		return NULL;

	//ѡ�����ָ�ֵ
	int next_lit = find_literal(cur_clauses);

	//���Ը�ֵΪtrue
	PtrList* reduced_clauses_true = assign(next_lit, cur_clauses);
	PtrList* new_literals_true = clone_clause(cur_literals);
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

	//���Ը�ֵΪfalse
	PtrList* reduced_clauses_false = assign(-next_lit, cur_clauses);
	PtrList* new_literals_false = clone_clause(cur_literals);
	list_append_int(new_literals_false, -next_lit);
	result = dpll_reduce(new_literals_false, reduced_clauses_false);
	list_destroy(new_literals_false, NULL);
	list_destroy(reduced_clauses_false, destroy_clause);
	return result;
}