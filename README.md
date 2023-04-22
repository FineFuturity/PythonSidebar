This is an API to provide a custom sidebar for use in Tkinter programs.  Very basic in its current iteration and, as such, is a work in progress.

## Prerequisites
You will need to have Python 3 and tkinter installed on your system in order to run this program.

## Running the Program
To run the program, simply run the sidebar_example.py file using Python

```
python sidebar.py
```

This will start the program and display a sidebar widget on the right side of the screen.

## Usage
The sidebar widget can be used to display additional information or controls in a tkinter program. You can add widgets to the sidebar using the add_widget method of the Sidebar class.

```
sidebar = Sidebar(root, 300, 'right')
label = tk.Label(text='My Label', font=('Arial', 12), bg='white')
sidebar.add_widget(label)
```

Widgets added to the sidebar can optionally have a hide/show button associated with them.  This is set via the `canhide` attribute when adding a widget, shown below using the previous example.

```
sidebar.add_widget(label)
```

You can also remove widgets from the sidebar using the remove_widget method.

```
sidebar.remove_widget(label)
```

## Contributing
If you would like to contribute to this project, feel free to submit a pull request.

## Authors
Initial work - https://github.com/FineFuturity (@FineFuturity)


