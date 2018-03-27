import  unittest
import  requests
from  operateExcel import Operate_excel
from   get_cookies import  Get_cookies
L=Get_cookies()
K =Operate_excel()
class  Test_statue(unittest.TestCase):
     def setUp(self):
        self.local_table ='C:\\Users\\Administrator\\Desktop\\test\\table\\test.xlsx'


     def tearDown(self):
      pass
     def  test_login(self):
         row=K.Show_table_one_detatil( self.local_table,0,1,0)
         row1=K.Show_table_one_detatil( self.local_table,0,1,1)
         row2= K.Show_table_one_detatil( self.local_table,0,1,2)
         url = K.Show_table_one_detatil( self.local_table,0,1,3)
         payload = {'user': , 'pwdd': ,}#根据实际情况传参
         cook=L.test_have_cookies( url,payload)#得到cook用于下面的接口测试
         print("我是cookies")
         return cook
     def  test_interface(self):
          lisl=K.Show_table_col_detail(self.local_table,1,0)
          list2=K.Show_table_col_detail(self.local_table,1,1)
          list3=K.Show_table_col_detail(self.local_table,1,2)#得到预期的返回
          rows=K.Get_row_count(self.local_table,1)
          self.t = K.copy_table(self.local_table)
          self.j = K.Get_sheet(self.t, 1)
          for i in range(rows):#根据数组下标相同来拼装链接
            if i<rows-1:
               print(lisl[i])
               r=requests.get(list2[i],params=eval(lisl[i]),cookies=Test_statue.test_login(self))
               print(r.text)
               print(r.status_code)

               l=self.assertEqual(r.status_code,int(list3[i]))
               if None == l:

                     i+= 1

                     self.j.write(i, 3, 'success')
                     i-= 1

               else:
                    i += 1

                    self.j.write(i, 3, 'fail')
                    i -= 1
            else:
                 pass
            K.close_table(self.t)


if __name__ == "__main__":
    unittest.main()

