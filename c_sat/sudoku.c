#include <stdio.h>
#include <stdlib.h>

#include "list.h"
#include "sudoku.h"

PtrList* get_box(int r, int c) 
{
    PtrList* ret = list_create(9);
    for (int i = r; i < r + 3; i++)
    {
        for (int j = c; j < c + 3; j++)
        {
            Coordinate* coord = malloc(sizeof(Coordinate));
            if (coord)
            {
                coord->row = i;
                coord->col = j;
                list_append(ret, coord);
            }
        }
    }

    return ret;
}

PtrList* read_lines(const char* filename)
{
    FILE* file = fopen(filename, "r");
    if (!file)
        return NULL;
    PtrList* lines = list_create(10);
    return NULL;
}