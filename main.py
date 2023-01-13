# The file for running the calculation after collecting the inputs
import inputs
"""from inputs import CollectInput
from inputs import ifExist
from inputs import findIndex
from inputs import AddInput"""

name, info = inputs.CollectInput()


db = []
inputs.AddInput(db, name, info)
name, info = inputs.CollectInput()
inputs.AddInput(db, name, info)


print(db)