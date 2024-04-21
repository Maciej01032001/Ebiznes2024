import unittest
import square_and_cube as sc


class TestSquareAndCube(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(sc.square_root(0), 0)
        self.assertEqual(sc.square_root(1), 1)
        self.assertEqual(sc.square_root(4), 2)
        self.assertEqual(sc.square_root(9), 3)
        self.assertAlmostEqual(sc.square_root(2), 1.414, places=3)
        with self.assertRaises(ValueError):
            sc.square_root(-1)

    def test_cube_root(self):
        self.assertEqual(sc.cube_root(0), 0)
        self.assertEqual(sc.cube_root(1), 1)
        self.assertEqual(sc.cube_root(8), 2)
        self.assertEqual(sc.cube_root(27), 3)
        self.assertAlmostEqual(sc.cube_root(64), 4, places=0)
        self.assertEqual(sc.cube_root(-1), -1)
        self.assertEqual(sc.cube_root(-8), -2)
        self.assertEqual(sc.cube_root(-27), -3)
        self.assertAlmostEqual(sc.cube_root(-64), -4, places=0)



    def test_area_of_square(self):
        self.assertEqual(sc.area_of_square(0), 0)
        self.assertEqual(sc.area_of_square(1), 1)
        self.assertEqual(sc.area_of_square(2), 4)
        self.assertEqual(sc.area_of_square(3), 9)
        self.assertEqual(sc.area_of_square(4), 16)
        self.assertEqual(sc.area_of_square(5), 25)
        self.assertEqual(sc.area_of_square(1.25), 1.5625)
        self.assertEqual(sc.area_of_square(2.5), 6.25)
        self.assertAlmostEqual(sc.area_of_square(1.414), 1.999, places=3)
        with self.assertRaises(ValueError):
            sc.area_of_square(-1)

    def test_area_of_cube(self):
        self.assertEqual(sc.area_of_cube(0), 0)
        self.assertEqual(sc.area_of_cube(1), 6)
        self.assertEqual(sc.area_of_cube(2), 24)
        self.assertEqual(sc.area_of_cube(3), 54)
        self.assertEqual(sc.area_of_cube(4), 96)
        self.assertEqual(sc.area_of_cube(5), 150)
        self.assertEqual(sc.area_of_cube(1.25), 9.375)
        self.assertEqual(sc.area_of_cube(2.5), 37.5)
        self.assertAlmostEqual(sc.area_of_cube(3.3), 65.340, places=3)
        with self.assertRaises(ValueError):
            sc.area_of_cube(-1)

    def test_volume_of_cube(self):
        self.assertEqual(sc.volume_of_cube(0), 0)
        self.assertEqual(sc.volume_of_cube(1), 1)
        self.assertEqual(sc.volume_of_cube(2), 8)
        self.assertEqual(sc.volume_of_cube(3), 27)
        self.assertEqual(sc.volume_of_cube(4), 64)
        self.assertEqual(sc.volume_of_cube(5), 125)
        self.assertAlmostEqual(sc.volume_of_cube(1.25), 1.953, places=3)
        self.assertEqual(sc.volume_of_cube(2.5), 15.625)
        self.assertAlmostEqual(sc.volume_of_cube(3.3), 35.937, places=3)
        with self.assertRaises(ValueError):
            sc.volume_of_cube(-1)

    def test_perimeter_of_square(self):
        self.assertEqual(sc.perimeter_of_square(0), 0)
        self.assertEqual(sc.perimeter_of_square(1), 4)
        self.assertEqual(sc.perimeter_of_square(2), 8)
        self.assertEqual(sc.perimeter_of_square(3), 12)
        self.assertEqual(sc.perimeter_of_square(4), 16)
        self.assertEqual(sc.perimeter_of_square(5), 20)
        self.assertEqual(sc.perimeter_of_square(1.25), 5)
        self.assertEqual(sc.perimeter_of_square(2.5), 10)
        self.assertEqual(sc.perimeter_of_square(3.3), 13.2)
        with self.assertRaises(ValueError):
            sc.perimeter_of_square(-1)

    def test_perimeter_of_cube(self):
        self.assertEqual(sc.perimeter_of_cube(0), 0)
        self.assertEqual(sc.perimeter_of_cube(1), 12)
        self.assertEqual(sc.perimeter_of_cube(2), 24)
        self.assertEqual(sc.perimeter_of_cube(3), 36)
        self.assertEqual(sc.perimeter_of_cube(4), 48)
        self.assertEqual(sc.perimeter_of_cube(5), 60)
        self.assertEqual(sc.perimeter_of_cube(1.25), 15)
        self.assertEqual(sc.perimeter_of_cube(2.5), 30)
        self.assertAlmostEqual(sc.perimeter_of_cube(3.3), 39.6, places=3)
        with self.assertRaises(ValueError):
            sc.perimeter_of_cube(-1)


if __name__ == '__main__':
    unittest.main()
