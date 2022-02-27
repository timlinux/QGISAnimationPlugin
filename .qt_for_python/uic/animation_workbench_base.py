# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/timlinux/dev/python/QGISAnimationWorkbench/ui/animation_workbench_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_animation_workbench_base(object):
    def setupUi(self, animation_workbench_base):
        animation_workbench_base.setObjectName("animation_workbench_base")
        animation_workbench_base.resize(774, 779)
        self.gridLayout_9 = QtWidgets.QGridLayout(animation_workbench_base)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea = QtWidgets.QScrollArea(animation_workbench_base)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 744, 842))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.animation_reference_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.animation_reference_group.setObjectName("animation_reference_group")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.animation_reference_group)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.layer_combo = gui.QgsMapLayerComboBox(self.animation_reference_group)
        self.layer_combo.setObjectName("layer_combo")
        self.gridLayout_4.addWidget(self.layer_combo, 1, 1, 1, 1)
        self.point_layer_label = QtWidgets.QLabel(self.animation_reference_group)
        self.point_layer_label.setObjectName("point_layer_label")
        self.gridLayout_4.addWidget(self.point_layer_label, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.animation_reference_group, 0, 0, 1, 1)
        self.output_destination_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.output_destination_group.setObjectName("output_destination_group")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.output_destination_group)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.folder_label = QtWidgets.QLabel(self.output_destination_group)
        self.folder_label.setObjectName("folder_label")
        self.gridLayout_6.addWidget(self.folder_label, 0, 0, 1, 1)
        self.folder_edit = QtWidgets.QLineEdit(self.output_destination_group)
        self.folder_edit.setObjectName("folder_edit")
        self.gridLayout_6.addWidget(self.folder_edit, 0, 1, 1, 1)
        self.folder_button = QtWidgets.QToolButton(self.output_destination_group)
        self.folder_button.setObjectName("folder_button")
        self.gridLayout_6.addWidget(self.folder_button, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.output_destination_group, 6, 0, 1, 1)
        self.output_options_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.output_options_group.setObjectName("output_options_group")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.output_options_group)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radio_gif = QtWidgets.QRadioButton(self.output_options_group)
        self.radio_gif.setObjectName("radio_gif")
        self.gridLayout_5.addWidget(self.radio_gif, 0, 0, 1, 1)
        self.rad_movie = QtWidgets.QRadioButton(self.output_options_group)
        self.rad_movie.setChecked(True)
        self.rad_movie.setObjectName("rad_movie")
        self.gridLayout_5.addWidget(self.rad_movie, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.output_options_group, 5, 0, 1, 1)
        self.preview_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.preview_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.preview_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.preview_frame.setObjectName("preview_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.preview_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.zoom_easing_preview = QtWidgets.QWidget(self.preview_frame)
        self.zoom_easing_preview.setMinimumSize(QtCore.QSize(250, 150))
        self.zoom_easing_preview.setObjectName("zoom_easing_preview")
        self.gridLayout_3.addWidget(self.zoom_easing_preview, 3, 0, 1, 1)
        self.current_frame_preview = QtWidgets.QLabel(self.preview_frame)
        self.current_frame_preview.setMinimumSize(QtCore.QSize(250, 150))
        self.current_frame_preview.setMaximumSize(QtCore.QSize(250, 150))
        self.current_frame_preview.setObjectName("current_frame_preview")
        self.gridLayout_3.addWidget(self.current_frame_preview, 5, 0, 1, 1)
        self.project_variables_text_edit = QtWidgets.QTextEdit(self.preview_frame)
        self.project_variables_text_edit.setObjectName("project_variables_text_edit")
        self.gridLayout_3.addWidget(self.project_variables_text_edit, 7, 0, 1, 1)
        self.pan_easing_preview_label = QtWidgets.QLabel(self.preview_frame)
        self.pan_easing_preview_label.setObjectName("pan_easing_preview_label")
        self.gridLayout_3.addWidget(self.pan_easing_preview_label, 0, 0, 1, 1)
        self.zoom_easing_label_3 = QtWidgets.QLabel(self.preview_frame)
        self.zoom_easing_label_3.setObjectName("zoom_easing_label_3")
        self.gridLayout_3.addWidget(self.zoom_easing_label_3, 4, 0, 1, 1)
        self.pan_easing_preview = QtWidgets.QWidget(self.preview_frame)
        self.pan_easing_preview.setMinimumSize(QtCore.QSize(250, 150))
        self.pan_easing_preview.setObjectName("pan_easing_preview")
        self.gridLayout_3.addWidget(self.pan_easing_preview, 1, 0, 1, 1)
        self.project_variables_label = QtWidgets.QLabel(self.preview_frame)
        self.project_variables_label.setObjectName("project_variables_label")
        self.gridLayout_3.addWidget(self.project_variables_label, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 8, 0, 1, 1)
        self.zoom_easing_preview_label = QtWidgets.QLabel(self.preview_frame)
        self.zoom_easing_preview_label.setObjectName("zoom_easing_preview_label")
        self.gridLayout_3.addWidget(self.zoom_easing_preview_label, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.preview_frame, 0, 1, 7, 1)
        self.animation_frames_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.animation_frames_group.setObjectName("animation_frames_group")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.animation_frames_group)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.hover_frames_label = QtWidgets.QLabel(self.animation_frames_group)
        self.hover_frames_label.setObjectName("hover_frames_label")
        self.gridLayout_8.addWidget(self.hover_frames_label, 1, 0, 1, 1)
        self.hover_frames_spin = QtWidgets.QSpinBox(self.animation_frames_group)
        self.hover_frames_spin.setMaximum(999)
        self.hover_frames_spin.setProperty("value", 15)
        self.hover_frames_spin.setObjectName("hover_frames_spin")
        self.gridLayout_8.addWidget(self.hover_frames_spin, 1, 1, 1, 1)
        self.point_frames_label = QtWidgets.QLabel(self.animation_frames_group)
        self.point_frames_label.setObjectName("point_frames_label")
        self.gridLayout_8.addWidget(self.point_frames_label, 0, 0, 1, 1)
        self.point_frames_spin = QtWidgets.QSpinBox(self.animation_frames_group)
        self.point_frames_spin.setMaximum(999)
        self.point_frames_spin.setProperty("value", 15)
        self.point_frames_spin.setObjectName("point_frames_spin")
        self.gridLayout_8.addWidget(self.point_frames_spin, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.animation_frames_group, 4, 0, 1, 1)
        self.easings_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.easings_group.setObjectName("easings_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.easings_group)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pan_easing_label = QtWidgets.QLabel(self.easings_group)
        self.pan_easing_label.setObjectName("pan_easing_label")
        self.gridLayout_2.addWidget(self.pan_easing_label, 0, 0, 1, 1)
        self.zoom_easing_combo = QtWidgets.QComboBox(self.easings_group)
        self.zoom_easing_combo.setObjectName("zoom_easing_combo")
        self.gridLayout_2.addWidget(self.zoom_easing_combo, 1, 2, 1, 1)
        self.zoom_easing_label = QtWidgets.QLabel(self.easings_group)
        self.zoom_easing_label.setObjectName("zoom_easing_label")
        self.gridLayout_2.addWidget(self.zoom_easing_label, 1, 0, 1, 1)
        self.pan_easing_combo = QtWidgets.QComboBox(self.easings_group)
        self.pan_easing_combo.setObjectName("pan_easing_combo")
        self.gridLayout_2.addWidget(self.pan_easing_combo, 0, 2, 1, 1)
        self.pan_preview_legend = QtWidgets.QWidget(self.easings_group)
        self.pan_preview_legend.setMaximumSize(QtCore.QSize(25, 25))
        self.pan_preview_legend.setAutoFillBackground(False)
        self.pan_preview_legend.setStyleSheet("background: yellow; border-radius: 3px;")
        self.pan_preview_legend.setObjectName("pan_preview_legend")
        self.gridLayout_2.addWidget(self.pan_preview_legend, 0, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.easings_group)
        self.widget_2.setMaximumSize(QtCore.QSize(25, 25))
        self.widget_2.setStyleSheet("background: green; border-radius: 3px;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.easings_group, 3, 0, 1, 1)
        self.render_mode_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.render_mode_group.setObjectName("render_mode_group")
        self.gridLayout = QtWidgets.QGridLayout(self.render_mode_group)
        self.gridLayout.setObjectName("gridLayout")
        self.radio_sphere = QtWidgets.QRadioButton(self.render_mode_group)
        self.radio_sphere.setObjectName("radio_sphere")
        self.gridLayout.addWidget(self.radio_sphere, 0, 0, 1, 1)
        self.radio_planar = QtWidgets.QRadioButton(self.render_mode_group)
        self.radio_planar.setChecked(True)
        self.radio_planar.setObjectName("radio_planar")
        self.gridLayout.addWidget(self.radio_planar, 0, 1, 1, 1)
        self.radio_static = QtWidgets.QRadioButton(self.render_mode_group)
        self.radio_static.setObjectName("radio_static")
        self.gridLayout.addWidget(self.radio_static, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.render_mode_group, 2, 0, 1, 1)
        self.zoom_range_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.zoom_range_group.setObjectName("zoom_range_group")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.zoom_range_group)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.mScaleRangeWidget = gui.QgsScaleRangeWidget(self.zoom_range_group)
        self.mScaleRangeWidget.setObjectName("mScaleRangeWidget")
        self.gridLayout_10.addWidget(self.mScaleRangeWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.zoom_range_group, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.button_box = QtWidgets.QDialogButtonBox(animation_workbench_base)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout_9.addWidget(self.button_box, 1, 0, 1, 1)

        self.retranslateUi(animation_workbench_base)
        self.button_box.accepted.connect(animation_workbench_base.accept) # type: ignore
        self.button_box.rejected.connect(animation_workbench_base.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(animation_workbench_base)

    def retranslateUi(self, animation_workbench_base):
        _translate = QtCore.QCoreApplication.translate
        animation_workbench_base.setWindowTitle(_translate("animation_workbench_base", "Dialog"))
        self.animation_reference_group.setTitle(_translate("animation_workbench_base", "Animation Reference"))
        self.point_layer_label.setText(_translate("animation_workbench_base", "Point layer"))
        self.output_destination_group.setTitle(_translate("animation_workbench_base", "Output Destination"))
        self.folder_label.setText(_translate("animation_workbench_base", "Folder"))
        self.folder_edit.setToolTip(_translate("animation_workbench_base", "The output folder will be populated with \n"
"all of the frames of the animation, and \n"
"the GIF or MP4 as selected above."))
        self.folder_button.setText(_translate("animation_workbench_base", "..."))
        self.output_options_group.setToolTip(_translate("animation_workbench_base", "Select which output format you would like. \n"
"Regardless of which you choose, a folder \n"
"of images will be created, one image per frame. \n"
"For the GIF export to work, you will \n"
"need to have the ImageMagick \'convert\'  application \n"
"available on your system. For the MP4 option to work, \n"
"you need to have the \'ffmpeg\' application on \n"
"your system."))
        self.output_options_group.setTitle(_translate("animation_workbench_base", "Output Options"))
        self.radio_gif.setText(_translate("animation_workbench_base", "Animated GIF"))
        self.rad_movie.setText(_translate("animation_workbench_base", "Movie (MP4)"))
        self.current_frame_preview.setText(_translate("animation_workbench_base", "TextLabel"))
        self.project_variables_text_edit.setHtml(_translate("animation_workbench_base", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can use these project variables to make cool expression based cartography that changes as the animation progresses, each point gets focussed on etc.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">@frames_per_point - the number of frames between points as defined in this dialog.<br />@current_frame - the number of the current frame in the current point set.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">@current_point_id - the id of the current point we are travelling to.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here is a example of an expression you could use to show an animation of the animation progress in the copyright decoration:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><span style=\" font-family:\'Droid Sans Mono\',\'monospace\',\'monospace\'; font-size:14px; color:#6a9955;\">[%\'Frame \' || to_string(coalesce(@current_frame, 0)) || \'/\' || </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Droid Sans Mono\',\'monospace\',\'monospace\'; font-size:14px; color:#d4d4d4;\">     </span><span style=\" font-family:\'Droid Sans Mono\',\'monospace\',\'monospace\'; font-size:14px; color:#6a9955;\">to_string(coalesce(@frames_per_point, 0)) || \' for point \' || </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Droid Sans Mono\',\'monospace\',\'monospace\'; font-size:14px; color:#d4d4d4;\">     </span><span style=\" font-family:\'Droid Sans Mono\',\'monospace\',\'monospace\'; font-size:14px; color:#6a9955;\">to_string(coalesce(@current_point_id,0))%]</span></p></body></html>"))
        self.pan_easing_preview_label.setText(_translate("animation_workbench_base", "Pan Easing Preview"))
        self.zoom_easing_label_3.setText(_translate("animation_workbench_base", "Current Frame Preview"))
        self.project_variables_label.setText(_translate("animation_workbench_base", "Project Variables"))
        self.zoom_easing_preview_label.setText(_translate("animation_workbench_base", "Zoom Easing Preview"))
        self.animation_frames_group.setTitle(_translate("animation_workbench_base", "Animation Frames"))
        self.hover_frames_label.setText(_translate("animation_workbench_base", "Hover frames at each point"))
        self.hover_frames_spin.setToolTip(_translate("animation_workbench_base", "This is the number of frames that will \n"
"be used during animation of the motion from \n"
"one point to the next. Video generation \n"
"is done at 30 frames per second, so a value \n"
"of 30 here would result in a 1 second flight time \n"
"between two consecutive points."))
        self.point_frames_label.setText(_translate("animation_workbench_base", "Frames between points"))
        self.point_frames_spin.setToolTip(_translate("animation_workbench_base", "This is the number of frames that will be used during\n"
" animation of the dwell period at each point. \n"
"Video generation is done at 30 frames per \n"
"second, so a value of 30 here would result in a 1 second \n"
"dwell time."))
        self.easings_group.setTitle(_translate("animation_workbench_base", "Easings"))
        self.pan_easing_label.setText(_translate("animation_workbench_base", "Pan Easing"))
        self.zoom_easing_combo.setToolTip(_translate("animation_workbench_base", "The zoom easing will affect the behaviour \n"
"of the camera during zoom transitions."))
        self.zoom_easing_label.setText(_translate("animation_workbench_base", "Zoom Easing"))
        self.pan_easing_combo.setToolTip(_translate("animation_workbench_base", "The pan easing will determine the motion \n"
"characteristics of the camera on the Y axis \n"
"as it flies across the scene."))
        self.render_mode_group.setToolTip(_translate("animation_workbench_base", "The render mode determines the behaviour and type of the animation. \n"
"For \'Sphere\' the coordinate reference system (CRS) will \n"
"be manipulated to create a spinning globe effect. \n"
"For \'Plane\', the CRS will not be altered, but will pan and \n"
"zoom to each point. For \'Static\' the animation will not \n"
"not pan / zoom the map."))
        self.render_mode_group.setTitle(_translate("animation_workbench_base", "Render Mode"))
        self.radio_sphere.setText(_translate("animation_workbench_base", "Sphere"))
        self.radio_planar.setText(_translate("animation_workbench_base", "Planar"))
        self.radio_static.setText(_translate("animation_workbench_base", "Static"))
        self.zoom_range_group.setToolTip(_translate("animation_workbench_base", "The scale range that the animation should \n"
"move through. The smallest scale will be \n"
"the zenith of the animation when it zooms \n"
"out while travelling between points, and the \n"
"largest scale will be the scale used when \n"
"we arrive at each point."))
        self.zoom_range_group.setTitle(_translate("animation_workbench_base", "Zoom Range"))
from qgis import gui
