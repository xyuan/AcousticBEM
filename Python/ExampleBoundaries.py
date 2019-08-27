# ---------------------------------------------------------------------------
# Copyright (C) 2017 Frank Jargstorff
#
# This file is part of the AcousticBEM library.
# AcousticBEM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AcousticBEM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AcousticBEM.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------------
import numpy as np
from Mesh import *

def square():
    chain = Chain(32, 32)
    chain.vertices = np.array([[0.00, 0.0000], [0.00, 0.0125], [0.00, 0.0250], [0.00, 0.0375],
                               [0.00, 0.0500], [0.00, 0.0625], [0.00, 0.0750], [0.00, 0.0875],

                               [0.0000, 0.10], [0.0125, 0.10], [0.0250, 0.10], [0.0375, 0.10],
                               [0.0500, 0.10], [0.0625, 0.10], [0.0750, 0.10], [0.0875, 0.10],

                               [0.10, 0.1000], [0.10, 0.0875], [0.10, 0.0750], [0.10, 0.0625],
                               [0.10, 0.0500], [0.10, 0.0375], [0.10, 0.0250], [0.10, 0.0125],

                               [0.1000, 0.00], [0.0875, 0.00], [0.0750, 0.00], [0.0625, 0.00],
                               [0.0500, 0.00], [0.0375, 0.00], [0.0250, 0.00], [0.0125, 0.00]],
                              dtype=np.float32)

    chain.edges = np.array([[0, 1], [1, 2], [2, 3], [3, 4],
                            [4, 5], [5, 6], [6, 7], [7, 8],

                            [8,  9],  [9,  10], [10, 11], [11, 12],
                            [12, 13], [13, 14], [14, 15], [15, 16],

                            [16, 17], [17, 18], [18, 19], [19, 20],
                            [20, 21], [21, 22], [22, 23], [23, 24],

                            [24, 25], [25, 26], [26, 27], [27, 28],
                            [28, 29], [29, 30], [30, 31], [31,  0]],
                           dtype=np.int32)
    return chain


# For RIM3T1 (Rayleigh Integral test program 1)
# This is the 2D "piston" or circular membrane lying in the
# plane {(x,y,z)|x = 1.0, y,z in R}
#
def disk_3d():
    mesh = Mesh(19, 25)
    mesh.vertices = np.array([[1.000, 0.000, 0.000],   [1.000, 0.025, 0.043],
                              [1.000, 0.050, 0.000],   [1.000,  0.025, -0.043],
                              [1.000, -0.025, -0.043], [1.000, -0.050, 0.000],
                              [1.000, -0.025,  0.043], [1.000,  0.050,  0.087],
                              [1.000,  0.087, 0.050],  [1.000,  0.100,  0.000],
                              [1.000,  0.087, -0.050], [1.000,  0.050, -0.087],
                              [1.000,  0.000, -0.100], [1.000, -0.050, -0.087],
                              [1.000, -0.087, -0.050], [1.000, -0.100,  0.000],
                              [1.000, -0.087,  0.050], [1.000, -0.050, 0.087],
                              [1.000,  0.000,  0.100]], dtype=np.float32)
    
    mesh.triangles = np.array([[0, 1, 6],   [0, 2, 1],   [0, 3, 2],   [0, 4, 3],
                               [0, 5,  4],  [0, 6,  5],  [7, 1,  8],  [8, 1,  2],
                               [8, 2,  9],  [9, 2, 10],  [10, 2,  3], [10, 3, 11],
                               [11, 3, 12], [12, 3,  4], [12, 4, 13], [13, 4, 14],
                               [14, 4,  5], [14, 5, 15], [15, 5, 16], [16, 5, 6],
                               [16, 6, 17], [17, 6, 18], [18, 7, 1],  [18, 1, 7]])
    return mesh


