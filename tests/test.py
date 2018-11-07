import unittest
from order_verify import check_order_status


class TestsOrder(unittest.TestCase):

    def setUp(self):
        self.check_order =check_order_status()
        self.sample_orders = dict(
            id = 1,
            status = 200
               
        )
    def test_check_order_status_creation(self):        
        self.assertIsInstance(self.check_order, check_order_status)

    def test_order_status(self):        
        self.status =self.check_order.order_status(2)
        self.assertEqual(self.status,True)
    
    def test_status_fail(self):       
        self.status =self.check_order.order_status(0)
        self.assertFalse(self.status)

    def test_order_id_type_input_returns_interger(self):
       self.num =self.check_order.order_id_type(2)
       self.assertIsInstance(self.num, int)

    def test_add_order_method(self):
        self.assertEqual(len(self.check_order.order_details),0)  
        self.check_order.add(**self.sample_orders)
        self.assertEqual(len(self.check_order.order_details),1)


    



if __name__ == '__main__':
    unittest.main()