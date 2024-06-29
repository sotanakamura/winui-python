English | [简体中文](README_CN.md)

![](./img.jpg)

# WinUI 3 with Python

This repository provides an example of WinUI 3 with Python. The sample program has the following features:

* Load an XAML file to layout UI components.
* Support WinUI 3 controls with Fluent Design System.
* Apply Mica.
* Adapt to a high DPI monitor.

[py-win32more](https://github.com/ynkdir/py-win32more) is used to generate "win32more" for WinUI 3.

## Requirement
* [Python from python.org](https://www.python.org/downloads/)
* [Windows App Runtime v1.5.0](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/downloads)
* [py-win32more](https://github.com/ynkdir/py-win32more) is used to generate "win32more" for WinUI 3.

You are allowed to install ``py-win32more`` through the following command:

```
pip install win32more
```

## Run the sample program

Loading the module for the first time takes time.

```
py winui-xaml.py
```

## Creating UI without XAML files (and handling events)

You can build your own GUI without writing XAML files.  
Also, you can handle events using your own functions just as example shown below.  
\*This example uses the sample program of RepeatButton.

```
py winui-click.py
```
