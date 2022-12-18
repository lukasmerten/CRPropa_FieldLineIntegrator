import sys
sys.path.append("/home/home1/mertelx/.py_venvs/crpropa_master/CRPropa_FieldLineIntegrator/build")

#import crpropa as crp
#import FieldlineIntegrator as fli
#
#
#bfield = crp.UniformMagneticField(crp.Vector3d(0,0,1))
#
#FLI = fli.FieldlineIntegrator(bfield, 1e-4, 10*crp.pc, 1*crp.kpc, True)

import sys

try:
    import unittest
    import tempfile
except:
    print("***********************************************************")
    print("* WARNING!! Couldn't import python unittesting framework! *")
    print("* No python tests have been executed                      *")
    print("***********************************************************")
    sys.exit(0)

try:
    import crpropa as crp
except Exception as e:
    print("*** CRPropa import failed")
    print(type(e), str(e))
    sys.exit(-1)

try:
    import FieldlineIntegrator as fli
except Exception as e:
    print("*** FieldlineIntegrator import failed")
    print(type(e), str(e))
    sys.exit(-1)

class testSimpleFieldlineIntegration(unittest.TestCase):
    def runTest(self):
        
        bfield = crp.UniformMagneticField(crp.Vector3d(0,0,1))
        
        #propagation parallel to magnetic field
        integrator = fli.FieldlineIntegrator(bfield, 1e-4, 1*crp.pc, 1*crp.pc, True)

        c = crp.Candidate()
        c.current.setPosition(crp.Vector3d(0))

        integrator.process(c)

        self.assertEqual(c.current.getPosition().x, 0.)
        self.assertEqual(c.current.getPosition().y, 0.)
        self.assertAlmostEqual(c.current.getPosition().z/crp.pc, 1)

        #propagation anti-parallel to magnetic field
        integrator.setDirection(False)

        c = crp.Candidate()
        c.current.setPosition(crp.Vector3d(0))

        integrator.process(c)

        self.assertEqual(c.current.getPosition().x, 0.)
        self.assertEqual(c.current.getPosition().y, 0.)
        self.assertAlmostEqual(c.current.getPosition().z/crp.pc, -1)


if __name__ == '__main__':
    unittest.main()
