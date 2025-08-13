#pragma once

PtrList* str_split(const char* s);

PtrList* read_file(const char* filename);

void destroy_clause(void* element);

int comp_by_v(const KV* a, const KV* b);

PtrList* clone_clause(PtrList* clause);

PtrList* assign(int x, PtrList* _clauses);

int find_literal(PtrList* clauses);

PtrList* dpll_reduce(PtrList* cur_literals, PtrList* cur_clauses);