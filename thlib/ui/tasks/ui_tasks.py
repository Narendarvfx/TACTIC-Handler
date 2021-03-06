# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasks\ui_tasks.ui'
#
# Created: Sat Oct  5 00:17:08 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from thlib.side.Qt import QtWidgets as QtGui
from thlib.side.Qt import QtGui as Qt4Gui
from thlib.side.Qt import QtCore

class Ui_tasks(object):
    def setupUi(self, tasks):
        tasks.setObjectName("tasks")
        tasks.resize(705, 420)
        self.verticalLayout = QtGui.QVBoxLayout(tasks)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(tasks)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.gridLayoutWidget = QtGui.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.contextLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.contextLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.contextLabel.setObjectName("contextLabel")
        self.gridLayout_2.addWidget(self.contextLabel, 2, 0, 1, 1)
        self.contextLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contextLineEdit.sizePolicy().hasHeightForWidth())
        self.contextLineEdit.setSizePolicy(sizePolicy)
        self.contextLineEdit.setObjectName("contextLineEdit")
        self.gridLayout_2.addWidget(self.contextLineEdit, 2, 1, 1, 1)
        self.processTreeWidget = QtGui.QTreeWidget(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processTreeWidget.sizePolicy().hasHeightForWidth())
        self.processTreeWidget.setSizePolicy(sizePolicy)
        self.processTreeWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.processTreeWidget.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.processTreeWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.processTreeWidget.setAllColumnsShowFocus(True)
        self.processTreeWidget.setColumnCount(1)
        self.processTreeWidget.setObjectName("processTreeWidget")
        self.processTreeWidget.headerItem().setText(0, "Process:")
        self.processTreeWidget.header().setVisible(False)
        self.gridLayout_2.addWidget(self.processTreeWidget, 1, 0, 1, 2)
        self.taskInfoGroupBox = QtGui.QGroupBox(self.splitter)
        self.taskInfoGroupBox.setBaseSize(QtCore.QSize(500, 0))
        self.taskInfoGroupBox.setFlat(True)
        self.taskInfoGroupBox.setObjectName("taskInfoGroupBox")
        self.gridLayout = QtGui.QGridLayout(self.taskInfoGroupBox)
        self.gridLayout.setContentsMargins(4, 6, 4, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(self.taskInfoGroupBox)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.editorLayout = QtGui.QHBoxLayout()
        self.editorLayout.setSpacing(0)
        self.editorLayout.setContentsMargins(-1, 0, -1, -1)
        self.editorLayout.setObjectName("editorLayout")
        self.verticalLayout_2.addLayout(self.editorLayout)
        self.descriptionTextEdit = QtGui.QTextEdit(self.groupBox)
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        self.verticalLayout_2.addWidget(self.descriptionTextEdit)
        self.gridLayout.addWidget(self.groupBox, 9, 0, 1, 3)
        self.label_3 = QtGui.QLabel(self.taskInfoGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.taskInfoGroupBox)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.assignedToComboBox = QtGui.QComboBox(self.taskInfoGroupBox)
        self.assignedToComboBox.setEditable(True)
        self.assignedToComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.assignedToComboBox.setObjectName("assignedToComboBox")
        self.gridLayout.addWidget(self.assignedToComboBox, 0, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.taskInfoGroupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.priorityComboBox = QtGui.QComboBox(self.taskInfoGroupBox)
        self.priorityComboBox.setEditable(True)
        self.priorityComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.priorityComboBox.setObjectName("priorityComboBox")
        self.gridLayout.addWidget(self.priorityComboBox, 2, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.taskInfoGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.statusComboBox = QtGui.QComboBox(self.taskInfoGroupBox)
        self.statusComboBox.setEditable(True)
        self.statusComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.statusComboBox.setObjectName("statusComboBox")
        self.gridLayout.addWidget(self.statusComboBox, 3, 1, 1, 2)
        self.startedDateTimeEdit = QtGui.QDateTimeEdit(self.taskInfoGroupBox)
        self.startedDateTimeEdit.setCalendarPopup(True)
        self.startedDateTimeEdit.setObjectName("startedDateTimeEdit")
        self.gridLayout.addWidget(self.startedDateTimeEdit, 4, 1, 1, 2)
        self.superviserComboBox = QtGui.QComboBox(self.taskInfoGroupBox)
        self.superviserComboBox.setEditable(True)
        self.superviserComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.superviserComboBox.setObjectName("superviserComboBox")
        self.gridLayout.addWidget(self.superviserComboBox, 1, 1, 1, 2)
        self.endDateTimeEdit = QtGui.QDateTimeEdit(self.taskInfoGroupBox)
        self.endDateTimeEdit.setCalendarPopup(True)
        self.endDateTimeEdit.setObjectName("endDateTimeEdit")
        self.gridLayout.addWidget(self.endDateTimeEdit, 5, 1, 1, 2)
        self.label_6 = QtGui.QLabel(self.taskInfoGroupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.taskInfoGroupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.saveChangesButton = QtGui.QPushButton(self.taskInfoGroupBox)
        self.saveChangesButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.saveChangesButton.setObjectName("saveChangesButton")
        self.gridLayout.addWidget(self.saveChangesButton, 10, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.taskInfoGroupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.showNotesButton = QtGui.QToolButton(self.taskInfoGroupBox)
        self.showNotesButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.showNotesButton.setAutoRaise(True)
        self.showNotesButton.setArrowType(QtCore.Qt.RightArrow)
        self.showNotesButton.setObjectName("showNotesButton")
        self.gridLayout.addWidget(self.showNotesButton, 10, 0, 1, 1)
        self.subsParentStatusLabel = QtGui.QLabel(self.taskInfoGroupBox)
        self.subsParentStatusLabel.setObjectName("subsParentStatusLabel")
        self.gridLayout.addWidget(self.subsParentStatusLabel, 6, 1, 1, 1)
        self.subsParentPushButton = QtGui.QPushButton(self.taskInfoGroupBox)
        self.subsParentPushButton.setObjectName("subsParentPushButton")
        self.gridLayout.addWidget(self.subsParentPushButton, 6, 2, 1, 1)
        self.subsTaskPushButton = QtGui.QPushButton(self.taskInfoGroupBox)
        self.subsTaskPushButton.setObjectName("subsTaskPushButton")
        self.gridLayout.addWidget(self.subsTaskPushButton, 7, 2, 1, 1)
        self.subsTaskStatusLabel = QtGui.QLabel(self.taskInfoGroupBox)
        self.subsTaskStatusLabel.setObjectName("subsTaskStatusLabel")
        self.gridLayout.addWidget(self.subsTaskStatusLabel, 7, 1, 1, 1)
        self.subsUsersPushButton = QtGui.QPushButton(self.taskInfoGroupBox)
        self.subsUsersPushButton.setObjectName("subsUsersPushButton")
        self.gridLayout.addWidget(self.subsUsersPushButton, 8, 2, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        self.skeyLineEdit = QtGui.QLineEdit(tasks)
        self.skeyLineEdit.setObjectName("skeyLineEdit")
        self.verticalLayout.addWidget(self.skeyLineEdit)

        self.retranslateUi(tasks)
        QtCore.QMetaObject.connectSlotsByName(tasks)
        tasks.setTabOrder(self.assignedToComboBox, self.superviserComboBox)
        tasks.setTabOrder(self.superviserComboBox, self.priorityComboBox)
        tasks.setTabOrder(self.priorityComboBox, self.statusComboBox)
        tasks.setTabOrder(self.statusComboBox, self.startedDateTimeEdit)
        tasks.setTabOrder(self.startedDateTimeEdit, self.endDateTimeEdit)
        tasks.setTabOrder(self.endDateTimeEdit, self.descriptionTextEdit)
        tasks.setTabOrder(self.descriptionTextEdit, self.saveChangesButton)
        tasks.setTabOrder(self.saveChangesButton, self.subsParentPushButton)
        tasks.setTabOrder(self.subsParentPushButton, self.showNotesButton)
        tasks.setTabOrder(self.showNotesButton, self.skeyLineEdit)

    def retranslateUi(self, tasks):
        tasks.setWindowTitle(u"Tasks for exam/props Mushroom")
        self.contextLabel.setText(u"Context:")
        self.taskInfoGroupBox.setTitle(u"Task info:")
        self.groupBox.setTitle(u"Task Desctiption:")
        self.label_3.setText(u"Priority:")
        self.label.setText(u"Assigned to:")
        self.label_5.setText(u"Started:")
        self.label_2.setText(u"Supervisor:")
        self.startedDateTimeEdit.setDisplayFormat(u"yyyy.MM.dd. HH:mm:ss")
        self.endDateTimeEdit.setDisplayFormat(u"yyyy.MM.dd. HH:mm:ss")
        self.label_6.setText(u"End planned:")
        self.label_4.setText(u"Status:")
        self.saveChangesButton.setText(u"Save changes")
        self.label_7.setText(u"Subscription:")
        self.showNotesButton.setText(u"Show Task Notes")
        self.subsParentStatusLabel.setText(u"Not Subscribed")
        self.subsParentPushButton.setText(u"Subscribe to parent")
        self.subsTaskPushButton.setText(u"Subscribe to task")
        self.subsTaskStatusLabel.setText(u"Not Subscribed")
        self.subsUsersPushButton.setText(u"Subscribe Users/Groups")
        self.skeyLineEdit.setText(u"skey://")

