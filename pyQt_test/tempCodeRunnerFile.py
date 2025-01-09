# settings 아이콘 설정
        settings_icon = QPixmap(":/img/settings.png")
        self.ui.label_settings_icon.setPixmap(settings_icon)
        self.ui.label_settings_icon.setScaledContents(True)
        self.ui.label_settings_icon.mousePressEvent = self.show_settings_dialog
        self.ui.label_settings_icon.setCursor(Qt.PointingHandCursor)