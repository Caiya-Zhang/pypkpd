import project.create_design
import numpy as np


xt1 = [np.array([1, 2, 3]), np.array([1, 2, 3, 4])]


design_1 = project.create_design.create_design(xt=xt1, groupsize=20)
#D:\college\extension\poped_python
print(design_1)