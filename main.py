from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import data


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class FourthWindow(Screen):
    pass


class FifthWindow(Screen):
    pass


class SixthWindow(Screen):
    pass


class ChangeUsername(Screen):
    pass


class ChangePassword(Screen):
    pass


class WindowManager(ScreenManager):
    pass



class IDKApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = data.get_theme()
        return Builder.load_file("main.kv")

    def username_changed_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Username Changed!",
                buttons=[
                    MDFlatButton(
                        text="Okay!", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    )
                ]

            )
        self.dialog.open()

    def password_changed_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Password Changed!",
                buttons=[
                    MDFlatButton(
                        text="Okay!", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    )
                ]

            )
        self.dialog.open()

    def password_copied_dialog(self, website):
        if not self.dialog:
            data.get_password(website)
            self.dialog = MDDialog(
                title=f"The username is {data.get_username(website)} and your password has been copied to the clipboard",
                buttons=[
                    MDFlatButton(
                        text="Okay!", text_color=self.theme_cls.primary_color, on_release=self.close_dialog,
                    )
                ]
            )
        self.dialog.open()

    def theme_changed_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"Please restart the app to view changes",
                buttons=[
                    MDFlatButton(
                        text="Okay!", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    )
                ]

            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


if __name__ == '__main__':
    IDKApp().run()
