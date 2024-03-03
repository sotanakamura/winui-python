from win32more.xaml import XamlApplication
from win32more.Windows.Foundation import PropertyValue
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import StackPanel, TextBlock
from win32more.Microsoft.UI.Xaml.Controls.Primitives import RepeatButton

class App(XamlApplication):
    def OnLaunched(self, args):
        self.clicks = 0

        win = Window()

        stack = StackPanel()

        incbtn = RepeatButton()
        incbtn.Width = 100
        incbtn.Delay = 500
        incbtn.Interval = 100
        incbtn.add_Click(self.Increase_Click)
        incbtn.Content = PropertyValue.CreateString("Increase")

        decbtn = RepeatButton()
        decbtn.Width = 100
        decbtn.Delay = 500
        decbtn.Interval = 100
        decbtn.add_Click(self.Decrease_Click)
        decbtn.Content = PropertyValue.CreateString("Decrease")

        self.textblock = TextBlock()
        self.textblock.Text = "Number of Clicks:"

        stack.Children.Append(incbtn)
        stack.Children.Append(decbtn)
        stack.Children.Append(self.textblock)

        win.Content = stack
        win.Activate()

    def Increase_Click(self, sender, args):
        self.clicks += 1
        self.textblock.Text = "Number of Clicks: " + str(self.clicks)

    def Decrease_Click(self, sender, args):
        if(self.clicks > 0):
            self.clicks -= 1
            self.textblock.Text = "Number of Clicks: " + str(self.clicks)

XamlApplication.Start(App)