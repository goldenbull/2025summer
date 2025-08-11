#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "list.h"
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
    {
        printf("�ļ���ʧ��");
        return NULL;
    }
    
    PtrList* lines = list_create(10);
    if (!lines) return NULL;

    char content[10240];
    while (fgets(content, sizeof(content), file))
    {
        char* line_copy = strdup(content);
        list_append(lines, line_copy);
    }
    if (ferror(file))
    {
        perror("�ļ���ȡ����");
        list_destroy(lines, free);
        lines = NULL;
    }
    fclose(file);
    return lines;
}

//ʹ�ú�Ҫlist_destroy(lines,free)


void append_coordiante(PtrList* coordinates, int row, int col)
{
    if (!coordinates) return;
    Coordinate* c = malloc(sizeof(Coordinate));
    if (!c) return;
    c->row = row;
    c->col = col;
    list_append(coordinates, c);
}