def square_3d():
    mesh = Mesh(25, 32)
    mesh.vertices = np.array([[0.000, 0.000, 0.000], [0.250, 0.000, 0.000],
                              [0.500, 0.000, 0.000], [0.750, 0.000, 0.000],
                              [1.000, 0.000, 0.000], [0.000, 0.250, 0.000],
                              [0.250, 0.250, 0.000], [0.500, 0.250, 0.000],
                              [0.750, 0.250, 0.000], [1.000, 0.250, 0.000],
                              [0.000, 0.500, 0.000], [0.250, 0.500, 0.000],
                              [0.500, 0.500, 0.000], [0.750, 0.500, 0.000],
                              [1.000, 0.500, 0.000], [0.000, 0.750, 0.000],
                              [0.250, 0.750, 0.000], [0.500, 0.750, 0.000],
                              [0.750, 0.750, 0.000], [1.000, 0.750, 0.000],
                              [0.000, 1.000, 0.000], [0.250, 1.000, 0.000],
                              [0.500, 1.000, 0.000], [0.750, 1.000, 0.000],
                              [1.000, 1.000, 0.000]])

    mesh.triangles = np.array([[0,   1,  5], [1,   6,  5], [1,   2,  7], [1,   7,  6],
                               [2,   3,  7], [3,   8,  7], [3,   4,  9], [3,   9,  8],
                               [5,   6, 11], [5,  11, 10], [6,   7, 11], [7,  12, 11],
                               [7,   8, 13], [7,  13, 12], [8,   9, 13], [9,  14, 13],
                               [10, 11, 15], [11, 16, 15], [11, 12, 17], [11, 17, 16],
                               [12, 13, 17], [13, 18, 17], [13, 14, 19], [13, 19, 18],
                               [15, 16, 21], [15, 21, 20], [16, 17, 21], [17, 22, 21],
                               [17, 18, 23], [17, 23, 22], [18, 19, 23], [19, 24, 23]])
    return mesh


def sphere_rad():
    oChain = Chain(19, 18)
    oChain.vertices = np.array([[0.000,  1.000], [0.174,  0.985], [0.342,  0.940], [0.500,  0.866],
                                [0.643,  0.766], [0.766,  0.643], [0.866,  0.500], [0.940,  0.342],
                                [0.985,  0.174], [1.000,  0.000], [0.985, -0.174], [0.940, -0.342],
                                [0.866, -0.500], [0.766, -0.643], [0.643, -0.766], [0.500, -0.866],
                                [0.342, -0.940], [0.174, -0.985], [0.000, -1.000]], dtype=np.float32)

    oChain.edges = np.array([[0,   1], [1,   2], [2,   3], [3,   4],
                             [4,   5], [5,   6], [6,   7], [7,   8],
                             [8,   9], [9,  10], [10, 11], [11, 12],
                             [12, 13], [13, 14], [14, 15], [15, 16],
                             [16, 17], [17, 18]], dtype=np.int32)
    return oChain


def sphere():
    mesh = Mesh(20, 36)
    mesh.vertices = np.array([[0.000,   0.000,   1.000],
                              [0.000,   0.745,   0.667],
                              [0.645,   0.372,   0.667],
                              [0.645,  -0.372,   0.667],
                              [0.000,  -0.745,   0.667],
                              [-0.645,  -0.372,  0.667],
                              [-0.645,   0.372,  0.667],
                              [0.500,    0.866,  0.000],
                              [1.000,    0.000,  0.000],
                              [0.500,   -0.866,  0.000],
                              [-0.500,  -0.866,  0.000],
                              [-1.000,   0.000,  0.000],
                              [-0.500,   0.866,  0.000],
                              [0.000,    0.745, -0.667],
                              [0.645,    0.372, -0.667],
                              [0.645,   -0.372, -0.667],
                              [0.000,   -0.745, -0.667],
                              [-0.645,  -0.372, -0.667],
                              [-0.645,   0.372, -0.667],
                              [0.000,    0.000, -1.000]], dtype=np.float32)
    
    mesh.triangles = np.array([[0,   2,  1], [0,   3,  2], [0,   4,  3],
                               [0,   5,  4], [0,   6,  5], [0,   1,  6],
                               [1,   2,  7], [2,   8,  7], [2,   3,  8],
                               [3,   9,  8], [3,   4,  9], [4,  10,  9],
                               [4,   5, 10], [5,  11, 10], [5,   6, 11],
                               [6,  12, 11], [6,   1, 12], [1,   7, 12],
                               [7,  14, 13], [7,   8, 14], [8,  15, 14],
                               [8,   9, 15], [9,  16, 15], [9,  10, 16],
                               [10, 17, 16], [10, 11, 17], [11, 18, 17],
                               [11, 12, 18], [12, 13, 18], [12,  7, 13],
                               [13, 14, 19], [14, 15, 19], [15, 16, 19],
                               [16, 17, 19], [17, 18, 19], [18, 13, 19]], dtype=np.int32)
    return mesh


