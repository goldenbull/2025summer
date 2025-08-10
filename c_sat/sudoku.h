#pragma once
#include "list.h"

typedef struct
{
    int row;
    int col;
} Coordinate;

PtrList* get_box(int r, int c) {
    PtrList* ret = list_create(9);
    for (int i = r; i < r + 3; i++)
    {
        for (int j = c; j < c + 3; j++)
        {
            Coordinate* coord = malloc(sizeof(Coordinate));
            coord->row = i;
            coord->col = j;
            list_append(ret, coord);
        }
    }
    return ret;
}
