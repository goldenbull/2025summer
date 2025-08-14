#pragma once

#include <stdlib.h>
#include "list.h"

extern PtrList* rows;
extern PtrList* cols;
extern PtrList* boxes;
extern PtrList* pcf_centers;
extern PtrList* pcf_boxes;
extern PtrList* cross_line;

void init_sudoku_structures();

void create_cnf(char* filename);
