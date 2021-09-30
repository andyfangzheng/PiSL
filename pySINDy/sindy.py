"""
Derived module from sindybase.py for classical SINDy
"""
import numpy as np
from findiff import FinDiff
from .sindybase import SINDyBase


class SINDy(SINDyBase):
    """
    Sparse Identification of Nonlinear Dynamics:
    reference: http://www.pnas.org/content/pnas/113/15/3932.full.pdf
    """
    def fit(self, data, _dt, poly_degree=2, cut_off=1e-3, deriv_acc=2):
        """
        :param data: dynamics data to be processed
        :param _dt: float, represents grid spacing
        :param poly_degree: degree of polynomials to be included in theta matrix
        :param cut_off: the threshold cutoff value for sparsity
        :param deriv_acc: (positive) integer, derivative accuracy
        :return: a SINDy model
        """
        if len(data.shape) == 1:
            data = data[np.newaxis, ]

        len_t = data.shape[-1]

        if len(data.shape) > 2:
            data = data.reshape((-1, len_t))
            print("The array is converted to 2D automatically: in SINDy, "
                  "each dimension except for the time (default the last dimension) "
                  "are treated equally.")

        # compute time derivative
        d_dt = FinDiff(data.ndim-1, _dt, 1, acc=deriv_acc)
        x_dot = d_dt(data).T

        # prepare for the library
        lib, self._desp = self.polynomial_expansion(data.T, degree=poly_degree)

        # sparse regression
        self._coef, _ = self.sparsify_dynamics(lib, x_dot, cut_off)

        return self
