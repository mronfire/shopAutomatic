import util.globales as g
# import sys, os

# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.dirname(__file__)
#     return os.path.join(base_path, relative_path)

def update_new_tab(val):
    g.new_tab = val

def update_driver(d):
    g.driver = d

def update_tab_num(n):
    g.tab_num = n

def get_new_tab():
    return g.new_tab

def get_driver():
    return g.driver

def get_tab_num():
    return g.tab_num