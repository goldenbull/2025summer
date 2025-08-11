#pragma once

#include "list.h"

typedef struct
{
    int row;
    int col;
} Coordinate;

PtrList* get_box(int r, int c);

PtrList* read_lines(const char* filename);
