import tkinter as tk
from tools import DnaSequenceManipulator


class InputComponent(tk.Frame):
    """
    Represent the construction of the input section of the GUI.
    """
    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.grid(row=0, rowspan=6, column=0, columnspan=4, sticky=tk.W+tk.E+tk.N+tk.S)
        self.make_widgets()

    def make_widgets(self):
        label_font = ("Helvetica", 16)
        label = tk.Label(self, text="Insert DNA sequence here: ", font=label_font)
        self.input_field = tk.Text(self, width=80, height=5, borderwidth=1, highlightbackground="grey", font=label_font)
        action_reverse_button = tk.Button(self, text="reverse", command=self.reverse, height=2, width=20,
                                       font=label_font, fg="#5900b3", relief=tk.RAISED)

        action_complement_button = tk.Button(self, text="complement", command=self.complement, height=2, width=20,
                                       font=label_font, fg="#5900b3", relief=tk.RAISED)

        action_reverse_complement_button = tk.Button(self, text="reverse complement", command=self.reverse_complement, height=2, width=20,
                                          font=label_font, fg="#5900b3", relief=tk.RAISED)
        action_refresh_button = tk.Button(self, text="clear", command=self.clear, height=2, width=20,
                                       font=label_font, fg="black")
        label.pack(side=tk.TOP, anchor=tk.NW, padx=4)
        self.input_field.pack(side=tk.TOP, padx=4, pady=5)
        action_reverse_button.pack(side=tk.LEFT, expand=tk.YES, padx=4)
        action_complement_button.pack(side=tk.LEFT, expand=tk.YES)
        action_reverse_complement_button.pack(side=tk.LEFT, expand=tk.YES)
        action_refresh_button.pack(side=tk.LEFT, expand=tk.YES)

    def _read_input_field(self):
        """
        helper method that retrieve use supplied string from the input field.
        :return:
        """
        return self.input_field.get("1.0", "end-1c")

    def reverse(self):
        sequence = self._read_input_field()
        reversed_seq = DnaSequenceManipulator(sequence).reverse_sequence()
        OutputComponent().output_field.insert(tk.END, reversed_seq)

    def complement(self):
        sequence = self._read_input_field()
        complement_seq = DnaSequenceManipulator(sequence).complement_sequence()
        OutputComponent().output_field.insert(tk.END, complement_seq)

    def reverse_complement(self):
        sequence = self._read_input_field()
        reverse_complement_seq = DnaSequenceManipulator(sequence).reverse_complement_sequence()
        OutputComponent().output_field.insert(tk.END, reverse_complement_seq)

    def clear(self):
        self.input_field.delete("1.0", "end")
        OutputComponent().output_field.delete("1.0", "end")


class OutputComponent(tk.Frame):
    """
    Represent the construction of the output section of the GUI.
    """
    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.grid(row=20, rowspan=6, column=0, columnspan=4, sticky=tk.W+tk.E+tk.N+tk.S)
        self.make_widgets()

    def make_widgets(self):
        label_font = ("Helvetica", 16)
        label_empty = tk.Label(self, text="     ")
        label = tk.Label(self, text="Converted sequence: ", font=label_font)
        self.output_field = tk.Text(self, width=80, height=5, borderwidth=1, highlightbackground="blue", font=label_font)
        label_empty.pack(side=tk.TOP)
        label.pack(side=tk.TOP, anchor=tk.NW, padx=4, pady=5)
        self.output_field.pack(side=tk.TOP, padx=4)
