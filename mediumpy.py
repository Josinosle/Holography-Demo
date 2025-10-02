import matplotlib.pyplot as plt

class Medium:
    def __init__(self, x, y, z, n, l):
        self.x = x
        self.y = y
        self.z = z
        self.n = n
        self.l = l

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def draw(self,axis):
        from mpl_toolkits.mplot3d.art3d import Poly3DCollection

        # Define cube vertices
        vertices = [
            [self.x, self.y, self.z],
            [self.l+self.x, self.y, self.z],
            [self.l+self.x, self.l+self.y, self.z],
            [self.x, self.l+self.y, self.z],
            [self.x, self.y, self.l+self.z],
            [self.l+self.x, self.y, self.l+self.z],
            [self.l+self.x, self.l+self.y, self.l+self.z],
            [self.x, self.l+self.y, self.l+self.z]
        ]

        # Define cube faces
        faces = [
            [vertices[j] for j in [0, 1, 2, 3]],
            [vertices[j] for j in [4, 5, 6, 7]],
            [vertices[j] for j in [0, 1, 5, 4]],
            [vertices[j] for j in [2, 3, 7, 6]],
            [vertices[j] for j in [1, 2, 6, 5]],
            [vertices[j] for j in [4, 7, 3, 0]]
        ]

        # Plotting the cube
        axis.add_collection3d(Poly3DCollection(faces, facecolors='cyan', edgecolors='black', linewidths=1, alpha=0.5))

