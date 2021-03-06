from OWDTestToolkit.global_imports import *

import  createEvent         ,\
        getEventPreview     ,\
        setView             ,\
        moveDayViewBy       ,\
        moveWeekViewBy      ,\
        moveMonthViewBy     ,\
        changeDay

class Calendar (
            createEvent.main,
            getEventPreview.main,
            setView.main,
            moveDayViewBy.main,
            moveWeekViewBy.main,
            moveMonthViewBy.main,
            changeDay.main
            ):
    
    def __init__(self, p_parent):
        self.apps       = p_parent.apps
        self.data_layer = p_parent.data_layer
        self.parent     = p_parent
        self.marionette = p_parent.marionette
        self.UTILS      = p_parent.UTILS
        self.actions    = Actions(self.marionette)

    def launch(self):
        #
        # Launch the app.
        #
        self.app = self.apps.launch(self.__class__.__name__)
        self.UTILS.waitForNotElements(DOM.GLOBAL.loading_overlay, self.__class__.__name__ + " app - loading overlay")
        return self.app

