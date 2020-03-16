#!/usr/bin/env python2
import matplotlib.pyplot as plt
import roadrunner

class StochasticComplexSystem(object):

    def evolve(self):
        """Evolve the system.
        """
        raise NotImplementedError

    def plot(self):
        """Plot the evolution of the system.
        """
        raise NotImplementedError