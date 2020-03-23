#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import tellurium as te


class StochasticComplexSystem(object):

    def evolve(self):
        """Evolve the system.
        """
        raise NotImplementedError

    def plot(self):
        """Plot the evolution of the system.
        """
        raise NotImplementedError


class EnzymeKineticsModel(StochasticComplexSystem):

    def __init__(self):
        import os
        path = 'complex_systems/models/enzyme_kinetics.txt'
        self.rr = te.loada(os.path.abspath(path))
        self.rr.integrator = 'gillespie'

    def evolve(self, start=0, end=1000, outputs=100):
        self.rr.simulate(start, end, outputs)

    def plot(self):
        self.rr.plot()
