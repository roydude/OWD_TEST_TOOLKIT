from OWDTestToolkit.global_imports import *

class main(GaiaTestCase):

    def replaceStr(self, p_field, p_str):
        #
        # Replace text in a field (as opposed to just appending to it).
        #
        p_field.clear()
        p_field.send_keys(p_str)
        
        x = self.marionette.find_element("tag name", "h1")
        x.tap()
        
        self.checkMatch(p_field, p_str, "After replacing the string, this field now")
