import tkinter as tk
from tkinter import ttk

class Sidebar:
    def __init__(self, root, width, pos):
        self.root = root
        self.sbar_frame = tk.Frame(self.root, bg='gray', width=width)
        self.sbar_frame.pack(side=pos, fill='y')
        self.sbar_frame.pack_propagate(False)  # Prevent automatic resizing

        self.frame = tk.Frame(self.sbar_frame, width=width, bg='gray')
        self.frame.pack(side='right', fill='y')
        self.frame.pack_propagate(False)  # Prevent automatic resizing
        self.widgets = {}
        self.is_hidden = False # Track the visibility of the sidebar

    def add_widget(self, widget, canhide=True):
        # Add a widget to the 
        spacer = tk.Frame(self.frame, bg='gray', height=5)
        spacer.pack(side='top', fill='x')

        master_frame = tk.Frame(self.frame, bd=1, relief='solid')
        master_frame.pack(side='top', fill='x')

        if canhide:
            hide_show_frame = tk.Frame(master_frame)
            hide_show_frame.pack(side='top', fill="x")

        widget_frame = tk.Frame(master_frame)
        widget_frame.pack(side='bottom', expand=True, fill='x')

        if canhide:
            hide_button = tk.Button(hide_show_frame, text='Hide', font=('Arial', 10), bg='gray', fg='white', command=lambda widget_frame=widget_frame: self.toggle_widget(widget_frame), bd=1, relief='solid')
            hide_button.pack(fill='x', )
            # Bind <Enter> and <Leave> events to change button color on hover
            def on_hover(event):
                event.widget.config(bg='#505050', fg='white')

            def on_leave(event):
                event.widget.config(bg='gray', fg='white')

            hide_button.bind('<Enter>', on_hover)
            hide_button.bind('<Leave>', on_leave)

        widget.pack(in_=widget_frame, side='top', fill='x')
        widget.pack_propagate(False)

        if canhide:
            self.widgets[widget_frame] = (widget, hide_button, False)

        # self.widgets[widget_frame] = (widget, hide_button, False)


    def remove_widget(self, widget):
        # Remove a widget from the sidebar
        for widget_frame, (widget, hide_button, hidden) in self.widgets.items():
            if widget == widget_frame.winfo_children()[0]:
                widget_frame.pack_forget()
                del self.widgets[widget_frame]
                break

    def toggle_widget(self, widget_frame):
        # Toggle visibility of a widget in the sidebar
        widget, hide_button, hidden = self.widgets[widget_frame]
        if hidden:
            widget_frame.pack(side='left', expand=True, fill='x')
            hide_button.config(text='Hide')
            self.widgets[widget_frame] = (widget, hide_button, False)
        else:
            widget_frame.pack_forget()
            hide_button.config(text='Show')
            self.widgets[widget_frame] = (widget, hide_button, True)
        
    def toggle_sidebar(self):
        # Toggle visibility of the sidebar
        if self.is_hidden:
            self.frame.pack(side='right', fill='y')
            self.is_hidden = False
            self.hide_show_button.config(text='Hide Sidebar')
        else:
            self.frame.pack_forget()
            self.is_hidden = True
            self.hide_show_button.config(text='Show Sidebar')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Sidebar Example')

    WIDTH = 300
    root.geometry(str(WIDTH) + "x600")
    sidebar = Sidebar(root, WIDTH, 'right')
    label = tk.Label(text='My Label', font=('Arial', 12), bg='white')
    button = tk.Button(text='Click me', font=('Arial', 12), bg='white', command=lambda: print('Button clicked!'))

    top_tree = ttk.Treeview(columns=('Attributes', 'Data'), height=15)
    top_tree['show'] = 'headings'
    # top_tree.pack(fill='both', expand=True)

    # Set column headings
    top_tree.heading('Attributes', text='Attributes', anchor='center')
    top_tree.heading('Data', text='Data', anchor='center')
    top_tree.column('#1', width=int(WIDTH/2)-1, stretch = False)
    top_tree.column('#2', width=int(WIDTH/2)-1,  stretch = False)
    top_tree.bind('<Motion>', 'break')
    # sidebar.add_widget(label)
    # sidebar.add_widget(button)
    sidebar.add_widget(top_tree, canhide=False)

    # top_bar.pack_propagate(False)
    root.mainloop()

# import tkinter as tk



# class Sidebar:
#     def __init__(self, root, width):
#         self.root = root
#         self.frame = tk.Frame(self.root, width=width, bg='gray')
#         self.frame.pack(side='right', fill='y')
#         self.frame.pack_propagate(False)  # Prevent automatic resizing
#         self.widgets = []

#     def add_widget(self, widget):
#         # Add a widget to the sidebar
#         widget.pack(side='top', fill='x')
#         self.widgets.append(widget)

#     def remove_widget(self, widget):
#         # Remove a widget from the sidebar
#         widget.pack_forget()
#         self.widgets.remove(widget)


# if __name__ == '__main__':
#     root = tk.Tk()
#     root.geometry("800x600")
#     root.title('Sidebar Example')
#     sidebar = Sidebar(root, 200)
#     label = tk.Label(sidebar.frame, text='My Widgets', font=('Arial', 12), bg='gray')
#     button = tk.Button(sidebar.frame, text='Click me', font=('Arial', 12), bg='#f0f0f0', command=lambda: print('Button clicked!'))
#     sidebar.add_widget(label)
#     sidebar.add_widget(button)
#     root.mainloop()
