import xlrd
from xlutils.copy import copy
class   Operate_excel(object):

    def Open_table(self,table):
        excel = xlrd.open_workbook(table)
        return excel
    def  Get_row_count(self,table,sheet_index):
      excel = Operate_excel().Open_table(table)
      BS = excel.sheet_by_index(sheet_index)
      num_rows = BS .nrows
      return num_rows
    def  Get_table_sheet_name(self,table,sheet_index):
      excel = Operate_excel().Open_table(table)
      BS = excel.sheet_by_index(sheet_index)
      return BS

    def Show_table_one_detatil(self,table,sheet_index,j,k):#获得指定单元格的数值
       excel=Operate_excel().Open_table(table)
       BS = excel.sheet_by_index(sheet_index)
       cell =BS.cell_value(j, k)

       return  cell
    def  Show_table_row_detail(self,table,sheet_index):
      excel = Operate_excel().Open_table(table)
      BS = excel.sheet_by_index(sheet_index)
      num_rows = BS.nrows
      for  j  in range(num_rows):
            row= BS.row_values(j)
            print(row)
    def  Show_table_col_detail(self,table,sheet_index,j):#j值为想获得列值
       excel = Operate_excel().Open_table(table)
       BS = excel.sheet_by_index(sheet_index)
       num_cols=BS.nrows
       print(num_cols)
       arr1 = []
       for  i in range(num_cols):

           if  i >0:

             BS.cell_value(i,j)

             BS.cell_value(i, j)
             arr1.append(BS.cell_value(i, j))

           else:
               pass
       return arr1




    def copy_table(self,table):
        excel = xlrd.open_workbook(table)
        wb = copy(excel)

        return wb
    def  Get_sheet(self,wb,sheet_index):
        ws = wb.get_sheet(sheet_index)
        return ws
    def close_table(self,w):
        w.save('D:\\test.xls')

if __name__ == "__main__":
   local_table='C:\\Users\\Administrator\\Desktop\\test\\table\\test.xlsx'
   h=Operate_excel()
   h.Show_table_one_detatil(local_table,0,1,1)
   h.Show_table_row_detail(local_table,0)