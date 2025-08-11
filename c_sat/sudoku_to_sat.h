#pragma once

#include <stdlib.h>
#include "list.h"

extern PtrList* rows;
extern PtrList* cols;
extern PtrList* boxes;
extern PtrList* pcf_centers;
extern PtrList* pcf_boxes;
extern PtrList* cross_line;

//初始化数独结构
void init_sudoku_structures();
