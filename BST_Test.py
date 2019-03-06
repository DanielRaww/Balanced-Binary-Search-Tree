import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
   
   def setUp(self):
      self.__tree = Binary_Search_Tree()
      
   def test_blank_tree(self):
      self.assertEqual('[ ]', str(self.__tree))
      self.assertEqual('[ ]', self.__tree.post_order())
      self.assertEqual('[ ]', self.__tree.pre_order())
      self.assertEqual([], self.__tree.to_list())
      self.assertEqual(0, self.__tree.get_height())
      
   def get_height_blank_tree(self):
      self.assertEqual('[ ]', str(self.__tree))
      self.assertEqual([], self.__tree.to_list())
      self.assertEqual(0, self.__tree.get_height())
      
   def test_removal_blank_tree(self):
      self.__tree.insert_element(7)
      self.__tree.remove_element(7)
      self.assertEqual('[ ]', str(self.__tree))
      self.assertEqual('[ ]', self.__tree.post_order())
      self.assertEqual('[ ]', self.__tree.pre_order())
      self.assertEqual([], self.__tree.to_list())
      self.assertEqual(0, self.__tree.get_height())
      
   def test_removal_string_blank_tree(self):
      self.__tree.insert_element('help')
      self.__tree.remove_element('help')
      self.assertEqual('[ ]', str(self.__tree))
      self.assertEqual('[ ]', self.__tree.post_order())
      self.assertEqual('[ ]', self.__tree.pre_order())
      self.assertEqual([], self.__tree.to_list())
      self.assertEqual(0, self.__tree.get_height())
      
   def test_insert_string(self):
      self.__tree.insert_element('hi')
      self.assertEqual('[ hi ]', str(self.__tree))
      
   def test_insert_two_string(self):
      self.__tree.insert_element('chocolate')
      self.__tree.insert_element('milk')
      self.assertEqual('[ chocolate, milk ]', str(self.__tree))
      
   def test_insert_one_element_tree(self):
      self.__tree.insert_element(0)
      self.assertEqual('[ 0 ]', str(self.__tree))
      self.assertEqual('[ 0 ]', self.__tree.post_order())
      self.assertEqual('[ 0 ]', self.__tree.pre_order())
      self.assertEqual([0], self.__tree.to_list())
      self.assertEqual(1 , self.__tree.get_height())
      
   def one_element_get_height_tree(self):
      self.__tree.insert_element(0)
      self.assertEqual('[ 0 ]', str(self.__tree))
      self.assertEqual([0], self.__tree.to_list())
      self.assertEqual(1, self.__tree.get_height())
      
   def test_remove_blank_tree(self):
      with (self.assertRaises(ValueError)):
         self.__tree.remove_element(13)
      self.assertEqual('[ ]', str(self.__tree))
      self.assertEqual('[ ]', self.__tree.pre_order())
      self.assertEqual('[ ]', self.__tree.post_order())
      self.assertEqual(0, self.__tree.get_height())
      self.assertEqual([], self.__tree.to_list())
      
   def test_remove_not_present_value(self):
      with (self.assertRaises(ValueError)):
         self.__tree.insert_element(4)
         self.__tree.remove_element(11)
      self.assertEqual('[ 4 ]', str(self.__tree))
      self.assertEqual('[ 4 ]', self.__tree.pre_order())
      self.assertEqual('[ 4 ]', self.__tree.post_order())
      self.assertEqual(1, self.__tree.get_height())
      self.assertEqual([4], self.__tree.to_list())
      
   def test_insert_two_elements(self):
      self.__tree.insert_element(0)
      self.__tree.insert_element(1)
      self.assertEqual('[ 0, 1 ]', str(self.__tree))
      self.assertEqual('[ 1, 0 ]', self.__tree.post_order())
      self.assertEqual('[ 0, 1 ]', self.__tree.pre_order())
      self.assertEqual([0, 1], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_balance_three_elements(self):
      self.__tree.insert_element(11)
      self.__tree.insert_element(5)
      self.__tree.insert_element(14)
      self.assertEqual('[ 5, 11, 14 ]', str(self.__tree))
      self.assertEqual('[ 5, 14, 11 ]', self.__tree.post_order())
      self.assertEqual('[ 11, 5, 14 ]', self.__tree.pre_order())
      self.assertEqual([5, 11, 14], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_rotate_right_three_elements(self):
      self.__tree.insert_element(7)
      self.__tree.insert_element(10)
      self.__tree.insert_element(18)
      self.assertEqual('[ 7, 10, 18 ]', str(self.__tree))
      self.assertEqual('[ 7, 18, 10 ]', self.__tree.post_order())
      self.assertEqual('[ 10, 7, 18 ]', self.__tree.pre_order())
      self.assertEqual([7, 10, 18], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_rotate_left_three_elements(self):
      self.__tree.insert_element(9)
      self.__tree.insert_element(7)
      self.__tree.insert_element(4)
      self.assertEqual('[ 4, 7, 9 ]', str(self.__tree))
      self.assertEqual('[ 4, 9, 7 ]', self.__tree.post_order())
      self.assertEqual('[ 7, 4, 9 ]', self.__tree.pre_order())
      self.assertEqual([4, 7, 9], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_rotate_left_four_elements(self):
      self.__tree.insert_element(13)
      self.__tree.insert_element(9)
      self.__tree.insert_element(7)
      self.__tree.insert_element(20)
      self.assertEqual('[ 7, 9, 13, 20 ]', str(self.__tree))
      self.assertEqual('[ 7, 20, 13, 9 ]', self.__tree.post_order())
      self.assertEqual('[ 9, 7, 13, 20 ]', self.__tree.pre_order())
      self.assertEqual([7, 9, 13, 20], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      
   def test_rotate_right_four_elements(self):
      self.__tree.insert_element(8)
      self.__tree.insert_element(15)
      self.__tree.insert_element(17)
      self.__tree.insert_element(2)
      self.assertEqual('[ 2, 8, 15, 17 ]', str(self.__tree))
      self.assertEqual('[ 2, 8, 17, 15 ]', self.__tree.post_order())
      self.assertEqual('[ 15, 8, 2, 17 ]', self.__tree.pre_order())
      self.assertEqual([2, 8, 15, 17], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      
   def test_double_rotate_five_elements(self):
      self.__tree.insert_element(11)
      self.__tree.insert_element(6)
      self.__tree.insert_element(16)
      self.__tree.insert_element(21)
      self.__tree.insert_element(19)
      self.assertEqual('[ 6, 11, 16, 19, 21 ]', str(self.__tree))
      self.assertEqual('[ 6, 16, 21, 19, 11 ]', self.__tree.post_order())
      self.assertEqual('[ 11, 6, 19, 16, 21 ]', self.__tree.pre_order())
      self.assertEqual([6,11,16,19,21], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      
   def test2_double_rotate_five_elements(self):
      self.__tree.insert_element(11)
      self.__tree.insert_element(9)
      self.__tree.insert_element(16)
      self.__tree.insert_element(6)
      self.__tree.insert_element(8)
      self.assertEqual('[ 6, 8, 9, 11, 16 ]', str(self.__tree))
      self.assertEqual('[ 6, 9, 8, 16, 11 ]', self.__tree.post_order())
      self.assertEqual('[ 11, 8, 6, 9, 16 ]', self.__tree.pre_order())
      self.assertEqual([6,8,9,11,16], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      
   def test_remove_one_element_tree(self):
      self.__tree.insert_element(12)
      self.__tree.remove_element(12)
      self.assertEqual('[ ]', str(self.__tree))
      self.assertEqual('[ ]', self.__tree.post_order())
      self.assertEqual('[ ]', self.__tree.pre_order())
      self.assertEqual([], self.__tree.to_list())
      self.assertEqual(0, self.__tree.get_height())
      
   def test_remove_root_two_element_tree(self):
      self.__tree.insert_element(12)
      self.__tree.insert_element(3)
      self.__tree.remove_element(12)
      self.assertEqual('[ 3 ]', str(self.__tree))
      self.assertEqual('[ 3 ]', self.__tree.post_order())
      self.assertEqual('[ 3 ]', self.__tree.pre_order())
      self.assertEqual([3], self.__tree.to_list())
      self.assertEqual(1, self.__tree.get_height())
      
   def test_remove_leaf_two_element_tree(self):
      self.__tree.insert_element(11)
      self.__tree.insert_element(8)
      self.__tree.remove_element(8)
      self.assertEqual('[ 11 ]', str(self.__tree))
      self.assertEqual('[ 11 ]', self.__tree.post_order())
      self.assertEqual('[ 11 ]', self.__tree.pre_order())
      self.assertEqual([11], self.__tree.to_list())
      self.assertEqual(1, self.__tree.get_height())
      
   def test_balance_remove_three_element_tree(self):
      self.__tree.insert_element(14)
      self.__tree.insert_element(12)
      self.__tree.insert_element(15)
      self.__tree.remove_element(15)
      self.assertEqual('[ 12, 14 ]', str(self.__tree))
      self.assertEqual('[ 12, 14 ]', self.__tree.post_order())
      self.assertEqual('[ 14, 12 ]', self.__tree.pre_order())
      self.assertEqual([12,14], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_balance_remove_root_three_element_tree(self):
      self.__tree.insert_element(10)
      self.__tree.insert_element(4)
      self.__tree.insert_element(15)
      self.__tree.remove_element(10)
      self.assertEqual('[ 4, 15 ]', str(self.__tree))
      self.assertEqual('[ 4, 15 ]', self.__tree.post_order())
      self.assertEqual('[ 15, 4 ]', self.__tree.pre_order())
      self.assertEqual([4,15], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_unbalanced_remove_old_root_two_element_tree(self):
      self.__tree.insert_element(10)
      self.__tree.insert_element(14)
      self.__tree.insert_element(19)
      self.__tree.remove_element(10)
      self.assertEqual('[ 14, 19 ]', str(self.__tree))
      self.assertEqual('[ 19, 14 ]', self.__tree.post_order())
      self.assertEqual('[ 14, 19 ]', self.__tree.pre_order())
      self.assertEqual([14,19], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_unbalanced_remove_new_root_three_element_tree(self):
      self.__tree.insert_element(10)
      self.__tree.insert_element(15)
      self.__tree.insert_element(20)
      #print(self.__tree.in_order())
      #print(self.__tree.pre_order())
      #print(self.__tree.post_order())
      self.__tree.remove_element(15)
      self.assertEqual('[ 10, 20 ]', str(self.__tree))
      self.assertEqual('[ 20, 10 ]', self.__tree.pre_order())
      self.assertEqual('[ 10, 20 ]', self.__tree.post_order())
      self.assertEqual([10,20], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_unbalanced_remove_lead_node_three_element_tree(self):
      self.__tree.insert_element(11)
      self.__tree.insert_element(15)
      self.__tree.insert_element(20)
      self.__tree.remove_element(15)
      self.assertEqual('[ 11, 20 ]', str(self.__tree))
      self.assertEqual('[ 11, 20 ]', self.__tree.post_order())
      self.assertEqual('[ 20, 11 ]', self.__tree.pre_order())
      self.assertEqual([11,20], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_remove_four_element_right_heavy(self):
      self.__tree.insert_element(12)
      self.__tree.insert_element(17)
      self.__tree.insert_element(22)
      self.__tree.insert_element(7)
      self.__tree.remove_element(17)
      self.assertEqual('[ 7, 12, 22 ]', str(self.__tree))
      self.assertEqual('[ 7, 22, 12 ]', self.__tree.post_order())
      self.assertEqual('[ 12, 7, 22 ]', self.__tree.pre_order())
      self.assertEqual([7, 12, 22], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_remove_four_element_left_heavy(self):
      self.__tree.insert_element(14)
      self.__tree.insert_element(19)
      self.__tree.insert_element(12)
      self.__tree.insert_element(5)
      self.__tree.remove_element(5)
      self.assertEqual('[ 12, 14, 19 ]', str(self.__tree))
      self.assertEqual('[ 12, 19, 14 ]', self.__tree.post_order())
      self.assertEqual('[ 14, 12, 19 ]', self.__tree.pre_order())
      self.assertEqual([12, 14, 19], self.__tree.to_list())
      self.assertEqual(2, self.__tree.get_height())
      
   def test_remove_five_element_double_rotate_right_heavy(self):
      self.__tree.insert_element(9)
      self.__tree.insert_element(3)
      self.__tree.insert_element(11)
      self.__tree.insert_element(19)
      self.__tree.insert_element(17)
      self.__tree.remove_element(11)
      self.assertEqual('[ 3, 9, 17, 19 ]', str(self.__tree))
      self.assertEqual('[ 3, 19, 17, 9 ]', self.__tree.post_order())
      self.assertEqual('[ 9, 3, 17, 19 ]', self.__tree.pre_order())
      self.assertEqual([3, 9, 17, 19], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      
   def test_remove_five_element_double_rotate_right_heavy(self):
      self.__tree.insert_element(11)
      self.__tree.insert_element(6)
      self.__tree.insert_element(16)
      self.__tree.insert_element(21)
      self.__tree.insert_element(19)
      self.__tree.remove_element(16)
      self.assertEqual('[ 6, 11, 19, 21 ]', str(self.__tree))
      self.assertEqual('[ 6, 21, 19, 11 ]', self.__tree.post_order())
      self.assertEqual('[ 11, 6, 19, 21 ]', self.__tree.pre_order())
      self.assertEqual([6, 11, 19, 21], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      
   def test_remove_five_element_double_rotate_left_heavy(self):
      self.__tree.insert_element(10)
      self.__tree.insert_element(8)
      self.__tree.insert_element(15)
      self.__tree.insert_element(5)
      self.__tree.insert_element(7)
      self.__tree.remove_element(8)
      self.assertEqual('[ 5, 7, 10, 15 ]', str(self.__tree))
      self.assertEqual('[ 5, 7, 15, 10 ]', self.__tree.post_order())
      self.assertEqual('[ 10, 7, 5, 15 ]', self.__tree.pre_order())
      self.assertEqual([5, 7, 10, 15], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      
   def tet_insert_duplicate_value(self):
      with (self.assertRaises(ValueError)):
         self.__tree.insert_element(-5)
         self.__tree.insert_element(-5)
      self.assertEqual('[ -5 ]', str(self.__tree))
      self.assertEqual('[ -5 ]', self.__tree.pre_order())
      self.assertEqual('[ -5 ]', self.__tree.post_order())
      self.assertEqual(1, self.__tree.get_height())
      self.assertEqual([-5], self.__tree.to_list())
      
   def test_balanced_big_tree(self):
      self.__tree.insert_element(15)  
      self.__tree.insert_element(-8)
      self.__tree.insert_element(12)
      self.__tree.insert_element(14)
      self.__tree.insert_element(26)
      self.assertEqual('[ -8, 12, 14, 15, 26 ]', str(self.__tree))
      self.assertEqual('[ 12, -8, 15, 14, 26 ]', self.__tree.pre_order())
      self.assertEqual('[ -8, 14, 26, 15, 12 ]', self.__tree.post_order())
      self.assertEqual([-8, 12, 14, 15, 26], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      self.__tree.insert_element(-2)
      self.assertEqual(3, self.__tree.get_height())
      self.__tree.insert_element(0)
      self.assertEqual('[ -8, -2, 0, 12, 14, 15, 26 ]', str(self.__tree))
      self.assertEqual([-8, -2, 0, 12, 14, 15, 26], self.__tree.to_list())
      self.assertEqual(3, self.__tree.get_height())
      self.__tree.insert_element(18)
      self.assertEqual('[ -8, -2, 0, 12, 14, 15, 18, 26 ]', str(self.__tree))
      self.assertEqual([-8, -2, 0, 12, 14, 15, 18, 26 ], self.__tree.to_list())
      self.assertEqual(4, self.__tree.get_height())
       
      
if __name__ == '__main__':
   unittest.main()