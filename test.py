#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import signal

from Qt import QtCore, QtWidgets

from NodeGraphQt import (
    NodeGraph,
    PropertiesBinWidget,
    NodesTreeWidget,
    NodesPaletteWidget,
    BaseNode,
    constants
)
import sys
# append a new directory to sys.path
sys.path.append(r'C:\Users\tranier\Documents\NodeGraphQt\NodeGraphQt')

class BasicNodeA(BaseNode):
    """
    A node class with 2 inputs and 2 outputs.
    """

    # unique node identifier.
    __identifier__ = 'nodes.basic'

    # initial default node name.
    NODE_NAME = 'node A'

    def __init__(self):
        super(BasicNodeA, self).__init__()

        # create node inputs.
        self.add_input('in A')
        self.add_input('in B')

        # create node outputs.
        self.add_output('out A')
        self.add_output('out B')



if __name__ == '__main__':


    
    app = QtWidgets.QApplication([])

    # create graph controller.
    graph = NodeGraph()
    graph.set_pipe_style(constants.PipeLayoutEnum.ANGLE.value)
    graph.set_acyclic(True)

    # registered example nodes.
    graph.register_nodes([
        BasicNodeA
    ])

    
    # show the node graph widget.
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.show()

    def action(node):
        node.output_ports()[0].disconnect_from()

     # create node with custom text color and disable it.
    n_basic_a = graph.create_node(
        'nodes.basic.BasicNodeA', text_color='#feab20')
    
     # create node with custom text color and disable it.
    n_basic_b = graph.create_node(
        'nodes.basic.BasicNodeA', text_color='#feab20')
    
    graph.node_double_clicked.connect(action)

    
    app.exec_()
