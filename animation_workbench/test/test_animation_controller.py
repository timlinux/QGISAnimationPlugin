# coding=utf-8
"""GUI Utils Test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = '(C) 2018 by Nyall Dawson'
__date__ = '20/04/2018'
__copyright__ = 'Copyright 2018, North Road'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import unittest

from qgis.PyQt.QtCore import QSize, QEasingCurve
from qgis.core import (
    QgsMapSettings,
    QgsRectangle,
    QgsCoordinateReferenceSystem,
    QgsReferencedRectangle,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsPointXY
)

from animation_workbench.core import AnimationController, MapMode
from .utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class AnimationControllerTest(unittest.TestCase):
    """Test AnimationController works."""

    # pylint: disable=too-many-statements

    def test_fixed_extent(self):
        """
        Test a fixed extent job
        """
        map_settings = QgsMapSettings()
        map_settings.setExtent(QgsRectangle(1, 2, 3, 4))
        map_settings.setDestinationCrs(QgsCoordinateReferenceSystem('EPSG:4326'))
        map_settings.setOutputSize(QSize(400, 300))
        extent = QgsReferencedRectangle(map_settings.extent(), map_settings.destinationCrs())
        controller = AnimationController.create_fixed_extent_controller(map_settings=map_settings,
                                                                        feature_layer=None,
                                                                        output_extent=extent,
                                                                        total_frames=5,
                                                                        frame_rate=10)

        it = controller.create_jobs()
        # should be 5 frames
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 0)
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 0)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 5)
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 1)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 5)
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 2)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=1200003)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 5)
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 3)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 3)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 5)
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 4)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 4)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 5)

        with self.assertRaises(StopIteration):
            next(it)

    def test_fixed_extent_with_layer(self):
        """
        Test a fixed extent job with a layer
        """

        vl = QgsVectorLayer('Point?crs=EPSG:4326&field=name:string', 'vl', 'memory')
        self.assertTrue(vl.isValid())

        f = QgsFeature(vl.fields())
        f['name'] = 'f1'
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(1, 2)))
        self.assertTrue(vl.dataProvider().addFeature(f))

        f['name'] = 'f2'
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10, 20)))
        self.assertTrue(vl.dataProvider().addFeature(f))

        map_settings = QgsMapSettings()
        map_settings.setExtent(QgsRectangle(1, 2, 3, 4))
        map_settings.setDestinationCrs(QgsCoordinateReferenceSystem('EPSG:4326'))
        map_settings.setOutputSize(QSize(400, 300))
        extent = QgsReferencedRectangle(map_settings.extent(), map_settings.destinationCrs())
        controller = AnimationController.create_fixed_extent_controller(map_settings=map_settings,
                                                                        feature_layer=vl,
                                                                        output_extent=extent,
                                                                        total_frames=2,
                                                                        frame_rate=10)

        it = controller.create_jobs()
        # should be 4 frames
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 0)
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 0)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 0)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 1)
        # self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 4)
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 1)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 1)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 1)
        # self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 4)
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 2)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 0)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 2)
        # self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 4)
        job = next(it)
        self.assertEqual(job.map_settings.extent(), map_settings.extent())
        self.assertAlmostEqual(job.map_settings.scale(), 2693593, delta=120000)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 3)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 2693593, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 3)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 1)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 2)
        # self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 4)

        with self.assertRaises(StopIteration):
            next(it)

    def test_planar(self):
        """
        Test a planar job
        """

        vl = QgsVectorLayer('Point?crs=EPSG:4326&field=name:string', 'vl', 'memory')
        self.assertTrue(vl.isValid())

        f = QgsFeature(vl.fields())
        f['name'] = 'f1'
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(1, 2)))
        self.assertTrue(vl.dataProvider().addFeature(f))

        f['name'] = 'f2'
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10, 20)))
        self.assertTrue(vl.dataProvider().addFeature(f))

        map_settings = QgsMapSettings()
        map_settings.setExtent(QgsRectangle(1, 2, 3, 4))
        map_settings.setDestinationCrs(QgsCoordinateReferenceSystem('EPSG:4326'))
        map_settings.setOutputSize(QSize(400, 300))
        controller = AnimationController.create_moving_extent_controller(map_settings=map_settings,
                                                                         mode=MapMode.PLANAR,
                                                                         feature_layer=vl,
                                                                         travel_frames=4,
                                                                         dwell_frames=2,
                                                                         min_scale=2000000,
                                                                         max_scale=1000000,
                                                                         pan_easing=QEasingCurve(
                                                                             QEasingCurve.Type.Linear),
                                                                         zoom_easing=QEasingCurve(
                                                                             QEasingCurve.Type.Linear),
                                                                         frame_rate=10)

        it = controller.create_jobs()

        job = next(it)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 0)
        self.assertAlmostEqual(job.map_settings.scale(), 1000000, delta=120000)
        self.assertAlmostEqual(job.map_settings.extent().center().x(), 1, 2)
        self.assertAlmostEqual(job.map_settings.extent().center().y(), 2, 2)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 1000000, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 0)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 0)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 8)
        self.assertEqual(job.map_settings.expressionContext().variable('current_animation_action'), "Hovering")
        job = next(it)
        self.assertAlmostEqual(job.map_settings.extent().center().x(), 1, 2)
        self.assertAlmostEqual(job.map_settings.extent().center().y(), 2, 2)
        self.assertAlmostEqual(job.map_settings.scale(), 1000000, delta=120000)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 1)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 1000000, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 1)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 8)
        self.assertEqual(job.map_settings.expressionContext().variable('current_animation_action'), "Hovering")

        # now we start panning
        job = next(it)
        self.assertAlmostEqual(job.map_settings.scale(), 1000000, delta=120000)
        self.assertAlmostEqual(job.map_settings.extent().center().x(), 1, 2)
        self.assertAlmostEqual(job.map_settings.extent().center().y(), 2, 2)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 2)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 1000000, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 0)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 8)
        self.assertEqual(job.map_settings.expressionContext().variable('from_feature').id(), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('to_feature').id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('current_animation_action'), "Panning")

        job = next(it)
        self.assertAlmostEqual(job.map_settings.scale(), 1666666, delta=120000)
        self.assertAlmostEqual(job.map_settings.extent().center().x(), 4, 2)
        self.assertAlmostEqual(job.map_settings.extent().center().y(), 8, 2)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 3)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 1666666, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 3)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 1)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 8)
        self.assertEqual(job.map_settings.expressionContext().variable('from_feature').id(), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('to_feature').id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('current_animation_action'), "Panning")

        job = next(it)
        self.assertAlmostEqual(job.map_settings.scale(), 1666666, delta=120000)
        self.assertAlmostEqual(job.map_settings.extent().center().x(), 7, 2)
        self.assertAlmostEqual(job.map_settings.extent().center().y(), 14, 2)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 4)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 1666666, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 4)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 2)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 8)
        self.assertEqual(job.map_settings.expressionContext().variable('from_feature').id(), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('to_feature').id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('current_animation_action'), "Panning")

        job = next(it)
        self.assertAlmostEqual(job.map_settings.scale(), 1000000, delta=120000)
        self.assertAlmostEqual(job.map_settings.extent().center().x(), 10, 2)
        self.assertAlmostEqual(job.map_settings.extent().center().y(), 20, 2)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 5)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 1000000, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 5)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 3)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 8)
        self.assertEqual(job.map_settings.expressionContext().variable('from_feature').id(), 1)
        self.assertEqual(job.map_settings.expressionContext().variable('to_feature').id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('current_animation_action'), "Panning")

        job = next(it)
        self.assertAlmostEqual(job.map_settings.scale(), 1000000, delta=120000)
        self.assertAlmostEqual(job.map_settings.extent().center().x(), 10, 2)
        self.assertAlmostEqual(job.map_settings.extent().center().y(), 20, 2)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 6)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 1000000, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 6)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 0)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 8)
        self.assertEqual(job.map_settings.expressionContext().variable('current_animation_action'), "Hovering")

        job = next(it)
        self.assertAlmostEqual(job.map_settings.scale(), 1000000, delta=120000)
        self.assertAlmostEqual(job.map_settings.extent().center().x(), 10, 2)
        self.assertAlmostEqual(job.map_settings.extent().center().y(), 20, 2)
        self.assertEqual(job.map_settings.frameRate(), 10)
        self.assertEqual(job.map_settings.currentFrame(), 7)
        self.assertAlmostEqual(job.map_settings.expressionContext().variable('map_scale'), 1000000, delta=120000)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_number'), 7)
        self.assertEqual(job.map_settings.expressionContext().variable('frame_rate'), 10)
        self.assertEqual(job.map_settings.expressionContext().variable('current_frame_for_feature'), 1)
        self.assertEqual(job.map_settings.expressionContext().feature().id(), 2)
        self.assertEqual(job.map_settings.expressionContext().variable('total_frame_count'), 8)
        self.assertEqual(job.map_settings.expressionContext().variable('current_animation_action'), "Hovering")

        with self.assertRaises(StopIteration):
            next(it)


if __name__ == "__main__":
    suite = unittest.makeSuite(AnimationControllerTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
