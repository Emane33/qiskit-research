from qiskit_research.protein_folding.interactions.random_interaction import (
    RandomInteraction,
)
from qiskit_research.protein_folding.interactions.miyazawa_jernigan_interaction import (
    MiyazawaJerniganInteraction,
)
from qiskit_research.protein_folding.peptide.peptide import Peptide
from qiskit_research.protein_folding.protein_folding_problem import (
    ProteinFoldingProblem,
)

from qiskit_research.protein_folding.penalty_parameters import PenaltyParameters
from qiskit.utils import algorithm_globals, QuantumInstance

algorithm_globals.random_seed = 23
main_chain = "APRLRFY"
side_chains = ["" , "A", "P", "R", "L", "F",""]
side_chain_1 = ["" , "A", "P", "R", "L", "F",""]
side_chain_2 = ["" , "A", "P", "R", "L", "F",""]
side_chain_3 = ["" , "A", "P", "R", "L", "F",""]
result = []
for i in range(len(side_chains)):
    result.append(side_chains[i] + side_chain_1[i] + side_chain_2[i] + side_chain_3[i])
#we got to a point where we think that the way to calulate energy for all side chains is by increasing the qubits
mj_interaction = MiyazawaJerniganInteraction()
penalty_back = 10
penalty_chiral = 10
penalty_1 = 10

penalty_terms = PenaltyParameters(penalty_chiral, penalty_back, penalty_1)
peptide = Peptide(main_chain, result)

protein_folding_problem = ProteinFoldingProblem(peptide, mj_interaction, penalty_terms)
qubit_op = protein_folding_problem.qubit_op()
print(qubit_op)
