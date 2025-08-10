#include<stdio.h>
#include<stdlib.h>
#include "dict.h"
#include "list.h"
#include "sudoku.h"

PtrList* rows = NULL;
PtrList* clos = NULL;
PtrList* boxes = NULL;
PtrList* pcf_boxes = NULL;
PtrList* cross_line = NULL;

void init_sudoku_structures(PtrList** rows, PtrList** cols, PtrList** boxes,
    PtrList** pcf_boxes, PtrList** pcf_centers, PtrList** cross_line)
{
    *rows = list_create(9);
    for (int i = 1; i < 10; i++)
    {
        PtrList* s_rows = list_create(9);
        for (int j = 1; j < 10; j++)
        {
            Coordinate* c = malloc(sizeof(Coordinate));
            c->row = j;
            c->col = i;
            list_append(s_rows, c);
        }
        list_append(*rows, s_rows);
    }

    *cols = list_create(9);
    for (int i = 1; i < 10; i++)
    {
        PtrList* s_cols = list_create(9);
        for (int j = 1; j < 10; j++)
        {
            Coordinate* c = malloc(sizeof(Coordinate));
            c->row = i;
            c->col = j;
            list_append(s_cols, c);
        }
        list_append(*cols, s_cols);
    }

    *boxes = list_create(9);
    int box_rows[] = { 1, 4, 7 };
    int box_cols[] = { 1, 4, 7 };
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            PtrList* box = get_box(box_rows[i], box_cols[j]);
            list_append(*boxes, box);
        }
    }

    *pcf_boxes = list_create(2);
    list_append(*pcf_boxes, get_box(2, 2));
    list_append(*pcf_boxes, get_box(6, 6));

    *pcf_centers = list_create(2);
    Coordinate* center1 = malloc(sizeof(Coordinate));
    center1->row = 3; center1->col = 3;
    Coordinate* center2 = malloc(sizeof(Coordinate));
    center2->row = 7; center2->col = 7;
    list_append(*pcf_centers, center1);
    list_append(*pcf_centers, center2);

    *cross_line = list_create(1);
    PtrList* s_cross_line = list_create(9);
    for (int r = 1; r <= 9; r++) 
    {
        Coordinate* c = malloc(sizeof(Coordinate));
        c->row = r;
        c->col = 10 - r;
        list_append(s_cross_line, c);
    }
    list_append(*cross_line, s_cross_line);
}
