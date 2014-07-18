# Copyright (c) 2014 Novo Nordisk Foundation Center for Biosustainability, DTU.
# See LICENSE for details.

import unittest

import os
import cobra
import optlang

from cameo.io import load_model
from cameo.solver_based_model import SolverBasedModel


TESTDIR = os.path.dirname(__file__)


class TestModelLoading(unittest.TestCase):
    def test_load_model_pickle_path(self):
        model = load_model(os.path.join(TESTDIR, 'data/iJO1366.pickle'))
        self.assertAlmostEqual(model.optimize().f, 0.9823718127269768)

    def test_load_model_pickle_handle(self):
        with open(os.path.join(TESTDIR, 'data/iJO1366.pickle')) as handle:
            model = load_model(handle)
        self.assertAlmostEqual(model.optimize().f, 0.9823718127269768)

    def test_load_model_sbml_path(self):
        model = load_model(os.path.join(TESTDIR, 'data/iJO1366.xml'))
        self.assertAlmostEqual(model.optimize().f, 0.9823718127269768)

    def test_load_model_sbml_handle(self):
        with open(os.path.join(TESTDIR, 'data/iJO1366.xml')) as handle:
            model = load_model(handle)
        self.assertAlmostEqual(model.optimize().f, 0.9823718127269768)

    def test_load_model_sbml_path_set_cplex_interface(self):
        model = load_model(os.path.join(TESTDIR, 'data/EcoliCore.xml'), solver_interface='cplex')
        self.assertAlmostEqual(model.optimize().f, 0.8739215069684306)
        self.assertTrue(isinstance(model, SolverBasedModel))
        self.assertTrue(isinstance(model.solver, optlang.cplex_interface.Model))

    def test_load_model_sbml_path_set_None_interface(self):
        model = load_model(os.path.join(TESTDIR, 'data/EcoliCore.xml'), solver_interface=None)
        self.assertAlmostEqual(model.optimize().f, 0.8739215069684306)
        self.assertTrue(isinstance(model, cobra.core.Model))
        self.assertFalse(hasattr(model, 'solver'))

if __name__ == '__main__':
    import nose
    nose.runmodule()