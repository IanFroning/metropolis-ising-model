from Hamiltonian import Hamiltonian

ham = Hamiltonian('1000', 0)

print('getLength: %s' % ham.getLength())

for i in range(0, ham.getLength()):
    print('getSpin(%s): %s' % (i, ham.getSpin(i)))

print('getEnergy: %s (should be 0)' %  ham.getEnergy())

print('getMagnetization: %s (should be -2)' %  ham.getMagnetization())

print('Flipping spin 3...')
ham.flipSpin(3)

for i in range(0, ham.getLength()):
    print('getSpin(%s): %s' % (i, ham.getSpin(i)))

print('getEnergy: %s (should be 4)' % ham.getEnergy())

print('getMagnetization: %s (should be 0)' %  ham.getMagnetization())
