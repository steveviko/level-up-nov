class check_order_status:

    def __init__(self):
        self.order_details = dict()


    def add(self,id,status):
        self.order_details[id] = status 
    
    def order_status(self,number):
        """Return True if *number and not 0* is status."""
        # for element in range(number):
        if number ==0:
            return False

        return True

    def order_id_type(self, id):
        number_types = (int, float, complex)
 
        if isinstance(id, number_types):
            return id 
        else:
            raise ValueError