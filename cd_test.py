# -*- coding: utf-8 -*-
"""Contract Dict^2 tests."""

import time
from functools import wraps
import UnionFindA
# from graph import ERGraph, BAGraph
from contractdict import ContractDict2


def fn_timer(function):
    """Calculate the running time."""
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("{0:7.3f} ".format(t1-t0), end='')
        return result
    return function_timer


def run_in_pieces(graph, size, pieces, output_file):
    """Clustering of the graph in one and in pieces."""
    # we are interested of the clustering of the SAME graph
    # with different methods
    output_file.write("{0:4.2f}".format(graph.q_rate()))
    # in one
    uf = UnionFindA.UnionFind(size)
    c = ContractDict2(size, graph)
    c.contract(uf, 0, size)
    output_file.write(" {0:6d}".format(graph.conflicts(uf)))

    c.correct(uf, 0, size)
    output_file.write(" {0:6d}".format(graph.conflicts(uf)))

    # in pieces
    uf2 = UnionFindA.UnionFind(size)
    c2 = ContractDict2(size, graph)

    c2.contract_in_pieces(uf2, pieces)
    output_file.write(" {0:6d}".format(graph.conflicts(uf2)))

    c2.correct_in_pieces(uf2, pieces)
    output_file.write(" {0:6d}".format(graph.conflicts(uf2)))

    c2.contract(uf2, 0, size)
    output_file.write(" {0:6d}".format(graph.conflicts(uf2)))

    c2.correct(uf2, 0, size)
    output_file.write(" {0:6d}\n".format(graph.conflicts(uf2)))


def run_recursive(graph, size, limit, output_file):
    """The clustering of the graph in one and in recursively."""
    output_file.write("{0:4.2f}".format(graph.q_rate()))
    # in one
    uf = UnionFindA.UnionFind(size)
    c = ContractDict2(size, graph)
    c.contract(uf, 0, size)
    output_file.write("{0:6d}".format(graph.conflicts(uf)))

    c.correct(uf, 0, size)
    output_file.write(" {0:6d}".format(graph.conflicts(uf)))

    # rekursively, including the correction
    uf2 = UnionFindA.UnionFind(size)
    c2 = ContractDict2(size, graph)

    c2.recursive_contract(uf2, limit, 0, size)
    output_file.write(" {0:6d}".format(graph.conflicts(uf2)))


def run_old(graph, size):
    """Clustering in one."""
    uf = UnionFindA.UnionFind(size)
    c = ContractDict2(size, graph)
    c.contract(uf, 0, size)
    c.correct(uf, 0, size)


def run_piece(graph, size, pieces):
    """Clustering in parts."""
    uf2 = UnionFindA.UnionFind(size)
    c2 = ContractDict2(size, graph)
    c2.contract_in_pieces(uf2, pieces)
    c2.correct_in_pieces(uf2, pieces)

    c2.contract(uf2, 0, size)
    c2.correct(uf2, 0, size)


def run_rec(graph, size, limit):
    """Clustering recursively."""
    uf2 = UnionFindA.UnionFind(size)
    c2 = ContractDict2(size, graph)
    c2.recursive_contract(uf2, limit, 0, size)


def test_pieces(graph, size, pieces, output_file, steps=100):
    """Compare clustering by breaking into parts."""
    edges = graph.number_of_edges()//steps
    for i in range(steps+1):
        run_in_pieces(graph, size, pieces, output_file)
        graph.recolor(edges)
    run_in_pieces(graph, size, pieces, output_file)


def test_recursive(graph, size, limit, output_file, steps=100):
    """Compare clustering by recursion."""
    edges = graph.number_of_edges()//steps
    for i in range(steps+1):
        run_recursive(graph, size, limit, output_file)
        graph.recolor(edges)
    run_recursive(graph, size, limit, output_file)


@fn_timer
def speed_old(graph, size, steps=100):
    """Speed test of old."""
    edges = graph.number_of_edges()//steps
    for i in range(steps+1):
        run_old(graph, size)
        graph.recolor(edges)
    run_old(graph, size)


@fn_timer
def speed_piece(graph, size, pieces, steps=100):
    """Speed test of parts."""
    edges = graph.number_of_edges()//steps
    for i in range(steps+1):
        run_piece(graph, size, pieces)
        graph.recolor(edges)
    run_piece(graph, size, pieces)


@fn_timer
def speed_rec(graph, size, limit, steps=100):
    """Speed test of parts."""
    edges = graph.number_of_edges()//steps
    for i in range(steps+1):
        run_rec(graph, size, limit)
        graph.recolor(edges)
    run_rec(graph, size, limit)
