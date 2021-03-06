#!/usr/bin/env python

import time



def add_node(tree_dic,comment):
    if comment.parent_comment is  None:
        tree_dic[comment] = {}
    else:
        for k,v in tree_dic.items():
            if k == comment.parent_comment:
                tree_dic[comment.parent_comment][comment] = {}
            else:
                add_node(v,comment)

def render_tree_node(tree_dic,margin_val):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='comment-node' style='margin-left:%spx'>" % margin_val + k.comment  + "<span style='margin-left:20px'>%s </span>"%k.date.fromtimestamp(time.time())    + \
                "<span style='margin-left:20px'>%s</span>" %k.user.name +"</div>"
        html += ele
        html += render_tree_node(v,margin_val+16)
    return html

def render_comment_tree(tree_dic):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='root-comment'>" + k.comment + "<span style='margin-left:20px'>%s </span>"%k.date \
              + "<span style='margin-left:20px'>%s</span>" %k.user.name +"</div>"
        html += ele
        html += render_tree_node(v,10)
    return html

def build_tree(comment_set):
    #print(comment_set)
    tree_dic = {}
    for comment in comment_set:
        add_node(tree_dic,comment)

    for k,v in tree_dic.items():
        print(k,v)
        return tree_dic