def truncated_sphere():
    mesh = Mesh(20, 36)
    mesh.vertices = np.array([[0.000,   0.000,  0.667],
                              [0.000,   0.745,  0.667],
                              [0.645,   0.372,  0.667],
                              [0.645,  -0.372,  0.667],
                              [0.000,  -0.745,  0.667],
                              [-0.645, -0.372,  0.667],
                              [-0.645,  0.372,  0.667],
                              [0.500,   0.866,  0.000],
                              [1.000,   0.000,  0.000],
                              [0.500,  -0.866,  0.000],
                              [-0.500, -0.866,  0.000],
                              [-1.000,  0.000,  0.000],
                              [-0.500,  0.866,  0.000],
                              [0.000,   0.745, -0.667],
                              [0.645,   0.372, -0.667],
                              [0.645,  -0.372, -0.667],
                              [0.000,  -0.745, -0.667],
                              [-0.645, -0.372, -0.667],
                              [-0.645,  0.372, -0.667],
                              [0.000,   0.000, -1.000]], dtype=np.float32)

    mesh.triangles = np.array([[0,   2,  1], [0,   3,  2], [0,   4,  3],
                               [0,   5,  4], [0,   6,  5], [0,   1,  6],
                               [1,   2,  7], [2,   8,  7], [2,   3,  8],
                               [3,   9,  8], [3,   4,  9], [4,  10,  9],
                               [4,   5, 10], [5,  11, 10], [5,   6, 11],
                               [6,  12, 11], [6,   1, 12], [1,   7, 12],
                               [7,  14, 13], [7,   8, 14], [8,  15, 14],
                               [8,   9, 15], [9,  16, 15], [9,  10, 16],
                               [10, 17, 16], [10, 11, 17], [11, 18, 17],
                               [11, 12, 18], [12, 13, 18], [12,  7, 13],
                               [13, 14, 19], [14, 15, 19], [15, 16, 19],
                               [16, 17, 19], [17, 18, 19], [18, 13, 19]], dtype=np.int32)
    open_triangles = 6
    mesh.named_partition['interface'] = (0, open_triangles)
    mesh.named_partition['cavity'] = (open_triangles, 36)
    return mesh

def truncated_sphere_rad():
    chain = Chain(15, 14)
    chain.vertices = np.array([[0.000,   0.000],
                                [0.200,  0.000],
                                [0.400,  0.000],
                                [0.600,  0.000],
                                [0.800,  0.000],
                                [1.000,  0.000],
                                [0.985, -0.174],
                                [0.940, -0.342],
                                [0.866, -0.500],
                                [0.766, -0.643],
                                [0.643, -0.766],
                                [0.500, -0.866],
                                [0.342, -0.940],
                                [0.174, -0.985],
                                [0.000, -1.000]], dtype=np.float32)

    chain.edges = np.array([[0,   1],
                            [1,   2],
                            [2,   3],
                            [3,   4],
                            [4,   5],
                            [5,   6],
                            [6,   7],
                            [7,   8],
                            [8,   9],
                            [9,  10],
                            [10, 11],
                            [11, 12],
                            [12, 13],
                            [13,  0]], dtype=np.int32)
    open_edges = 5
    chain.named_partition['interface'] = (0, open_edges)
    chain.named_partition['cavity'] = (open_edges, 14)

    return chain
