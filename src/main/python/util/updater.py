import util.globales as g

def update_new_tab(val):
    g.new_tab = val

def update_driver(d):
    g.driver = d

def update_tab_num(n):
    g.tab_num = n

def update_login(l):
    g.login = l

def update_driver_path(d):
    g.driver_path = d

def get_new_tab():
    return g.new_tab

def get_driver():
    return g.driver

def get_tab_num():
    return g.tab_num

def get_login():
    return g.login

def get_driver_path():
    return g.driver_path