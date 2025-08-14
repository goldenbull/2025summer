#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#include "list.h"
#include "dict.h"
#include "sudoku.h"
#include "create_sudoku.h"

//��ӡ����
void print_board(PtrList* sudoku)
{
	printf("=====================\n");
	for (int i = 0; i < 9; i++)
	{
		if (i % 3 == 0 && i != 0)
		{
			printf("---------------------\n");
		}

		for (int j = 0; j < 9; j++)
		{
			int v;
			sudoku_get_int(sudoku, i, j, &v);

			if (j % 3 == 0 && j != 0)
				printf("| ");

			if (j == 8)
			{
				if (v == 0)
					printf(".\n");
				else
					printf("%d\n", v);
			}
			else
			{
				if (v == 0)
					printf(". ");
				else
					printf("%d ", v);
			}
		}
	}
	printf("=====================\n");
}


//�жϣ�row,col)���������Ƿ���Ч,��Ӧ����λ��sudoku[row-1][col-1]
bool is_valid(PtrList* sudoku, int row, int col, int value)
{
	//�����Լ��
	for (int i = 0; i < 9; i++)
	{
		int v;
		sudoku_get_int(sudoku, row - 1, i, &v);
		if (v == value)
			return false;
	}

	//�����Լ��
	for (int j = 0; j < 9; j++)
	{
		int v;
		sudoku_get_int(sudoku, j, col - 1, &v);
		if (v == value)
			return false;
	}

	//���Ź���Լ��
	int x = 3 * ((row - 1) / 3);
	int y = 3 * ((col - 1) / 3);
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			int v;
			sudoku_get_int(sudoku, x + i, y + j, &v);
			if (v == value)
				return false;
		}
	}

	//���ٷֺ�Լ��
	extern PtrList* pcf_centers;
	for (int k = 0; k < pcf_centers->size; k++)
	{
		Coordinate* coord;
		list_get(pcf_centers, k, &coord);
		int center_r, center_c;
		center_r = coord->row;
		center_c = coord->col;
		if (abs(row - center_r) <= 1 && abs(col - center_c) <= 1)
		{
			for (int i = center_r - 1; i < center_r + 2; i++)
			{
				for (int j = center_c - 1; j < center_c + 2; j++)
				{
					int v;
					sudoku_get_int(sudoku, i - 1, j - 1, &v);
					if (v == value)
						return false;
				}
			}
		}
	}

	//���Խ���Լ��
	if (row + col == 10)
	{
		for (int i = 0; i < 9; i++)
		{
			int v;
			sudoku_get_int(sudoku, i, 8 - i, &v);
			if (v == value)
				return false;
		}
	}

	return true;
}


//���ݷ�������
bool solve_sudoku(PtrList* sudoku)
{
	for (int row = 1; row < 10; row++)
	{
		for (int col = 1; col < 10; col++)
		{
			int v;
			sudoku_get_int(sudoku, row - 1, col - 1, &v);

			if (v == 0)
			{
				//����������е�����
				PtrList* numbers = list_create(9);
				for (int k = 1; k < 10; k++)
					list_append_int(numbers, k);
				list_random_shuffle(numbers);

				//����������֣��ж��Ƿ�����
				for (int i = 0; i < numbers->size; i++)
				{
					int value;
					list_get_int(numbers, i, &value);
					if (is_valid(sudoku, row, col, value))
					{
						sudoku_set_int(sudoku, row - 1, col - 1, value);
						if (solve_sudoku(sudoku))
						{
							list_destroy(numbers, NULL);
							return true;
						}
						else
							sudoku_set_int(sudoku, row - 1, col - 1, 0);
					}
				}

				list_destroy(numbers, NULL);
				return false;
			}
		}
	}
	return true;
}


//����һ����������
PtrList* complete_sudoku(void)
{
	//��ʼ����������
	PtrList* sudoku = list_create(9);
	for (int i = 0; i < 9; i++)
	{
		PtrList* sudoku_row = list_create(9);
		for (int j = 0; j < 9; j++)
			list_append_int(sudoku_row, 0);
		list_append(sudoku, sudoku_row);
	}

	//������
	solve_sudoku(sudoku);
	return sudoku;
}


//�ڶ�
void dig_holes(PtrList* sudoku, int holes)
{
	PtrList* cells = list_create(81);
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			Coordinate* coord1 = malloc(sizeof(Coordinate));
			coord1->row = i;
			coord1->col = j;
			list_append(cells, coord1);
		}
	}

	//����ڶ�
	list_random_shuffle(cells);
	for (int i = 0; i < holes; i++)
	{
		Coordinate* coord;
		list_get(cells, i, &coord);
		int r = coord->row;
		int c = coord->col;
		sudoku_set_int(sudoku, r, c, 0);
	}
}


//�����ڶ��������
PtrList* create_puzzle()
{
	PtrList* my_sudoku = complete_sudoku();

	//�����30-50����
	int holes_num = rand() % (50 - 30 + 1) + 30;
	dig_holes(my_sudoku, holes_num);

	printf("Randomly initialize the Sudoku game layout:\n\n");
	print_board(my_sudoku);
	return my_sudoku;
}


//���������ļ�
void create_sudoku_txt(PtrList* my_sudoku)
{
	// ���ļ�
	FILE* fout = fopen("my_sudoku.txt", "wt");

	// д�ļ�
	PtrList* sudoku_list = list_create(81);
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			int v;
			sudoku_get_int(my_sudoku, i, j, &v);
			if (v == 0)
			{
				fprintf(fout, ".");
			}
			else
			{
				fprintf(fout, "%d", v);
			}
		}
	}

	fprintf(fout, "\n");
	fclose(fout);
}