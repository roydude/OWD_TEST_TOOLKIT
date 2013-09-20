frame_locator           = ('src', 'browser')
browser_page_frame      = ('mozbrowser', "")
url_input               = ('id', 'url-input')
url_go_button           = ('id', 'url-button')
throbber                = ("xpath", "//*[@id='throbber' and @class='loading']")

search_result_links     = ("xpath", "//div[@id='search']//a")

open_in_new_tab_button  = ("xpath", "//button[contains(text(), 'Open link in new tab')]")
new_tab_screen          = ("id", "startscreen")

tab_screen              = ("id", "main-screen")
tab_tray_close_btn      = ("id", "awesomescreen-cancel-button")

tab_tray_counter        = ("id", "tabs-badge")
tab_tray_open           = ("id", "more-tabs")
tab_tray_new_tab_btn    = ("id", "new-tab-button")
tab_tray_settings_btn   = ("id", "settings-button")
tab_tray_screen         = ("class name", "tabs-screen")
tab_tray_new_tab_btn    = ("id", "new-tab-button")
tab_tray_tab_panels     = ("xpath", "//div[@id='tab-panels']//li/a")
tab_tray_tab_list       = ("xpath", "//div[@id='tabs-list']//li/a")
tab_tray_tab_list_curr  = ("xpath", "//div[@id='tabs-list']//li[@class='current']/a")

tab_tray_tab_item_close = ("tag name", "button") # Use these with :
tab_tray_tab_item_image = ("tag name", "div")    #   x = getElement(...tab_tray_tab_list)[0]
tab_tray_tab_item_title = ("tag name", "span")   #   y = x.find_element(<these>)


settings_button         = ("id", "settings-button")
settings_header         = ("xpath", "//header[@id='settings-header']")

website_frame           = ("class", "browser-tab")
page_title              = ('xpath', ".//*[@id='results']/ul//h5[text()='Problemloadingpage']")
page_problem            = ("xpath", "//*[text()='Problem loading page']")
